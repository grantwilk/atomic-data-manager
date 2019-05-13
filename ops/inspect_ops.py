"""
Copyright (C) 2019 Grant Wilk

This file is part of Data MGR.

Data MGR is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Data MGR is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with Data MGR.  If not, see <https://www.gnu.org/licenses/>.
"""

import bpy
from bpy.utils import register_class, unregister_class
from atomic_data_manager.ops.utils import duplicate, delete


# Data Manager Inspection Rename Operator
class DATAMGR_OT_inspection_rename(bpy.types.Operator):
    """Rename this data-block"""
    bl_idname = "datamgr.rename"
    bl_label = "Rename Data-Block To"

    def draw(self, context):
        dmgr = bpy.context.scene.datamgr

        layout = self.layout
        row = layout.row()
        row.prop(dmgr, "rename_field", text="", icon="GREASEPENCIL")

    def execute(self, context):
        dmgr = bpy.context.scene.datamgr
        inspection = dmgr.active_inspection

        name = dmgr.rename_field

        if inspection == 'COLLECTIONS':
            bpy.data.collections[dmgr.collections_field].name = name
            dmgr.collections_field = name

        if inspection == 'IMAGES':
            bpy.data.images[dmgr.images_field].name = name
            dmgr.images_field = name

        if inspection == 'LIGHTS':
            bpy.data.lights[dmgr.lights_field].name = name
            dmgr.lights_field = name

        if inspection == 'MATERIALS':
            bpy.data.materials[dmgr.materials_field].name = name
            dmgr.materials_field = name

        if inspection == 'NODE_GROUPS':
            bpy.data.node_groups[dmgr.node_groups_field].name = name
            dmgr.node_groups_field = name

        if inspection == 'PARTICLES':
            bpy.data.particles[dmgr.particles_field].name = name
            dmgr.particles_field = name

        if inspection == 'TEXTURES':
            bpy.data.textures[dmgr.textures_field].name = name
            dmgr.textures_field = name

        if inspection == 'WORLDS':
            bpy.data.worlds[dmgr.worlds_field].name = name
            dmgr.worlds_field = name

        dmgr.rename_field = ""
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=200)


class DATAMGR_OT_inspection_replace(bpy.types.Operator):
    """Replace a data-block with another data-block"""
    bl_idname = "datamgr.replace"
    bl_label = "Replace Data-Block With"

    def draw(self, context):
        dmgr = bpy.context.scene.datamgr
        inspection = dmgr.active_inspection

        layout = self.layout
        row = layout.row()

        if inspection == 'IMAGES':
            row.prop_search(dmgr, "replace_field", bpy.data, "images", text="")
        if inspection == 'LIGHTS':
            row.prop_search(dmgr, "replace_field", bpy.data, "lights", text="")
        if inspection == 'MATERIALS':
            row.prop_search(dmgr, "replace_field", bpy.data, "materials", text="")
        if inspection == 'NODE_GROUPS':
            row.prop_search(dmgr, "replace_field", bpy.data, "node_groups", text="")
        if inspection == 'PARTICLES':
            row.prop_search(dmgr, "replace_field", bpy.data, "particles", text="")
        if inspection == 'TEXTURES':
            row.prop_search(dmgr, "replace_field", bpy.data, "textures", text="")
        if inspection == 'WORLDS':
            row.prop_search(dmgr, "replace_field", bpy.data, "worlds", text="")

    def execute(self, context):
        dmgr = bpy.context.scene.datamgr
        inspection = dmgr.active_inspection

        if inspection == 'IMAGES' and dmgr.replace_field in bpy.data.images.keys():
            bpy.data.images[dmgr.images_field].user_remap(bpy.data.images[dmgr.replace_field])
            dmgr.images_field = dmgr.replace_field

        if inspection == 'LIGHTS' and dmgr.replace_field in bpy.data.lights.keys():
            bpy.data.lights[dmgr.lights_field].user_remap(bpy.data.lights[dmgr.replace_field])
            dmgr.lights_field = dmgr.replace_field

        if inspection == 'MATERIALS' and dmgr.replace_field in bpy.data.materials.keys():
            bpy.data.materials[dmgr.materials_field].user_remap(bpy.data.materials[dmgr.replace_field])
            dmgr.materials_field = dmgr.replace_field

        if inspection == 'NODE_GROUPS' and dmgr.replace_field in bpy.data.node_groups.keys():
            bpy.data.node_groups[dmgr.node_groups_field].user_remap(bpy.data.node_groups[dmgr.replace_field])
            dmgr.node_groups_field = dmgr.replace_field

        if inspection == 'PARTICLES' and dmgr.replace_field in bpy.data.particles.keys():
            bpy.data.particles[dmgr.particles_field].user_remap(bpy.data.particles[dmgr.replace_field])
            dmgr.particles_field = dmgr.replace_field

        if inspection == 'TEXTURES' and dmgr.replace_field in bpy.data.textures.keys():
            bpy.data.textures[dmgr.textures_field].user_remap(bpy.data.textures[dmgr.replace_field])
            dmgr.textures_field = dmgr.replace_field

        if inspection == 'WORLDS' and dmgr.replace_field in bpy.data.worlds.keys():
            bpy.data.worlds[dmgr.worlds_field].user_remap(bpy.data.worlds[dmgr.replace_field])
            dmgr.worlds_field = dmgr.replace_field

        dmgr.replace_field = ""
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=200)


