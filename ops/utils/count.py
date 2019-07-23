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

Contains functions that count quantities of various data-blocks.
"""

import bpy
from atomic_data_manager.ops.utils import unused
from atomic_data_manager.ops.utils import unnamed


def collections():
    # returns the number of collections in the project
    return len(bpy.data.collections)


def unused_collections():
    # returns the number of unused collections in the project
    return len(unused.collections())


def unnamed_collections():
    # returns the number of unnamed collections in the project
    return len(unnamed.collections())


def images():
    # returns the number of images in the project
    return len(bpy.data.images)


def unused_images():
    # returns the number of unused images in the project
    return len(unused.images())


def unnamed_images():
    # returns the number of unnamed images in the project
    return len(unnamed.images())


def lights():
    # returns the number of lights in the project
    return len(bpy.data.lights)


def unused_lights():
    # returns the number of unused lights in the project
    return len(unused.lights())


def unnamed_lights():
    # returns the number of unnamed lights in the project
    return len(unnamed.lights())


def materials():
    # returns the number of materials in the project
    return len(bpy.data.materials)


def unused_materials():
    # returns the number of unused materials in the project
    return len(unused.materials())


def unnamed_materials():
    # returns the number of unnamed materials in the project
    return len(unnamed.materials())


def node_groups():
    # returns the number of node_groups in the project
    return len(bpy.data.node_groups)


def unused_node_groups():
    # returns the number of unused node_groups in the project
    return len(unused.node_groups())


def unnamed_node_groups():
    # returns the number of unnamed node groups in the project
    return len(unnamed.node_groups())


def particles():
    # returns the number of particles in the project
    return len(bpy.data.particles)


def unused_particles():
    # returns the number of unused particles in the project
    return len(unused.particles())


def unnamed_particles():
    # returns the number of unnamed particle systems in the project
    return len(unnamed.particles())


def textures():
    # returns the number of textures in the project
    return len(bpy.data.textures)


def unused_textures():
    # returns the number of unused textures in the project
    return len(unused.textures())


def unnamed_textures():
    # returns the number of unnamed textures in the project
    return len(unnamed.textures())


def worlds():
    # returns the number of worlds in the project
    return len(bpy.data.worlds)


def unused_worlds():
    # returns the number of unused worlds in the project
    return len(unused.worlds())


def unnamed_worlds():
    # returns the number of unnamed worlds in the project
    return len(unnamed.worlds())
