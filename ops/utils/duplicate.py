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


def duplicate_data(data, key):
    # creates a copy of the specified data-block and returns its key
    return data[key].copy().name


def collection(key):
    # creates of copy of the specified collection and links it to the scene collection
    collections = bpy.data.collections
    scene_collection = bpy.context.scene.collection

    copy_key = duplicate_data(collections, key)
    scene_collection.children.link(collections[copy_key])
    return copy_key


def image(key):
    # creates of copy of the specified image
    return duplicate_data(bpy.data.images, key)


def light(key):
    # creates of copy of the specified light
    return duplicate_data(bpy.data.lights, key)


def material(key):
    # creates of copy of the specified material
    return duplicate_data(bpy.data.materials, key)


def node_group(key):
    # creates of copy of the specified node group
    return duplicate_data(bpy.data.node_groups, key)


def particle(key):
    # creates of copy of the specified particle
    return duplicate_data(bpy.data.particles, key)


def texture(key):
    # creates of copy of the specified texture
    return duplicate_data(bpy.data.textures, key)


def world(key):
    # creates of copy of the specified world
    return duplicate_data(bpy.data.worlds, key)
