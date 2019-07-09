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


# <editor-fold desc="Collection Users">
def collection_camera(collection_key):
    # returns a list of camera object keys that are in the collection indicated by collection_key
    users = []

    for obj in bpy.data.collections[collection_key].objects:
        if obj.type == 'CAMERA':
            users.append(obj.name)

    return distinct(users)


def collection_child(collection_key):
    # returns a list of child collection keys that are in the collection indicated by collection_key
    users = []

    for child in bpy.data.collections[collection_key].children:
        users.append(child.name)

    return distinct(users)


def collection_light(collection_key):
    # returns a list of light object keys that are in the collection indicated by collection_key
    users = []

    for obj in bpy.data.collections[collection_key].objects:
        if obj.type == 'LIGHT':
            users.append(obj.name)

    return distinct(users)


def collection_mesh(collection_key):
    # returns a list of mesh object keys that are in the collection indicated by collection_key
    users = []

    for obj in bpy.data.collections[collection_key].objects:
        if obj.type == 'MESH':
            users.append(obj.name)

    return distinct(users)


def collection_others(collection_key):
    # returns a list of other object keys that are in the collection indicated by collection_key
    # excludes cameras, lights, and meshes
    users = []

    # Object types to exclude from this search
    detected_types = ['CAMERA', 'LIGHT', 'MESH']

    for obj in bpy.data.collections[collection_key].objects:
        if obj.type not in detected_types:
            users.append(obj.name)

    return distinct(users)
# </editor-fold>


# <editor-fold desc="Image Users">
def image_materials(image_key):
    # returns a list of material keys that use the image indicated by image_key
    users = []

    # node types that can have images
    image_nodes = ['TEX_IMAGE', 'TEX_ENVIRONMENT']

    # node groups that use this image
    node_groups = image_node_groups(image_key)

    for mat in bpy.data.materials:
        if mat.use_nodes:
            for node in mat.node_tree.nodes:

                # If image in node in node tree
                if node.type in image_nodes and node.image is not None:
                    if node.image.name == bpy.data.images[image_key].name:
                        users.append(mat.name)

                # If image in node in node group in node tree
                elif node.type == 'GROUP':
                    if node.node_tree is not None and node.node_tree.name in node_groups:
                        users.append(mat.name)

    return distinct(users)


def image_node_groups(image_key):
    # returns a list of node group keys that use the image indicated by image_key
    users = []

    # node types that can have images
    image_nodes = ['TEX_IMAGE', 'TEX_ENVIRONMENT']

    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:
            if node.type in image_nodes and node.image is not None:
                if node.image.name == bpy.data.images[image_key].name:
                    users.append(node_group.name)

    return distinct(users)


def image_objects(image_key):
    # returns a list of object keys that use the image indicated by image_key
    users = []

    # material keys that use the image
    materials = image_materials(image_key)

    for material_key in materials:
        for material in material_objects(material_key):
            users.append(material)

    return distinct(users)


def image_worlds(image_key):
    # returns a list of world keys that use the image indicated by image_key
    users = []

    # node types that can have images
    image_nodes = ['TEX_IMAGE', 'TEX_ENVIRONMENT']

    for world in bpy.data.worlds:
        if world.use_nodes:
            for node in world.node_tree.nodes:
                if node.type in image_nodes:
                    if node.image.name == image_key:
                        users.append(world.name)

    return distinct(users)
# </editor-fold>


# <editor-fold desc="Light Users">
def lights_lights(light_key):
    # returns a list of light object keys that use the light data specified by light_key
    users = []

    for obj in bpy.data.objects:
        if obj.type == 'LIGHT':
            if obj.data.name == light_key:
                users.append(obj.name)

    return distinct(users)
# </editor-fold>


# <editor-fold desc="Material Users">
def material_objects(material_key):
    # returns a list of object keys that use the material data specified by material_key
    users = []

    # object types that can have materials
    material_types = ['MESH', 'META', 'CURVE', 'SURFACE', 'FONT', 'GPENCIL']

    for obj in bpy.data.objects:
        if obj.type in material_types:
            for slot in obj.material_slots:
                if material_key == slot.name:
                    users.append(obj.name)

    return distinct(users)
