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


def collection_camera(collection_key):
    # recursively returns a list of camera object keys that are in the collection and its child collections
    users = []
    collection = bpy.data.collections[collection_key]

    # list of all child collections in our collection
    children = collection_children(collection_key)

    # recursively append all cameras from child collections
    for child_key in children:
        users.append(collection_camera(child_key))

    # append all camera objects in our collection
    for obj in collection.objects:
        if obj.type == 'CAMERA':
            users.append(obj.name)

    return distinct(users)


def collection_children(collection_key):
    # returns a list of child collection keys that are in the collection  and its child collections
    users = []
    collection = bpy.data.collections[collection_key]

    # append all children of our collection
    for child in collection.children:
        users.append(child.name)

    # recurse through our children and append their children
    for user_key in users:
        users.append(collection_children(user_key))

    return distinct(users)


def collection_light(collection_key):
    # returns a list of light object keys that are in the collection indicated by collection_key
    users = []
    collection = bpy.data.collections[collection_key]

    # list of all child collections in our collection
    children = collection_children(collection_key)

    # recursively append all lights from child collections
    for child_key in children:
        users.append(collection_light(child_key))

    # append all light objects in our collection
    for obj in collection.objects:
        if obj.type == 'LIGHT':
            users.append(obj.name)

    return distinct(users)


def collection_mesh(collection_key):
    # returns a list of mesh object keys that are in the collection indicated by collection_key
    users = []
    collection = bpy.data.collections[collection_key]

    # list of all child collections in our collection
    children = collection_children(collection_key)

    # recursively append all meshes from child collections
    for child_key in children:
        users.append(collection_mesh(child_key))

    # append all mesh objects in our collection
    for obj in collection.objects:
        if obj.type == 'MESH':
            users.append(obj.name)

    return distinct(users)


def collection_others(collection_key):
    # returns a list of other object keys that are in the collection indicated by collection_key
    # excludes cameras, lights, and meshes
    users = []
    collection = bpy.data.collections[collection_key]

    # object types to exclude from this search
    excluded_types = ['CAMERA', 'LIGHT', 'MESH']

    # list of all child collections in our collection
    children = collection_children(collection_key)

    # recursively append all other objects from child collections
    for child_key in children:
        users.append(collection_others(child_key))

    # append all other objects in our collection
    for obj in collection.objects:
        if obj.type not in excluded_types:
            users.append(obj.name)

    return distinct(users)


def image_materials(image_key):
    # returns a list of material keys that use the image indicated by image_key
    users = []

    # node types that can have images
    image_nodes = ['TEX_IMAGE', 'TEX_ENVIRONMENT']

    # node groups that use this image
    node_groups = image_node_groups(image_key)

    for mat in bpy.data.materials:

        # if material uses a node tree, check each node
        if mat.use_nodes:
            for node in mat.node_tree.nodes:

                # if image in node in the main node tree
                if node.type in image_nodes and node.image:
                    if node.image.name == bpy.data.images[image_key].name:
                        users.append(mat.name)

                # if image in node in node group in node tree
                elif node.type == 'GROUP':
                    if node.node_tree and node.node_tree.name in node_groups:
                        users.append(mat.name)

    return distinct(users)


def image_node_groups(image_key):
    # recursively returns a list of node group keys that use the image indicated by image_key
    users = []
    image = bpy.data.images[image_key]

    for node_group in bpy.data.node_groups:

        # for every node in the node tree
        for node in node_group.nodes:

            # if node is a group type
            if node.type == "GROUP":

                # recurse through that node group
                users.append(image_node_groups(image_key))

            # if node is an image type
            elif hasattr(node, image):
                if node.image and node.image.name == image.name:
                    users.append(node_group.name)

    return distinct(users)


def image_texture(image_key):
    # returns a list of texture keys that use the image indicated by image_key
    users = []
    image = bpy.data.images[image_key]

    # list of node groups that use this image
    node_group_users = image_node_groups(image_key)

    for texture in bpy.data.textures:

        # if texture uses a node tree, check each node
        if texture.use_nodes:
            for node in texture.node_tree.nodes:

                # check image nodes that use this image
                if hasattr(node, 'image') and node.image:
                    if node.image.name == image.name:
                        users.append(texture.name)

                # check for node groups that use this image
                elif node.type == "GROUP":
                    if node.node_tree.name in node_group_users:
                        users.append(texture.name)

        # otherwise check the texture's image attribute
        else:
            if texture.image.name == image.name:
                users.append(texture.name)

    return distinct(users)


def image_worlds(image_key):
    # returns a list of world keys that use the image indicated by image_key
    users = []
    image = bpy.data.images[image_key]

    # list of node groups that use this image
    node_group_users = image_node_groups(image_key)

    for world in bpy.data.worlds:

        # if world uses a node tree, check each node
        if world.use_nodes:
            for node in world.node_tree.nodes:

                # check image nodes
                if hasattr(node, 'image') and node.image:
                    if node.image.name == image.name:
                        users.append(world.name)

                # check for node groups that use this image
                elif node.type == "GROUP":
                    if node.node_tree.name in node_group_users:
                        users.append(world.name)

    return distinct(users)


