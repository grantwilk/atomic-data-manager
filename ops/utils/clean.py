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
from atomic_data_manager import config
from atomic_data_manager.stats import stats


def clean_data(data):
    # removes all unused.py data-blocks from the indicated set of data
    atom = bpy.context.scene.atomic
    for key in data.keys():
        if data[key].users == 0:
            data.remove(data[key])
        elif config.ignore_fake_users and data[key].users == 1 and data[key].use_fake_user:
            data.remove(data[key])


def collections():
    # removes all collections with no objects stored in them
    for key in bpy.data.collections.keys():
        if len(bpy.data.collections[key].all_objects.values()) == 0:
            bpy.data.collections.remove(bpy.data.collections[key])


def images():
    # removes all unused.py images
    clean_data(bpy.data.images)


def lights():
    # removes all unused.py lights
    clean_data(bpy.data.lights)


def materials():
    # removes all unused.py materials
    for material_key in stats.get_unused_materials():
        bpy.data.materials.remove(bpy.data.materials[material_key])


def node_groups():
    # removes all unused.py node groups
    clean_data(bpy.data.node_groups)


def particles():
    # removes all unused.py particle systems
    clean_data(bpy.data.particles)


def textures():
    # removes all unused.py textures
    clean_data(bpy.data.textures)


def worlds():
    # removes all unused.py worlds
    clean_data(bpy.data.worlds)