# </editor-fold>


# <editor-fold desc="Node Group Users">
def node_groups_materials(node_group_key):
    # returns a list of material keys that use the node group specified by node_group_key in their node trees
    users = []

    # node groups that use this node group
    node_groups = node_groups_node_groups(node_group_key)

    for material in bpy.data.materials:
        if material.use_nodes:
            for node in material.node_tree.nodes:
                if node.type == 'GROUP':
                    if node.node_tree.name == node_group_key or node.node_tree.name in node_groups:
                        users.append(material.name)

    return distinct(users)


def node_groups_node_groups(node_group_key):
    # returns a list of node group keys that use the node group specified by node_group_key in their node trees
    users = []

    for node_group in bpy.data.node_groups:
            for node in node_group.nodes:
                if node.type == 'GROUP' and node.node_tree.name == node_group_key:
                    users.append(node_group.name)

    return distinct(users)


def node_groups_world(node_group_key):
    # returns a list of world keys that use the node group specified by node_group_key in their node trees
    users = []

    # node groups that use this node group
    node_groups = node_groups_node_groups(node_group_key)

    for world in bpy.data.worlds:
        if world.use_nodes:
            for node in world.node_tree.nodes:
                if node.type == 'GROUP' and node.node_tree is not None:
                    if node.node_tree.name == node_group_key or node.node_tree.name in node_groups:
                        users.append(world.name)

    return distinct(users)
# </editor-fold>


# <editor-fold desc="Particle Users">
def particles_objects(particle_key):
    # returns a list of object keys that use the particle system indicted by particle_key
    users = []

    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            for particle in obj.particle_systems:
                if particle_key == particle.name:
                    users.append(obj.name)

    return distinct(users)
# </editor-fold>


# <editor-fold desc="Texture Users">
def textures_brushes(texture_key):
    # returns a list of brush keys that use the texture indicted by texture_key
    users = []

    for brush in bpy.data.brushes:
        if brush.texture is not None:
            texture_name = brush.texture.name
            if texture_name is not None and texture_name == texture_key:
                users.append(brush.name)

    return distinct(users)


def textures_objects(texture_key):
    # returns a list of object keys that use the texture indicted by texture_key in one of their modifiers
    users = []

    # object types that can have modifiers
    modifier_objects = ['MESH', 'CURVE', 'SURFACE', 'FONT', 'GPENCIL', 'LATTICE']
    # modifier types with texture attribute
    texture_modifiers = ['DISPLACE', 'WARP', 'WAVE']
    # modifier types with mask_texture attribute
    mask_texture_modifiers = ['VERTEX_WEIGHT_PAINT', 'VERTEX_WEIGHT_PROXIMITY', 'VERTEX_WEIGHT_MIX']

    # append objects that use the texture in a modifier
    for obj in bpy.data.objects:
        if obj.type in modifier_objects:
            for modifier in obj.modifiers:

                if modifier.type in texture_modifiers:
                    texture_name = modifier.texture.name
                    if texture_name is not None and texture_name == texture_key:
                        users.append(obj.name)

                elif modifier.type in mask_texture_modifiers:
                    texture_name = modifier.mask_texture.name
                    if texture_name is not None and texture_name == texture_key:
                        users.append(obj.name)

    # append objects that use particle systems that use the texture
    particles = textures_particles(texture_key)
    for particle in particles:
        objects = particles_objects(particle)
        for obj in objects:
            users.append(obj)

    return distinct(users)


def textures_particles(texture_key):
    # returns a list of particle system keys that use the texture indicted by texture_key in their texture slots
    users = []

    for particle in bpy.data.particles:
        for texture_slot in particle.texture_slots:
            if texture_slot is not None:
                texture_name = texture_slot.texture.name
                if texture_name is not None and texture_name == texture_key:
                    users.append(particle.name)

    return distinct(users)
# </editor-fold>


def distinct(seq):
    # returns a list of distinct elements
    return list(set(seq))
