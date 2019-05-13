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
from atomic_data_manager.ui.utils import blendstats
from atomic_data_manager.ui.utils import ui_layouts


# Data Manager Main Panel
class DATAMGR_PT_main_panel(bpy.types.Panel):
    """
    The primary Data Manager panel that will appear in the Scene tab of the Properties panel.
    This panel contains the Nuke/Clean/Undo buttons as well as the data set toggles and selection tools.
    """
    bl_label = "Data Manager"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        dmgr = bpy.context.scene.datamgr
        category_props = [dmgr.collections, dmgr.images, dmgr.lights, dmgr.materials, dmgr.node_groups, dmgr.particles, dmgr.textures, dmgr.worlds]

        # Nuke and Clean Buttons
        row = layout.row(align=True)
        row.scale_y = 2.0
        row.operator("datamgr.nuke", text="Nuke", icon="GHOST_ENABLED")
        row.operator("datamgr.clean", text="Clean", icon="PARTICLEMODE")
        row.operator("datamgr.undo", text="Undo", icon="LOOP_BACK")

        row = layout.row()

        # DATA SET TOGGLES
        split = layout.split(align=False)

        # LEFT COLUMN
        col = split.column(align=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_collections", icon='GROUP', text="")
        splitcol.prop(dmgr, "collections",
                      text=ui_layouts.number_suffix("Collections", blendstats.collections_unused()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_lights", icon='LIGHT', text="")
        splitcol.prop(dmgr, "lights",
                      text=ui_layouts.number_suffix("Lights", blendstats.lights_unused()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_node_groups", icon='NODETREE', text="")
        splitcol.prop(dmgr, "node_groups",
                      text=ui_layouts.number_suffix("Node Groups", blendstats.node_groups_unused()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_textures", icon='TEXTURE', text="")
        splitcol.prop(dmgr, "textures",
                      text=ui_layouts.number_suffix("Textures", blendstats.textures_unused()), toggle=True)

        # RIGHT COLUMN
        col = split.column(align=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_images", icon='IMAGE_DATA', text="")
        splitcol.prop(dmgr, "images",
                      text=ui_layouts.number_suffix("Images", blendstats.images_unused()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_materials", icon='MATERIAL', text="")
        splitcol.prop(dmgr, "materials",
                      text=ui_layouts.number_suffix("Materials", blendstats.materials_unused()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_particles", icon='PARTICLES', text="")
        splitcol.prop(dmgr, "particles",
                      text=ui_layouts.number_suffix("Particles", blendstats.particles_unused()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_worlds", icon='WORLD', text="")
        splitcol.prop(dmgr, "worlds",
                      text=ui_layouts.number_suffix("Worlds", blendstats.worlds_unused()), toggle=True)

        # SELECTION OPERATORS
        row = layout.row(align=True)
        row.operator("datamgr.smart_select", text='Smart Select', icon='ZOOM_SELECTED')
        if all(prop is True for prop in category_props):
            row.operator("datamgr.deselect_all", text="Deselect All", icon='RESTRICT_SELECT_ON')
        else:
            row.operator("datamgr.select_all", text="Select All", icon='RESTRICT_SELECT_OFF')


reg_list = [DATAMGR_PT_main_panel]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
