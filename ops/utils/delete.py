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
from atomic_data_manager.ops.utils import users


def delete_datablock(data, key):
    # deletes a specific data-block from a set of data
    data.remove(data[key])


def collection(key):
    # removes a specific collection
    delete_datablock(bpy.data.collections, key)


def image(key):
    # removes a specific image
    delete_datablock(bpy.data.images, key)


def light(key):
    # removes a specific light
    delete_datablock(bpy.data.lights, key)


def material(key):
    # removes a specific material
    delete_datablock(bpy.data.materials, key)


def node_group(key):
    # removes a specific node group
    delete_datablock(bpy.data.node_groups, key)


def particle(key):
    # removes a specific particle system
    delete_datablock(bpy.data.particles, key)

    # code that might not delete the object when it deletes particles
    # ... but blender doesn't let it to work >:(
    """
    users = blendusers.particles_objects(key)
    active_object = bpy.context.view_layer.objects.active

    for obj_key in users:
        index = bpy.data.objects[obj_key].particle_systems.find(key)

        # select the object
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[1].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[obj_key]

        if index != -1:
            bpy.data.objects[obj_key].particle_systems.active_index = index
            bpy.ops.object.particle_system_remove()
    """


def texture(key):
    # removes a specific texture
    delete_datablock(bpy.data.textures, key)


def world(key):
    # removes a specific world
    delete_datablock(bpy.data.worlds, key)