# Data Manager Inspection Rename Operator
class DATAMGR_OT_inspection_toggle_fake_user(bpy.types.Operator):
    """Save this data-block even if it has no users"""
    bl_idname = "datamgr.toggle_fake_user"
    bl_label = "Toggle Fake User"

    def execute(self, context):
        dmgr = bpy.context.scene.datamgr
        inspection = dmgr.active_inspection

        if inspection == 'IMAGES':
            image = bpy.data.images[dmgr.images_field]
            bpy.data.images[dmgr.images_field].use_fake_user = not image.use_fake_user
        if inspection == 'LIGHTS':
            light = bpy.data.lights[dmgr.lights_field]
            bpy.data.lights[dmgr.lights_field].use_fake_user = not light.use_fake_user
        if inspection == 'MATERIALS':
            material = bpy.data.materials[dmgr.materials_field]
            bpy.data.materials[dmgr.materials_field].use_fake_user = not material.use_fake_user
        if inspection == 'NODE_GROUPS':
            node_group = bpy.data.node_groups[dmgr.node_groups_field]
            bpy.data.node_groups[dmgr.node_groups_field].use_fake_user = not node_group.use_fake_user
        if inspection == 'TEXTURES':
            texture = bpy.data.textures[dmgr.textures_field]
            bpy.data.textures[dmgr.textures_field].use_fake_user = not texture.use_fake_user
        if inspection == 'WORLDS':
            world = bpy.data.worlds[dmgr.worlds_field]
            bpy.data.worlds[dmgr.worlds_field].use_fake_user = not world.use_fake_user

        return {'FINISHED'}


