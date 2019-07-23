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


# <editor-fold desc="Size Functions">
def to_file_size(size_bytes):
    # returns the number of bytes converted to the appropriate size rounded to one decimal with a unit suffix
    # e.g. size_bytes = 1024 will return "1 KB"
    kilobyte = 1024  # bytes
    megabyte = 1048576  # bytes
    gigabyte = 1073741824  # bytes

    if 0 <= size_bytes < kilobyte:
        size_scaled = "{:.1f} B".format(size_bytes)
    elif kilobyte <= size_bytes < megabyte:
        size_scaled = "{:.1f} KB".format(size_bytes / kilobyte)
    elif megabyte <= size_bytes < gigabyte:
        size_scaled = "{:.1f} MB".format(size_bytes / megabyte)
    elif size_bytes >= gigabyte:
        size_scaled = "{:.1f} GB".format(size_bytes / gigabyte)
    else:
        size_scaled = "No Data!"

    return size_scaled


def blend_size():
    # returns the size of the current Blender file in scaled units as a string
    blend_filepath = bpy.data.filepath
    blend_bytesize = os.stat(blend_filepath).st_size if blend_filepath != '' else -1
    blend_filesize = to_file_size(blend_bytesize)

    return blend_filesize