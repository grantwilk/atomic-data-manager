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

This file contains functions that detect unnamed data-blocks in the
Blender project.
"""

import bpy
import re


def collections():
    # returns the keys of all unnamed collections in the project
    unnamed = []

    for collection in bpy.data.collections:
        if re.match(r'.*\.\d\d\d$', collection.name) or collection.name.startswith("Collection"):
            unnamed.append(collection.name)

    return unnamed


def images():
    # returns the keys of all unnamed images in the project
    unnamed = []

    for image in bpy.data.images:
        if re.match(r'.*\.\d\d\d$', image.name) or image.name.startswith("Untitled"):
            unnamed.append(image.name)

    return unnamed


def lights():
    # returns the keys of all unnamed lights in the project
    unnamed = []

    for light in bpy.data.lights:
        if re.match(r'.*\.\d\d\d$', light.name) or light.name.startswith("Light"):
            unnamed.append(light.name)

    return unnamed


def materials():
    # returns the keys of all unnamed materials in the project
    unnamed = []

    for material in bpy.data.lights:
        if re.match(r'.*\.\d\d\d$', material.name) or material.name.startswith("Material"):
            unnamed.append(material.name)

    return unnamed


def objects():
    # returns the keys of all unnamed materials in the project

    # the default names of all objects by category
    curve_names = ["BezierCircle", "BezierCurve", "NurbsCircle", "NurbsCurve", "NurbsPath"]
    gpencil_names = ["GPencil", "Stroke"]
    light_names = ["Area", "Light", "Point", "Spot", "Sun"]
    lprobe_names = ["IrradianceVolume", "ReflectionCubemap", "ReflectionPlane"]
    mesh_names = ["Circle", "Cone", "Cube", "Cylinder", "Grid", "Icosphere", "Plane", "Sphere", "Torus"]
    misc_names = ["Mball", "Text", "Armature", "Lattice", "Empty", "Camera", "Speaker", "Field"]
    nurbs_names = ["SurfCircle", "SurfCurve", "SurfPatch", "SurfTorus", "Surface"]

    # the default names of all objects, compiled into one list
    default_obj_names = [
        curve_names,
        gpencil_names,
        light_names,
        lprobe_names,
        mesh_names,
        misc_names,
        nurbs_names
    ]

    unnamed = []

    for obj in bpy.data.objects:
        if re.match(r'.*\.\d\d\d$', obj.name) or obj.name.startswith(default_obj_names):
            unnamed.append(obj.name)

    return unnamed


def node_groups():
    # returns the keys of all unnamed node groups in the project
    unnamed = []

    for node_group in bpy.data.node_groups:
        if re.match(r'.*\.\d\d\d$', node_group.name) or node_group.name.startswith("NodeGroup"):
            unnamed.append(node_group.name)

    return unnamed


def particles():
    # returns the keys of all unnamed particle systems in the project
    unnamed = []

    for particle in bpy.data.particles:
        if re.match(r'.*\.\d\d\d$', particle.name) or particle.name.startswith("ParticleSettings"):
            unnamed.append(particle.name)

    return unnamed


def textures():
    # returns the keys of all unnamed textures in the project
    unnamed = []

    for texture in bpy.data.textures:
        if re.match(r'.*\.\d\d\d$', texture.name) or texture.name.startswith("Texture"):
            unnamed.append(texture.name)

    return unnamed


def worlds():
    # returns the keys of all unnamed worlds in the project
    unnamed = []

    for world in bpy.data.worlds:
        if re.match(r'.*\.\d\d\d$', world.name) or world.name.startswith("World"):
            unnamed.append(world.name)

    return unnamed