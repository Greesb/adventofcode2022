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


def get_folders_size_le_100000(folder: Folder) -> int:
    _sum = 0
    if folder.size < 100000:
        _sum += folder.size

    for f in folder.folders:
        _sum += get_folders_size_le_100000(f)

    return _sum


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

    print(get_folders_size_le_100000(base_folder))
