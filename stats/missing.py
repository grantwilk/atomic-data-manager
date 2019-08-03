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

---

This file contains functions that detect missing files in the Blender
project.

"""

import bpy
import os


def get_missing(data):
    # returns a list of keys of unpacked data-blocks with non-existent
    # filepaths

    missing = []

    # list of keys that should not be flagged
    do_not_flag = ["Render Result", "Viewer Node", "D-NOISE Export"]

    for datablock in data:

        # the absolute path to our data-block
        abspath = bpy.path.abspath(datablock.filepath)

        # if data-block is not packed and has an invalid filepath
        if not datablock.packed_files and not os.path.isfile(abspath):

            # if data-block is not in our do not flag list
            # append it to the missing data list
            if datablock.name not in do_not_flag:
                missing.append(datablock.name)

        # if data-block is packed but it does not have a filepath
        elif datablock.packed_files and not abspath:

            # if data-block is not in our do not flag list
            # append it to the missing data list
            if datablock.name not in do_not_flag:
                missing.append(datablock.name)

    return missing


def images():
    # returns a list of keys of images with a non-existent filepath
    return get_missing(bpy.data.images)


def libraries():
    # returns a list of keys of libraries with a non-existent filepath
    return get_missing(bpy.data.libraries)
