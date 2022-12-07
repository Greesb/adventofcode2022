#!/usr/bin/env python3

import dataclasses
import sys
import typing


class File(typing.TypedDict):
    name: str
    size: int


@dataclasses.dataclass
class Folder:
    name: str
    parent: typing.Union["Folder", None] = dataclasses.field(default=None)
    files: list[File] = dataclasses.field(init=False, default_factory=list)
    folders: list["Folder"] = dataclasses.field(init=False, default_factory=list)
    size: int = dataclasses.field(init=False, default=0)

    def get_folder(self, name: str) -> typing.Self | None:
        for f in self.folders:
            if f.name == name:
                return f


def get_folders_size_ge_than_required(
    folder: Folder, required: int, selected: int = sys.maxsize
) -> int:
    if selected > folder.size >= required:
        selected = folder.size

    for f in folder.folders:
        selected = get_folders_size_ge_than_required(f, required, selected)

    return selected


TOTAL_SIZE = 70000000
REQUIRED_SIZE = 30000000
base_folder = None
current_folder = None
# listing_current_folder = False
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("$ cd"):
            # listing_current_folder = False
            dirname = line.replace("$ cd ", "")
            if dirname == "..":
                current_folder = current_folder.parent
            elif base_folder == None:
                base_folder = Folder(dirname)
                current_folder = base_folder
            else:
                current_folder = current_folder.get_folder(dirname)

        elif line == "$ ls":
            pass
        elif line.startswith("dir "):
            dirname = line.replace("dir ", "")
            current_folder.folders.append(Folder(dirname, parent=current_folder))
        else:
            # file
            file_size, file_name = line.split(" ")
            file_size = int(file_size)

            current_folder.files.append(File({"name": file_name, "size": file_size}))
            current_folder.size += file_size

            f = current_folder.parent
            while f is not None:
                f.size += file_size
                f = f.parent

    print(TOTAL_SIZE)
    print(REQUIRED_SIZE)
    print(TOTAL_SIZE - base_folder.size)
    print(REQUIRED_SIZE - (TOTAL_SIZE - base_folder.size))
    print(
        get_folders_size_ge_than_required(
            base_folder, REQUIRED_SIZE - (TOTAL_SIZE - base_folder.size)
        )
    )
