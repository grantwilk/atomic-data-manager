"""
Copyright (C) 2019 Grant Wilk

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


def nuke_data(data):
    # removes all data-blocks from the indicated set of data
    for key in data.keys():
        data.remove(data[key])


def collections():
    # removes all collections
    nuke_data(bpy.data.collections)


def images():
    # removes all images
    nuke_data(bpy.data.images)


def lights():
    # removes all lights
    nuke_data(bpy.data.lights)


def materials():
    # removes all materials
    nuke_data(bpy.data.materials)


def node_groups():
    # removes all node groups
    nuke_data(bpy.data.node_groups)


def particles():
    # removes all particle systems
    nuke_data(bpy.data.particles)


def textures():
    # removes all textures
    nuke_data(bpy.data.textures)


def worlds():
    # removes all worlds
    nuke_data(bpy.data.worlds)
