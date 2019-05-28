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
from bpy.utils import register_class, unregister_class
from atomic_data_manager.ui.utils import blendstats
from atomic_data_manager.ui.utils import ui_layouts


# Atomic Data Manager Main Panel
class DATAMGR_PT_main_panel(bpy.types.Panel):
    """
    The primary Atomic Data Manager panel that will appear in the Scene tab of the Properties panel.
    This panel contains the Nuke/Clean/Undo buttons as well as the data set toggles and selection tools.
    """
    bl_label = "Atomic Data Manager"
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
                      text=ui_layouts.number_suffix("Collections", blendstats.count_unused_collections()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_lights", icon='LIGHT', text="")
        splitcol.prop(dmgr, "lights",
                      text=ui_layouts.number_suffix("Lights", blendstats.count_unused_lights()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_node_groups", icon='NODETREE', text="")
        splitcol.prop(dmgr, "node_groups",
                      text=ui_layouts.number_suffix("Node Groups", blendstats.count_unused_node_groups()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_textures", icon='TEXTURE', text="")
        splitcol.prop(dmgr, "textures",
                      text=ui_layouts.number_suffix("Textures", blendstats.count_unused_textures()), toggle=True)

        # RIGHT COLUMN
        col = split.column(align=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_images", icon='IMAGE_DATA', text="")
        splitcol.prop(dmgr, "images",
                      text=ui_layouts.number_suffix("Images", blendstats.count_unused_images()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_materials", icon='MATERIAL', text="")
        splitcol.prop(dmgr, "materials",
                      text=ui_layouts.number_suffix("Materials", blendstats.count_unused_materials()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_particles", icon='PARTICLES', text="")
        splitcol.prop(dmgr, "particles",
                      text=ui_layouts.number_suffix("Particles", blendstats.count_unused_particles()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("datamgr.inspect_worlds", icon='WORLD', text="")
        splitcol.prop(dmgr, "worlds",
                      text=ui_layouts.number_suffix("Worlds", blendstats.count_unused_worlds()), toggle=True)

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
