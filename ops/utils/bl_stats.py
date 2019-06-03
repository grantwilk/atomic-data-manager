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
# </editor-fold>


# <editor-fold desc="Helper Functions">
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
        or (data == bpy.data.images and key.startswith("Untitled")) \
        or (data == bpy.data.lights and key.startswith("Light")) \
        or (data == bpy.data.materials and key.startswith("Material")) \
        or (data == bpy.data.objects and key.startswith(default_obj_names)) \
        or (data == bpy.data.node_groups and key.startswith("NodeGroup")) \
        or (data == bpy.data.particles and key.startswith("ParticleSettings")) \
        or (data == bpy.data.textures and key.startswith("Textures")) \
        or (data == bpy.data.worlds and key.startswith("World"))
# </editor-fold>


# <editor-fold desc="Count Functions">
def count_total(data):
    # returns the amount of keys in a set of data
    return len(data.keys())


def count_unused(data):
    # returns the amount of unused data-blocks in a set of data
    return sum(1 if datablock.users == 0 else 0 for datablock in data)


def count_unnamed(data):
    # returns the amount of unnamed data-blocks in a set of data
    unnamed_datablocks = []

    for key in data.keys():
        if is_unnamed(data, key):
            unnamed_datablocks.append(key)

    return len(unnamed_datablocks)


def count_collections():
    # returns the amount of collections in the current Blender file
    return count_total(bpy.data.collections)


def count_unused_collections():
    # returns the amount of empty collections in the current Blender file
    return str(sum(1 if len(collection.all_objects.values()) == 0 else 0 for collection in bpy.data.collections))


def count_unnamed_collections():
    # returns the amount of unnamed collections in the current Blender file
    return count_unnamed(bpy.data.collections)


def count_images():
    # returns the amount of images in the current Blender file
    return count_total(bpy.data.images)


def count_unused_images():
    # returns the amount of unused images in the current Blender file
    return count_unused(bpy.data.images)


def count_unnamed_images():
    # returns the amount of unnamed images in the current Blender file
    return count_unnamed(bpy.data.images)


def count_missing_images():
    # returns the amount of images with a non-existent filepath in the current Blender file
    images = bpy.data.images
    return sum(1 if image.name != "Render Result" and not os.path.isfile(image.filepath) else 0 for image in images)


def count_lights():
    # returns the amount of lights in the current Blender file
    return count_total(bpy.data.lights)


def count_unused_lights():
    # returns the amount of unused lights in the current Blender file
    return count_unused(bpy.data.lights)


def count_unnamed_lights():
    # returns the amount of unnamed lights in the current Blender file
    return count_unnamed(bpy.data.lights)


def count_materials():
    # returns the amount of materials in the current Blender file
    return count_total(bpy.data.materials)


def count_unused_materials():
    # returns the amount of unused materials in the current Blender file
    return count_unused(bpy.data.materials)


def count_unnamed_materials():
    # returns the amount of unnamed materials in the current Blender file
    return count_unnamed(bpy.data.materials)


def count_objects():
    # returns the amount of objects in the current Blender file
    return count_total(bpy.data.objects)


def count_unnamed_objects():
    # returns the amount of unnamed objects in the current Blender file
    return count_unnamed(bpy.data.objects)


def count_particles():
    # returns the amount of particle systems in the current Blender file
    return count_total(bpy.data.particles)


def count_unused_particles():
    # returns the amount of unused particle systems in the current Blender file
    return count_unused(bpy.data.particles)


def count_unnamed_particles():
    # returns the amount of unnamed particle systems in the current Blender file
    return count_unnamed(bpy.data.particles)


def count_emitted_particles():
    # returns the  number of particles emitted in all particle systems in the current Blender file
    return sum(particle.count for particle in bpy.data.particles)


def count_emitted_particles_visible():
    # returns the the number of visible particles emitted in all particle systems in the current Blender file
    return sum(int(particle.count * (particle.display_percentage / 100)) for particle in bpy.data.particles)


def count_node_groups():
    # returns the amount of node groups in the current Blender file
    return count_total(bpy.data.node_groups)


def count_unused_node_groups():
    # returns the amount of unused node groups in the current Blender file
    return count_unused(bpy.data.node_groups)


def count_unnamed_node_groups():
    # returns the amount of unnamed node_groups in the current Blender file
    return count_unnamed(bpy.data.node_groups)


def count_textures():
    # returns the amount of textures in the current Blender file
    return count_total(bpy.data.textures)


def count_unused_textures():
    # returns the amount of unused textures in the current Blender file
    return count_unused(bpy.data.textures)


def count_unnamed_textures():
    # returns the amount of unnamed textures in the current Blender file
    return count_unnamed(bpy.data.textures)


def count_worlds():
    # returns the amount of worlds in the current Blender file
    return count_total(bpy.data.worlds)


def count_unused_worlds():
    # returns the amount of unused worlds in the current Blender file
    return count_unused(bpy.data.worlds)


def count_unnamed_worlds():
    # returns the amount of unnamed worlds in the current Blender file
    return count_unnamed(bpy.data.worlds)
# </editor-fold>


# <editor-fold desc="Get Functions">
def get_unused(data):
    # returns a list of keys of data with no users in the specified set of data
    unused_data = []
    for datablock in data:
        if datablock.users == 0:
            unused_data.append(datablock.name)
    return unused_data


def get_unused_collections():
    # returns a list of keys of collections with no objects
    unused_collections = []
    for collection in bpy.data.collections:
        if len(collection.all_objects.values()) == 0:
            unused_collections.append(collection.name)
    return unused_collections


def get_unused_images():
    # returns a list of keys of images with no users
    return get_unused(bpy.data.images)


def get_missing_images():
    # returns a list of keys of images with a non-existent filepath
    missing_images = []
    for image in bpy.data.images:
        if image.name != "Render Result" and not os.path.isfile(image.filepath):
            missing_images.append(image.name)

    return missing_images


def get_unused_lights():
    # returns a list of keys of lights with no users
    return get_unused(bpy.data.lights)


def get_unused_materials():
    # returns a list of keys of materials with no users
    return get_unused(bpy.data.materials)


def get_unused_node_groups():
    # returns a list of keys of node groups with no users
    return get_unused(bpy.data.node_groups)


def get_unused_particles():
    # returns a list of keys of particles with no users
    return get_unused(bpy.data.particles)


def get_unused_textures():
    # returns a list of keys of textures with no users
    return get_unused(bpy.data.textures)


def get_unused_worlds():
    # returns a list of keys of worlds with no users
    return get_unused(bpy.data.worlds)
# </editor-fold>