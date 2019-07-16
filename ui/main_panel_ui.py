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
from bpy.utils import register_class, unregister_class
from atomic_data_manager.ops.utils import stats
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
        category_props = [atom.collections,
                          atom.images,
                          atom.lights,
                          atom.materials,
                          atom.node_groups,
                          atom.particles,
                          atom.textures,
                          atom.worlds]

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

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "collections",
                      text=ui_layouts.number_suffix("Collections", stats.count_unused_collections()),
                      icon='GROUP', toggle=True)
        splitcol.operator("atomic.inspect_collections", icon='VIEWZOOM', text="")

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "lights",
                      text=ui_layouts.number_suffix("Lights", stats.count_unused_lights()),
                      icon='LIGHT', toggle=True)
        splitcol.operator("atomic.inspect_lights", icon='VIEWZOOM', text="")

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "node_groups",
                      text=ui_layouts.number_suffix("Node Groups", stats.count_unused_node_groups()),
                      icon='NODETREE', toggle=True)
        splitcol.operator("atomic.inspect_node_groups", icon='VIEWZOOM', text="")

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "textures",
                      text=ui_layouts.number_suffix("Textures", stats.count_unused_textures()),
                      icon='TEXTURE', toggle=True)
        splitcol.operator("atomic.inspect_textures", icon='VIEWZOOM', text="")

        # RIGHT COLUMN
        col = split.column(align=True)

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "images",
                      text=ui_layouts.number_suffix("Images", stats.count_unused_images()),
                      toggle=True, icon='IMAGE_DATA')
        splitcol.operator("atomic.inspect_images", icon='VIEWZOOM', text="")

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "materials",
                      text=ui_layouts.number_suffix("Materials", stats.count_unused_materials()),
                      icon='MATERIAL', toggle=True)
        splitcol.operator("atomic.inspect_materials", icon='VIEWZOOM', text="")

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "particles",
                      text=ui_layouts.number_suffix("Particles", stats.count_unused_particles()),
                      icon='PARTICLES', toggle=True)
        splitcol.operator("atomic.inspect_particles", icon='VIEWZOOM', text="")

        splitcol = col.split(factor=0.8, align=True)
        splitcol.prop(atom, "worlds",
                      text=ui_layouts.number_suffix("Worlds", stats.count_unused_worlds()),
                      icon='WORLD', toggle=True)
        splitcol.operator("atomic.inspect_worlds", icon='VIEWZOOM', text="")

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
