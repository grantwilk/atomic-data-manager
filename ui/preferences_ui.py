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

This file contains the Atomic preferences UI, preferences properties, and
some functions for syncing the preference properties with external factors.

"""

import bpy
from bpy.utils import register_class
from bpy.utils import unregister_class
from atomic_data_manager import config
from atomic_data_manager.updater import addon_updater_ops


def set_enable_support_me_popup(value):
    # sets the value of the enable_support_me_popup boolean property

    bpy.context.preferences.addons["atomic_data_manager"]\
        .preferences.enable_support_me_popup = value
    copy_prefs_to_config(None, None)
    bpy.ops.wm.save_userpref()


def set_last_popup_day(day):
    # sets the value of the last_popup_day float property

    bpy.context.preferences.addons["atomic_data_manager"]\
        .preferences.last_popup_day = day
    copy_prefs_to_config(None, None)


def copy_prefs_to_config(self, context):
    # copies the values of Atomic's preferences to the variables in
    # config.py for global use

    preferences = bpy.context.preferences

    atomic_preferences = preferences.addons['atomic_data_manager']\
        .preferences

    # visible atomic preferences
    config.enable_missing_file_warning = \
        atomic_preferences.enable_missing_file_warning

    config.enable_pie_menu_ui = \
        atomic_preferences.enable_pie_menu_ui

    config.enable_support_me_popup = \
        atomic_preferences.enable_support_me_popup

    config.ignore_fake_users = \
        atomic_preferences.ignore_fake_users

    # hidden atomic preferences
    config.pie_menu_type = \
        atomic_preferences.pie_menu_type

    config.pie_menu_alt = \
        atomic_preferences.pie_menu_alt

    config.pie_menu_any = \
        atomic_preferences.pie_menu_any

    config.pie_menu_ctrl = \
        atomic_preferences.pie_menu_ctrl

    config.pie_menu_oskey = \
        atomic_preferences.pie_menu_oskey

    config.pie_menu_shift = \
        atomic_preferences.pie_menu_shift

    config.last_popup_day = \
        atomic_preferences.last_popup_day


def update_pie_menu_hotkeys(self, context):
    preferences = bpy.context.preferences
    atomic_preferences = preferences.addons['atomic_data_manager'] \
        .preferences

    # add the hotkeys if the preference is enabled
    if atomic_preferences.enable_pie_menu_ui:
        add_pie_menu_hotkeys()

    # remove the hotkeys otherwise
    else:
        remove_pie_menu_hotkeys()


def add_pie_menu_hotkeys():
    # adds the pie menu hotkeys to blender's addon keymaps

    keyconfigs = bpy.context.window_manager.keyconfigs.addon

    # add a new keymap
    km = keyconfigs.keymaps.new(
        name="Window",
        space_type='EMPTY',
        region_type='WINDOW'
    )

    # add a new keymap item to that keymap
    kmi = km.keymap_items.new(
        idname="atomic.invoke_pie_menu_ui",
        type=config.pie_menu_type,
        value="PRESS",
        alt=config.pie_menu_alt,
        any=config.pie_menu_any,
        ctrl=config.pie_menu_ctrl,
        oskey=config.pie_menu_oskey,
        shift=config.pie_menu_shift,
    )

    # # point the keymap item to our pie menu
    # kmi.properties.name = "ATOMIC_MT_main_pie"
    keymaps.append((km, kmi))


def remove_pie_menu_hotkeys():
    # removes the pie menu hotkeys from blender's addon keymaps if they
    # exist there

    # remove each hotkey in our keymaps list if it exists in blenders
    # addon keymaps
    for km, kmi in keymaps:
        if kmi in km.keymap_items:
            km.keymap_items.remove(kmi)

    # clear our keymaps list
    keymaps.clear()


# Atomic Data Manager Preference Panel UI
class ATOMIC_PT_preferences_panel(bpy.types.AddonPreferences):
    bl_idname = "atomic_data_manager"

    # visible atomic preferences
    enable_missing_file_warning: bpy.props.BoolProperty(
        description="Display a warning on startup if Atomic detects "
                    "missing files in your project",
        default=True
    )

    enable_support_me_popup: bpy.props.BoolProperty(
        description="Occasionally display a popup asking if you would "
                    "like to support Remington Creative",
        default=True
    )

    ignore_fake_users: bpy.props.BoolProperty(
        description="Let the clean tool remove unused data-blocks "
                    "even if they have fake users",
        default=False
    )

    enable_pie_menu_ui: bpy.props.BoolProperty(
        description="Enable the Atomic pie menu UI, so you can clean "
                    "your project from anywhere.",
        default=True,
        update=update_pie_menu_hotkeys
    )

    # hidden atomic preferences
    pie_menu_type: bpy.props.StringProperty(
        default="D"
    )

    pie_menu_alt: bpy.props.BoolProperty(
        default=False
    )

    pie_menu_any: bpy.props.BoolProperty(
        default=False
    )

    pie_menu_ctrl: bpy.props.BoolProperty(
        default=False
    )

    pie_menu_oskey: bpy.props.BoolProperty(
        default=False
    )

    pie_menu_shift: bpy.props.BoolProperty(
        default=False
    )

    last_popup_day: bpy.props.FloatProperty(
        default=0
    )

    # add-on updater properties
    auto_check_update: bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=True,
    )

    updater_intrval_months: bpy.props.IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0,
        max=6
    )
    updater_intrval_days: bpy.props.IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
    )
    updater_intrval_hours: bpy.props.IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23
    )
    updater_intrval_minutes: bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
    )

    def draw(self, context):
        layout = self.layout

        split = layout.split()

        # left column
        col = split.column()

        # enable missing file warning toggle
        col.prop(
            self,
            "enable_missing_file_warning",
            text="Show Missing File Warning"
        )

        # enable support me popup toggle
        col.prop(
            self,
            "enable_support_me_popup",
            text="Show \"Support Me\" Popup"
        )

        # right column
        col = split.column()

        # ignore fake users toggle
        col.prop(
            self,
            "ignore_fake_users",
            text="Ignore Fake Users"
        )

        # pie menu settings
        pie_split = col.split(factor=0.55)  # nice

        # enable pie menu ui toggle
        pie_split.prop(
            self,
            "enable_pie_menu_ui",
            text="Enable Pie Menu"
        )

        # keymap item that contains our pie menu hotkey
        # note: keymap item index hardcoded with an index -- may be
        # dangerous if more keymap items are added
        kmi = bpy.context.window_manager.keyconfigs.addon.keymaps[
            'Window'].keymap_items[0]

        # put the property in a row so it can be disabled
        pie_row = pie_split.row()
        pie_row.enabled = self.enable_pie_menu_ui

        # hotkey property
        pie_row.prop(
            kmi,
            "type",
            text="",
            full_event=True
        )

        # update hotkey preferences
        self.pie_menu_type = kmi.type
        self.pie_menu_any = kmi.any
        self.pie_menu_alt = kmi.alt
        self.pie_menu_ctrl = kmi.ctrl
        self.pie_menu_oskey = kmi.oskey
        self.pie_menu_shift = kmi.shift

        separator = layout.separator()  # extra space

        # add-on updater box
        addon_updater_ops.update_settings_ui(self, context)

        # update config with any new preferences
        copy_prefs_to_config(None, None)


reg_list = [ATOMIC_PT_preferences_panel]
keymaps = []


def register():
    for cls in reg_list:
        register_class(cls)

    # make sure global preferences are updated on registration
    copy_prefs_to_config(None, None)

    # update keymaps
    add_pie_menu_hotkeys()


def unregister():
    for cls in reg_list:
        unregister_class(cls)

    remove_pie_menu_hotkeys()
