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
class ATOMIC_PT_main_panel(bpy.types.Panel):
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
        atom = bpy.context.scene.atomic
        category_props = [atom.collections, atom.images, atom.lights, atom.materials, atom.node_groups, atom.particles, atom.textures, atom.worlds]

        # Nuke and Clean Buttons
        row = layout.row(align=True)
        row.scale_y = 2.0
        row.operator("atomic.nuke", text="Nuke", icon="GHOST_ENABLED")
        row.operator("atomic.clean", text="Clean", icon="PARTICLEMODE")
        row.operator("atomic.undo", text="Undo", icon="LOOP_BACK")

        row = layout.row()

        # DATA SET TOGGLES
        split = layout.split(align=False)

        # LEFT COLUMN
        col = split.column(align=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_collections", icon='GROUP', text="")
        splitcol.prop(atom, "collections",
                      text=ui_layouts.number_suffix("Collections", blendstats.count_unused_collections()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_lights", icon='LIGHT', text="")
        splitcol.prop(atom, "lights",
                      text=ui_layouts.number_suffix("Lights", blendstats.count_unused_lights()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_node_groups", icon='NODETREE', text="")
        splitcol.prop(atom, "node_groups",
                      text=ui_layouts.number_suffix("Node Groups", blendstats.count_unused_node_groups()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_textures", icon='TEXTURE', text="")
        splitcol.prop(atom, "textures",
                      text=ui_layouts.number_suffix("Textures", blendstats.count_unused_textures()), toggle=True)

        # RIGHT COLUMN
        col = split.column(align=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_images", icon='IMAGE_DATA', text="")
        splitcol.prop(atom, "images",
                      text=ui_layouts.number_suffix("Images", blendstats.count_unused_images()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_materials", icon='MATERIAL', text="")
        splitcol.prop(atom, "materials",
                      text=ui_layouts.number_suffix("Materials", blendstats.count_unused_materials()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_particles", icon='PARTICLES', text="")
        splitcol.prop(atom, "particles",
                      text=ui_layouts.number_suffix("Particles", blendstats.count_unused_particles()), toggle=True)

        splitcol = col.split(factor=0.2, align=True)
        splitcol.operator("atomic.inspect_worlds", icon='WORLD', text="")
        splitcol.prop(atom, "worlds",
                      text=ui_layouts.number_suffix("Worlds", blendstats.count_unused_worlds()), toggle=True)

        # SELECTION OPERATORS
        row = layout.row(align=True)
        row.operator("atomic.smart_select", text='Smart Select', icon='ZOOM_SELECTED')
        if all(prop is True for prop in category_props):
            row.operator("atomic.deselect_all", text="Deselect All", icon='RESTRICT_SELECT_ON')
        else:
            row.operator("atomic.select_all", text="Select All", icon='RESTRICT_SELECT_OFF')


reg_list = [ATOMIC_PT_main_panel]


def register():
    for cls in reg_list:
        register_class(cls)


def unregister():
    for cls in reg_list:
        unregister_class(cls)
