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

This file contains functions that detect data-blocks that have no users,
as determined by stats.users.py

"""

import bpy
from atomic_data_manager import config
from atomic_data_manager.stats import users


def collections():
    # returns a list of keys of unused collections

    unused = []

    for collection in bpy.data.collections:
        if not users.collection_all(collection.name):
            unused.append(collection.name)

    return unused


def images():
    # returns a list of keys of unused images

    unused = []

    for image in bpy.data.images:
        if not users.image_all(image.name):

            # check if image has a fake user or if ignore fake users
            # is enabled
            if not image.has_fake_user or config.ignore_fake_users:
                unused.append(image.name)

    return unused


def lights():
    # returns a list of keys of unused lights

    unused = []

    for light in bpy.data.lights:
        if not users.light_all(light.name):

            # check if light has a fake user or if ignore fake users
            # is enabled
            if not light.has_fake_user or config.ignore_fake_users:
                unused.append(light.name)

    return unused


def materials():
    # returns a list of keys of unused materials

    unused = []

    for material in bpy.data.materials:
        if not users.material_all(material.name):

            # check if material has a fake user or if ignore fake users
            # is enabled
            if not material.has_fake_user or config.ignore_fake_users:
                unused.append(material.name)

    return unused


def node_groups():
    # returns a list of keys of unused node_groups

    unused = []

    for node_group in bpy.data.node_groups:
        if not users.node_group_all(node_group.name):

            # check if node group has a fake user or if ignore fake users
            # is enabled
            if not node_group.has_fake_user or config.ignore_fake_users:
                unused.append(node_group.name)

    return unused


def particles():
    # returns a list of keys of unused particles

    unused = []

    for particle in bpy.data.particles:
        if not users.particle_all(particle.name):

            # check if particle system has a fake user or if ignore fake users
            # is enabled
            if not particle.has_fake_user or config.ignore_fake_users:
                unused.append(particle.name)

    return unused


def textures():
    # returns a list of keys of unused textures

    unused = []

    for texture in bpy.data.textures:
        if not users.texture_all(texture.name):

            # check if texture has a fake user or if ignore fake users
            # is enabled
            if not texture.has_fake_user or config.ignore_fake_users:
                unused.append(texture.name)

    return unused


def worlds():
    # returns a list of keys of unused worlds

    unused = []

    for world in bpy.data.worlds:
        if world.users == 0:

            # check if world has a fake user or if ignore fake users
            # is enabled
            if not world.has_fake_user or config.ignore_fake_users:
                unused.append(world.name)

    return unused
