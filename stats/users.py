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

This file contains functions that return the keys of data-blocks that
use other data-blocks.

They are titled as such that the first part of the function name is the
type of the data being passed in and the second part of the function name
is the users of that type.

e.g. If you were searching for all of the places where an image is used in
a material would be searching for the image_materials() function.

"""

import bpy


def collection_all(collection_key):
    # returns a list of keys of every data-block that uses this collection

    return collection_cameras(collection_key) + \
           collection_children(collection_key) + \
           collection_lights(collection_key) + \
           collection_meshes(collection_key) + \
           collection_others(collection_key)


def collection_cameras(collection_key):
    # recursively returns a list of camera object keys that are in the
    # collection and its child collections

    users = []
    collection = bpy.data.collections[collection_key]

    # append all camera objects in our collection
    for obj in collection.objects:
        if obj.type == 'CAMERA':
            users.append(obj.name)

        # list of all child collections in our collection
        children = collection_children(collection_key)

    # append all camera objects from the child collections
    for child in children:
        for obj in bpy.data.collections[child].objects:
            if obj.type == 'CAMERA':
                users.append(obj.name)

    return distinct(users)


def collection_children(collection_key):
    # returns a list of all child collections under the specified
    # collection using recursive functions

    collection = bpy.data.collections[collection_key]

    children = collection_children_recursive(collection_key)
    children.remove(collection.name)

    return children


def collection_children_recursive(collection_key):
    # recursively returns a list of all child collections under the
    # specified collection including the collection itself

    collection = bpy.data.collections[collection_key]

    # base case
    if not collection.children:
        return [collection.name]

    # recursion case
    else:
        children = []
        for child in collection.children:
            children += collection_children(child.name)
        children.append(collection.name)
        return children


def collection_lights(collection_key):
    # returns a list of light object keys that are in the collection

    users = []
    collection = bpy.data.collections[collection_key]

    # append all light objects in our collection
    for obj in collection.objects:
        if obj.type == 'LIGHT':
            users.append(obj.name)

    # list of all child collections in our collection
    children = collection_children(collection_key)

    # append all light objects from the child collections
    for child in children:
        for obj in bpy.data.collections[child].objects:
            if obj.type == 'LIGHT':
                users.append(obj.name)

    return distinct(users)


def collection_meshes(collection_key):
    # returns a list of mesh object keys that are in the collection

    users = []
    collection = bpy.data.collections[collection_key]

    # append all mesh objects in our collection and from child
    # collections
    for obj in collection.all_objects:
        if obj.type == 'MESH':
            users.append(obj.name)

    return distinct(users)


def collection_others(collection_key):
    # returns a list of other object keys that are in the collection
    # NOTE: excludes cameras, lights, and meshes

    users = []
    collection = bpy.data.collections[collection_key]

    # object types to exclude from this search
    excluded_types = ['CAMERA', 'LIGHT', 'MESH']

    # append all other objects in our collection and from child
    # collections
    for obj in collection.all_objects:
        if obj.type not in excluded_types:
            users.append(obj.name)

    return distinct(users)


def image_all(image_key):
    # returns a list of keys of every data-block that uses this image

    return image_materials(image_key) + \
           image_node_groups(image_key) + \
           image_textures(image_key) + \
           image_worlds(image_key)


def image_materials(image_key):
    # returns a list of material keys that use the image

    users = []
    image = bpy.data.images[image_key]

    # list of node groups that use this image
    node_group_users = image_node_groups(image_key)

    for mat in bpy.data.materials:

        # if material uses a valid node tree, check each node
        if mat.use_nodes and mat.node_tree:
            for node in mat.node_tree.nodes:

                # if node is has a not none image attribute
                if hasattr(node, 'image') and node.image:

                    # if the nodes image is our image
                    if node.image.name == image.name:
                        users.append(mat.name)

                # if image in node in node group in node tree
                elif node.type == 'GROUP':

                    # if node group has a valid node tree and is in our
                    # list of node groups that use this image
                    if node.node_tree and \
                            node.node_tree.name in node_group_users:
                        users.append(mat.name)

    return distinct(users)


def image_node_groups(image_key):
    # returns a list of keys of node groups that use this image

    users = []
    image = bpy.data.images[image_key]

    # for each node group
    for node_group in bpy.data.node_groups:

        # if node group contains our image
        if node_group_has_image(node_group.name, image.name):
            users.append(node_group.name)

    return distinct(users)


def image_textures(image_key):
    # returns a list of texture keys that use the image

    users = []
    image = bpy.data.images[image_key]

    # list of node groups that use this image
    node_group_users = image_node_groups(image_key)

    for texture in bpy.data.textures:

        # if texture uses a valid node tree, check each node
        if texture.use_nodes and texture.node_tree:
            for node in texture.node_tree.nodes:

                # check image nodes that use this image
                if hasattr(node, 'image') and node.image:
                    if node.image.name == image.name:
                        users.append(texture.name)

                # check for node groups that use this image
                elif node.type == "GROUP" and node.node_tree:

                    # if node group is in our list of node groups that
                    # use this image
                    if node.node_tree.name in node_group_users:
                        users.append(texture.name)

        # otherwise check the texture's image attribute
        else:

            # if texture uses an image
            if hasattr(texture, 'image') and texture.image:

                # if texture image is our image
                if texture.image.name == image.name:
                    users.append(texture.name)

    return distinct(users)


def image_worlds(image_key):
    # returns a list of world keys that use the image

    users = []
    image = bpy.data.images[image_key]

    # list of node groups that use this image
    node_group_users = image_node_groups(image_key)

    for world in bpy.data.worlds:

        # if world uses a valid node tree, check each node
        if world.use_nodes and world.node_tree:
            for node in world.node_tree.nodes:

                # check image nodes
                if hasattr(node, 'image') and node.image:
                    if node.image.name == image.name:
                        users.append(world.name)

                # check for node groups that use this image
                elif node.type == "GROUP" and node.node_tree:
                    if node.node_tree.name in node_group_users:
                        users.append(world.name)

    return distinct(users)


def light_all(light_key):
    # returns a list of keys of every data-block that uses this light

    return light_objects(light_key)


def light_objects(light_key):
    # returns a list of light object keys that use the light data

    users = []
    light = bpy.data.lights[light_key]

    for obj in bpy.data.objects:
        if obj.type == 'LIGHT' and obj.data:
            if obj.data.name == light.name:
                users.append(obj.name)

    return distinct(users)


def material_all(material_key):
    # returns a list of keys of every data-block that uses this material

    return material_objects(material_key)


def material_objects(material_key):
    # returns a list of object keys that use this material

    users = []
    material = bpy.data.materials[material_key]

    for obj in bpy.data.objects:

        # if the object has the option to add materials
        if hasattr(obj, 'material_slots'):

            # for each material slot
            for slot in obj.material_slots:

                # if material slot has a valid material and it is our
                # material
                if slot.material and slot.material.name == material.name:
                    users.append(obj.name)

    return distinct(users)


def node_group_all(node_group_key):
    # returns a list of keys of every data-block that uses this node group

    return node_group_materials(node_group_key) + \
           node_group_node_groups(node_group_key) + \
           node_group_textures(node_group_key) + \
           node_group_worlds(node_group_key)


def node_group_materials(node_group_key):
    # returns a list of material keys that use the node group in their
    # node trees

    users = []
    node_group = bpy.data.node_groups[node_group_key]

    # node groups that use this node group
    node_group_users = node_group_node_groups(node_group_key)

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


def node_group_node_groups(node_group_key):
    # returns a list of all node groups that use this node group in
    # their node tree

    users = []
    node_group = bpy.data.node_groups[node_group_key]

    # for each search group
    for search_group in bpy.data.node_groups:

        # if the search group contains our node group
        if node_group_has_node_group(
                search_group.name, node_group.name):
            users.append(search_group.name)

    return distinct(users)


def node_group_textures(node_group_key):
    # returns a list of texture keys that use this node group in their
    # node trees

    users = []
    node_group = bpy.data.node_groups[node_group_key]

    # list of node groups that use this node group
    node_group_users = node_group_node_groups(node_group_key)

    for texture in bpy.data.textures:

        # if texture uses a valid node tree, check each node
        if texture.use_nodes and texture.node_tree:
            for node in texture.node_tree.nodes:

                # check if node is a node group and has a valid node tree
                if node.type == "GROUP" and node.node_tree:

                    # if node is our node group
                    if node.node_tree.name == node_group.name:
                        users.append(texture.name)

                    # if node is a node group that contains our node group
                    if node.node_tree.name in node_group_users:
                        users.append(texture.name)

    return distinct(users)


def node_group_worlds(node_group_key):
    # returns a list of world keys that use the node group in their node
    # trees

    users = []
    node_group = bpy.data.node_groups[node_group_key]

    # node groups that use this node group
    node_group_users = node_group_node_groups(node_group_key)

    for world in bpy.data.worlds:

        # if world uses nodes and has a valid node tree
        if world.use_nodes and world.node_tree:
            for node in world.node_tree.nodes:

                # if node is a node group and has a valid node tree
                if node.type == 'GROUP' and node.node_tree:

                    # if this node is our node group
                    if node.node_tree.name == node_group.name:
                        users.append(world.name)

                    # if this node is one of the node groups that use
                    # our node group
                    elif node.node_tree.name in node_group_users:
                        users.append(world.name)

    return distinct(users)


def node_group_has_image(node_group_key, image_key):
    # returns true if a node group contains this image

    has_image = False
    node_group = bpy.data.node_groups[node_group_key]
    image = bpy.data.images[image_key]

    # for each node in our search group
    for node in node_group.nodes:

        # base case
        # if node has a not none image attribute
        if hasattr(node, 'image') and node.image:

            # if the node group is our node group
            if node.image.name == image.name:
                has_image = True

        # recurse case
        # if node is a node group and has a valid node tree
        elif node.type == "GROUP" and node.node_tree:
            has_image = node_group_has_image(
                node.node_tree.name, image.name)

    return has_image


def node_group_has_node_group(search_group_key, node_group_key):
    # returns true if a node group contains this node group

    has_node_group = False
    search_group = bpy.data.node_groups[search_group_key]
    node_group = bpy.data.node_groups[node_group_key]

    # for each node in our search group
    for node in search_group.nodes:

        # if node is a node group and has a valid node tree
        if node.type == "GROUP" and node.node_tree:

            # base case
            # if node group is our node group
            if node.node_tree.name == node_group.name:
                has_node_group = True

            # recurse case
            # if node group is any other node group
            else:
                has_node_group = node_group_has_node_group(
                    search_group.name, node_group.name)

    return has_node_group


def node_group_has_texture(node_group_key, texture_key):
    # returns true if a node group contains this image

    has_texture = False
    node_group = bpy.data.node_groups[node_group_key]
    texture = bpy.data.textures[texture_key]

    # for each node in our search group
    for node in node_group.nodes:

        # base case
        # if node has a not none image attribute
        if hasattr(node, 'texture') and node.texture:

            # if the node group is our node group
            if node.texture.name == texture.name:
                has_texture = True

        # recurse case
        # if node is a node group and has a valid node tree
        elif node.type == "GROUP" and node.node_tree:
            has_texture = node_group_has_texture(
                node.node_tree.name, texture.name)

    return has_texture


def particle_all(particle_key):
    # returns a list of keys of every data-block that uses this particle
    # system

    return particle_objects(particle_key)


def particle_objects(particle_key):
    # returns a list of object keys that use the particle system

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


def texture_all(texture_key):
    # returns a list of keys of every data-block that uses this texture

    return texture_brushes(texture_key) + \
           texture_objects(texture_key) + \
           texture_node_groups(texture_key) + \
           texture_particles(texture_key)


def texture_brushes(texture_key):
    # returns a list of brush keys that use the texture

    users = []
    texture = bpy.data.textures[texture_key]

    for brush in bpy.data.brushes:

        # if brush has a texture
        if brush.texture:

            # if brush texture is our texture
            if brush.texture.name == texture.name:
                users.append(brush.name)

    return distinct(users)


def texture_objects(texture_key):
    # returns a list of object keys that use the texture in one of their
    # modifiers

    users = []
    texture = bpy.data.textures[texture_key]

    # list of particle systems that use our texture
    particle_users = texture_particles(texture_key)

    # append objects that use the texture in a modifier
    for obj in bpy.data.objects:

        # if object can have modifiers applied to it
        if hasattr(obj, 'modifiers'):
            for modifier in obj.modifiers:

                # if the modifier has a texture attribute that is not None
                if hasattr(modifier, 'texture') \
                        and modifier.texture:
                    if modifier.texture.name == texture.name:
                        users.append(obj.name)

                # if the modifier has a mask_texture attribute that is
                # not None
                elif hasattr(modifier, 'mask_texture') \
                        and modifier.mask_texture:
                    if modifier.mask_texture.name == texture.name:
                        users.append(obj.name)

    # append objects that use the texture in a particle system
    for particle in particle_users:

        # append all objects that use the particle system
        users += particle_objects(particle)

    return distinct(users)


def texture_node_groups(texture_key):
    # returns a list of keys of all node groups that use this texture

    users = []
    texture = bpy.data.textures[texture_key]

    # for each node group
    for node_group in bpy.data.node_groups:

        # if node group contains our texture
        if node_group_has_texture(
                node_group.name, texture.name):
            users.append(node_group.name)

    return distinct(users)


def texture_particles(texture_key):
    # returns a list of particle system keys that use the texture in
    # their texture slots

    users = []
    texture = bpy.data.textures[texture_key]

    for particle in bpy.data.particles:

        # for each texture slot in the particle system
        for texture_slot in particle.texture_slots:

            # if texture slot has a texture that is not None
            if hasattr(texture_slot, 'texture') and texture_slot.texture:

                # if texture in texture slot is our texture
                if texture_slot.texture.name == texture.name:
                    users.append(particle.name)

    return distinct(users)


def distinct(seq):
    # returns a list of distinct elements

    return list(set(seq))