def objects_lights(light_key):
    # returns a list of light object keys that use the light data specified by light_key
    users = []
    light = bpy.data.lights[light_key]

    for obj in bpy.data.objects:
        if obj.type == 'LIGHT' and obj.data:
            if obj.data.name == light.name:
                users.append(obj.name)

    return distinct(users)


def material_objects(material_key):
    # returns a list of object keys that use the material data specified by material_key
    users = []
    material = bpy.data.materials[material_key]

    for obj in bpy.data.objects:

        # if the object has the option to add materials
        if hasattr(obj, 'material_slots'):

            # for each material slot
            for slot in obj.material_slots:
                if slot.material.name == material.name:
                    users.append(obj.name)

    return distinct(users)


def node_groups_materials(node_group_key):
    # returns a list of material keys that use the node group specified by node_group_key in their node trees
    users = []
    node_group = bpy.data.node_groups[node_group_key]

    # node groups that use this node group
    node_group_users = node_groups_node_groups(node_group_key)

    for material in bpy.data.materials:

        # if material uses nodes and has a valid node tree, check each node
        if material.use_nodes and material.node_tree:
            for node in material.node_tree.nodes:

                # if node is a group node
                if node.type == "GROUP" and node.node_tree:

                    # if node is the node group
                    if node.node_tree.name == node_group.name:
                        users.append(material.name)

                    # if node is using a node group contains our node group
                    if node.node_tree.name in node_group_users:
                        users.append(material.name)

    return distinct(users)


def node_groups_node_groups(node_group_key):
    # recursively returns a list of node group keys that use the node group specified by node_group_key
    users = []
    this_node_group = bpy.data.node_groups[node_group_key]

    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:

            # if node is a node group and has a valid node tree
            if node.type == 'GROUP' and node.node_tree:

                # if this node is this node group
                if node.node_tree.name == this_node_group.name:
                    users.append(node.node_tree.name)

                # if this node is any other node group
                else:
                    # recurse and append return to users
                    users.append(node_groups_node_groups(node_group.name))

    return distinct(users)


def node_groups_world(node_group_key):
    # returns a list of world keys that use the node group specified by node_group_key in their node trees
    users = []
    node_group = bpy.data.node_groups[node_group_key]

    # node groups that use this node group
    node_group_users = node_groups_node_groups(node_group_key)

    for world in bpy.data.worlds:

        # if world uses nodes and has a valid node tree
        if world.use_nodes and world.node_tree:
            for node in world.node_tree.nodes:

                # if node is a node group and has a valid node tree
                if node.type == 'GROUP' and node.node_tree:

                    # if this node is our node group
                    if node.node_tree.name == node_group.name:
                        users.append(world.name)

                    # if this node is one of the node groups that use our node group
                    elif node.node_tree.name in node_group_users:
                        users.append(world.name)

    return distinct(users)


def particles_objects(particle_key):
    # returns a list of object keys that use the particle system indicted by particle_key
    users = []
    particle_system = bpy.data.particles[particle_key]

    for obj in bpy.data.objects:

        # if object can have a particle system
        if hasattr(obj, 'particle_systems'):
            for particle in obj.particle_systems:

                # if particle settings is our particle system
                if particle.settings.name == particle_system.name:
                    users.append(obj.name)

    return distinct(users)


def textures_brushes(texture_key):
    # returns a list of brush keys that use the texture indicted by texture_key
    users = []
    texture = bpy.data.textures[texture_key]

    for brush in bpy.data.brushes:

        # if brush has a texture
        if brush.texture:

            # if brush texture is our texture
            if brush.texture.name == texture.name:
                users.append(brush.name)

    return distinct(users)


def textures_objects(texture_key):
    # returns a list of object keys that use the texture indicted by texture_key in one of their modifiers
    users = []
    texture = bpy.data.textures[texture_key]

    # list of particle systems that use our texture
    particle_users = textures_particles(texture_key)

    # append objects that use the texture in a modifier
    for obj in bpy.data.objects:

        # if object can have modifiers applied to it
        if hasattr(obj, 'modifiers'):
            for modifier in obj.modifiers:

                # if the modifier has a texture attribute
                if hasattr(modifier, 'texture'):
                    if modifier.texture.name == texture.name:
                        users.append(obj.name)

                # if the modifier has a mask_texture attribute
                elif hasattr(modifier, 'mask_texture'):
                    if modifier.mask_texture.name == texture.name:
                        users.append(obj.name)

    # append objects that use the texture in a particle system
    for particle in particle_users:

        # append all objects that use the particle system
        users.append(particles_objects(particle))

    return distinct(users)


def textures_particles(texture_key):
    # returns a list of particle system keys that use the texture indicted by texture_key in their texture slots
    users = []
    texture = bpy.data.particles[texture_key]

    for particle in bpy.data.particles:

        # for each texture slot in the particle system
        for texture_slot in particle.texture_slots:

            # if texture slot is not None
            if texture_slot:

                # if texture in texture slot is our texture
                if texture_slot.texture.name == texture.name:
                    users.append(particle.name)

    return distinct(users)


def distinct(seq):
    # returns a list of distinct elements
    return list(set(seq))