# Data Manager Inspection Duplicate Operator
class DATAMGR_OT_inspection_duplicate(bpy.types.Operator):
    """Duplicate this data-block"""
    bl_idname = "datamgr.inspection_duplicate"
    bl_label = "Inspection Duplicate"

    def execute(self, context):
        dmgr = bpy.context.scene.datamgr
        inspection = dmgr.active_inspection

        if inspection == 'COLLECTIONS':
            key = dmgr.collections_field
            collections = bpy.data.collections

            if key in collections.keys():
                copy_key = duplicate.collection(key)
                dmgr.collections_field = copy_key

        elif inspection == 'IMAGES':
            key = dmgr.images_field
            images = bpy.data.images

            if key in images.keys():
                copy_key = duplicate.image(key)
                dmgr.images_field = copy_key

        elif inspection == 'LIGHTS':
            key = dmgr.lights_field
            lights = bpy.data.lights

            if key in lights.keys():
                copy_key = duplicate.light(key)
                dmgr.lights_field = copy_key

        elif inspection == 'MATERIALS':
            key = dmgr.materials_field
            materials = bpy.data.materials

            if key in materials.keys():
                copy_key = duplicate.material(key)
                dmgr.materials_field = copy_key

        elif inspection == 'NODE_GROUPS':
            key = dmgr.node_groups_field
            node_groups = bpy.data.node_groups

            if key in node_groups.keys():
                copy_key = duplicate.node_group(key)
                dmgr.node_groups_field = copy_key

        elif inspection == 'PARTICLES':
            key = dmgr.particles_field
            particles = bpy.data.particles

            if key in particles.keys():
                copy_key = duplicate.particle(key)
                dmgr.particles_field = copy_key

        elif inspection == 'TEXTURES':
            key = dmgr.textures_field
            textures = bpy.data.textures

            if key in textures.keys():
                copy_key = duplicate.texture(key)
                dmgr.textures_field = copy_key

        elif inspection == 'WORLDS':
            key = dmgr.worlds_field
            worlds = bpy.data.worlds

            if key in worlds.keys():
                copy_key = duplicate.world(key)
                dmgr.worlds_field = copy_key

        return {'FINISHED'}


# Data Manager Inspection Delete Operator
class DATAMGR_OT_inspection_delete(bpy.types.Operator):
    """Forcibly delete this data-block"""
    bl_idname = "datamgr.inspection_delete"
    bl_label = "Inspection Delete"

    def execute(self, context):
        dmgr = bpy.context.scene.datamgr
        inspection = dmgr.active_inspection

        if inspection == 'COLLECTIONS':
            key = dmgr.collections_field
            collections = bpy.data.collections

            if key in collections.keys():
                delete.collection(key)
                dmgr.collections_field = ""

        elif inspection == 'IMAGES':
            key = dmgr.images_field
            images = bpy.data.images

            if key in images.keys():
                delete.image(key)
                dmgr.images_field = ""

        elif inspection == 'LIGHTS':
            key = dmgr.lights_field
            lights = bpy.data.lights

            if key in lights.keys():
                delete.light(key)
                dmgr.lights_field = ""

        elif inspection == 'MATERIALS':
            key = dmgr.materials_field
            materials = bpy.data.materials

            if key in materials.keys():
                delete.material(key)
                dmgr.materials_field = ""

        elif inspection == 'NODE_GROUPS':
            key = dmgr.node_groups_field
            node_groups = bpy.data.node_groups

            if key in node_groups.keys():
                delete.node_group(key)
                dmgr.node_groups_field = ""

        elif inspection == 'PARTICLES':
            key = dmgr.particles_field
            particles = bpy.data.particles
            if key in particles.keys():
                delete.particle(key)
                dmgr.particles_field = ""

        elif inspection == 'TEXTURES':
            key = dmgr.textures_field
            textures = bpy.data.textures

            if key in textures.keys():
                delete.texture(key)
                dmgr.textures_field = ""

        elif inspection == 'WORLDS':
            key = dmgr.worlds_field
            worlds = bpy.data.worlds

            if key in worlds.keys():
                delete.world(key)
                dmgr.worlds_field = ""

        return {'FINISHED'}


reg_list = [DATAMGR_OT_inspection_rename,
            DATAMGR_OT_inspection_replace,
            DATAMGR_OT_inspection_toggle_fake_user,
            DATAMGR_OT_inspection_duplicate,
            DATAMGR_OT_inspection_delete]


def register():
    for item in reg_list:
        register_class(item)


def unregister():
    for item in reg_list:
        unregister_class(item)
