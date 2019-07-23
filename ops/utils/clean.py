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

This file contains functions for cleaning out specific data categories.

"""

import bpy
from atomic_data_manager.stats import unused


def collections():
    # removes all unused collections from the project
    for collection_key in unused.collections():
        bpy.data.collections.remove(bpy.data.collections[collection_key])


def images():
    # removes all unused images from the project
    for image_key in unused.images():
        bpy.data.images.remove(bpy.data.images[image_key])


def lights():
    # removes all unused lights from the project
    for light_key in unused.lights():
        bpy.data.lights.remove(bpy.data.lights[light_key])


def materials():
    # removes all unused materials from the project
    for light_key in unused.materials():
        bpy.data.materials.remove(bpy.data.materials[light_key])


def node_groups():
    # removes all unused node groups from the project
    for node_group_key in unused.node_groups():
        bpy.data.node_groups.remove(bpy.data.node_groups[node_group_key])


def particles():
    # removes all unused particle systems from the project
    for particle_key in unused.particles():
        bpy.data.particles.remove(bpy.data.particles[particle_key])


def textures():
    # removes all unused textures from the project
    for texture_key in unused.textures():
        bpy.data.textures.remove(bpy.data.textures[texture_key])


def worlds():
    # removes all unused worlds from the project
    for world_key in unused.worlds():
        bpy.data.worlds.remove(bpy.data.worlds[world_key])
