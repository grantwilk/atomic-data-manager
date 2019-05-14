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
import os
import re


# <editor-fold desc="Size Helper Functions">
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
# </editor-fold>


# <editor-fold desc="Special-Use Helper Functions">
def is_unnamed(data, key):
    # returns true if an object is unnamed, false otherwise
    # a value is considered unnamed if it has a default name (e.g. Cube) or ends with ".###" (e.g. Rock.001)

    # the default names of all objects by category
    curve_names = ("BezierCircle", "BezierCurve", "NurbsCircle", "NurbsCurve", "NurbsPath")
    gpencil_names = ("GPencil", "Stroke")
    light_names = ("Area", "Light", "Point", "Spot", "Sun")
    lprobe_names = ("IrradianceVolume", "ReflectionCubemap", "ReflectionPlane")
    mesh_names = ("Circle", "Cone", "Cube", "Cylinder", "Grid", "Icosphere", "Plane", "Sphere", "Torus")
    misc_names = ("Mball", "Text", "Armature", "Lattice", "Empty", "Camera", "Speaker", "Field")
    nurbs_names = ("SurfCircle", "SurfCurve", "SurfPatch", "SurfTorus", "Surface")

    # the default names of all objects
    default_obj_names = curve_names + gpencil_names + light_names + lprobe_names + mesh_names + misc_names + nurbs_names

    return re.match(r'.*\.\d\d\d$', key) \
        or (data == bpy.data.collections and key.startswith("Collection")) \
        or (data == bpy.data.images and key.startswith("Images")) \
        or (data == bpy.data.lights and key.startswith("Light")) \
        or (data == bpy.data.materials and key.startswith("Material")) \
        or (data == bpy.data.objects and key.startswith(default_obj_names)) \
        or (data == bpy.data.node_groups and key.startswith("NodeGroup")) \
        or (data == bpy.data.particles and key.startswith("ParticleSettings")) \
        or (data == bpy.data.textures and key.startswith("Textures")) \
        or (data == bpy.data.worlds and key.startswith("World"))
# </editor-fold>


# <editor-fold desc="Generic Count Functions">
def total_count(data):
    # returns the amount of keys in a set of data
    return len(data.keys())


def unused_count(data):
    # returns the amount of unused data-blocks in a set of data
    return sum(1 if datablock.users == 0 else 0 for datablock in data)


def unnamed_count(data):
    # returns the amount of unnamed data-blocks in a set of data
    unnamed_datablocks = []

    for key in data.keys():
        if is_unnamed(data, key):
            unnamed_datablocks.append(key)

    return len(unnamed_datablocks)
# </editor-fold>


# <editor-fold desc="Data Set Specific Functions">
def collections_count():
    # returns the amount of collections in the current Blender file
    return total_count(bpy.data.collections)


def collections_unused():
    # returns the amount of empty collections in the current Blender file
    return str(sum(1 if len(collection.all_objects.values()) == 0 else 0 for collection in bpy.data.collections))


def collections_unnamed():
    # returns the amount of unnamed collections in the current Blender file
    return unnamed_count(bpy.data.collections)


def images_count():
    # returns the amount of images in the current Blender file
    return total_count(bpy.data.images)


def images_unused():
    # returns the amount of unused images in the current Blender file
    return unused_count(bpy.data.images)


def images_unnamed():
    # returns the amount of unnamed images in the current Blender file
    return unnamed_count(bpy.data.images)


def lights_count():
    # returns the amount of lights in the current Blender file
    return total_count(bpy.data.lights)


def lights_unused():
    # returns the amount of unused lights in the current Blender file
    return unused_count(bpy.data.lights)


def lights_unnamed():
    # returns the amount of unnamed lights in the current Blender file
    return unnamed_count(bpy.data.lights)


def images_size():
    # returns the size of all images in the current Blender file in scaled units as a string
    images_bytesize = sum(image.packed_file.size if image.packed_file is not None else 0 for image in bpy.data.images)
    images_filesize = to_file_size(images_bytesize)

    return images_filesize


def images_unused_size():
    # returns the size of all unused images in the current Blender file in scaled units as a string
    images_unused_bytesize = sum(
        image.packed_file.size if image.packed_file is not None and image.users == 0 else 0 for image in
        bpy.data.images)
    images_unused_filesize = to_file_size(images_unused_bytesize)

    return images_unused_filesize


def materials_count():
    # returns the amount of materials in the current Blender file
    return total_count(bpy.data.materials)


def materials_unused():
    # returns the amount of unused materials in the current Blender file
    return unused_count(bpy.data.materials)


def materials_unnamed():
    # returns the amount of unnamed materials in the current Blender file
    return unnamed_count(bpy.data.materials)


def objects_count():
    # returns the amount of objects in the current Blender file
    return total_count(bpy.data.objects)


def objects_unnamed():
    # returns the amount of unnamed objects in the current Blender file
    return unnamed_count(bpy.data.objects)


def particles_count():
    # returns the amount of particle systems in the current Blender file
    return total_count(bpy.data.particles)


def particles_unused():
    # returns the amount of unused particle systems in the current Blender file
    return unused_count(bpy.data.particles)


def particles_unnamed():
    # returns the amount of unnamed particle systems in the current Blender file
    return unnamed_count(bpy.data.particles)


def particles_sum_particles():
    # returns the sum of the number of particles in all particle systems in the current Blender file
    return sum(particle.count for particle in bpy.data.particles)


def particles_sum_visible():
    # returns the sum of the number of particles in all particle systems in the current Blender file
    return sum(int(particle.count * (particle.display_percentage / 100)) for particle in bpy.data.particles)


def node_groups_count():
    # returns the amount of node groups in the current Blender file
    return total_count(bpy.data.node_groups)


def node_groups_unused():
    # returns the amount of unused node groups in the current Blender file
    return unused_count(bpy.data.node_groups)


def node_groups_unnamed():
    # returns the amount of unnamed node_groups in the current Blender file
    return unnamed_count(bpy.data.node_groups)


def textures_count():
    # returns the amount of textures in the current Blender file
    return total_count(bpy.data.textures)


def textures_unused():
    # returns the amount of unused textures in the current Blender file
    return unused_count(bpy.data.textures)


def textures_unnamed():
    # returns the amount of unnamed textures in the current Blender file
    return unnamed_count(bpy.data.textures)


def worlds_count():
    # returns the amount of worlds in the current Blender file
    return total_count(bpy.data.worlds)


def worlds_unused():
    # returns the amount of unused worlds in the current Blender file
    return unused_count(bpy.data.worlds)


def worlds_unnamed():
    # returns the amount of unnamed worlds in the current Blender file
    return unnamed_count(bpy.data.worlds)
# </editor-fold>
