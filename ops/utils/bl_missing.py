"""
Copyright (C) 2019 Remington Creative

This file is part of Atomic Data Manager.

Atomic Data Manager is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Atomic Data Manager is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with Atomic Data Manager.  If not, see <https://www.gnu.org/licenses/>.
"""

import bpy
import os


def get_missing(data):
    # returns a list of keys of non-packed datablocks with a non-existent filepath
    missing = []
    for datablock in data:
        if datablock.filepath and not os.path.isfile(datablock.filepath) and not datablock.packed_files.keys():
            missing.append(datablock.name)

    return missing


def get_images():
    # returns a list of keys of images with a non-existent filepath
    return get_missing(bpy.data.images)


def get_libraries():
    # returns a list of keys of libraries with a non-existent filepath
    return get_missing(bpy.data.libraries)
