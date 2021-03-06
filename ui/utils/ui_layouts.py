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

This file contains basic UI layouts for the Atomic add-on that can be
used throughout the interface.

"""

import bpy


def box_list(layout, title=None, items=None, columns=2, icon=None):
    # a title label followed by a box that contains a two column list of
    # items, each of which is preceded by a uniform icon that does not
    # change depending on the objects type

    # box list title
    row = layout.row()  # extra row for additional spacing

    if title is not None:
        row = layout.row()
        row.label(text=title)

    box = layout.box()

    # if the list has elements
    if items is not None and len(items) != 0:

        # display the list
        flow = box.column_flow(columns=columns)
        for item in items:
            if icon is not None:
                flow.label(text=item, icon=icon)
            else:
                flow.label(text=item)

    # if the list has no elements
    else:

        # display the none label
        row = box.row()
        row.enabled = False
        row.label(text="none")


def box_list_diverse(layout, title, items, columns=2):
    # a title label followed by a box that contains a two column list of
    # items, each of which is preceded by an icon that changes depending
    # on the type of object that is being listed

    # box list title
    row = layout.row()  # extra row for additional spacing
    row = layout.row()
    row.label(text=title)
    box = layout.box()

    # if the list has elements
    if len(items) != 0:

        # display the list
        flow = box.column_flow(columns=columns)
        objects = bpy.data.objects
        for item in items:
            if objects[item].type == 'ARMATURE':
                flow.label(text=item, icon="OUTLINER_OB_ARMATURE")

            elif objects[item].type == 'CAMERA':
                flow.label(text=item, icon="OUTLINER_OB_CAMERA")

            elif objects[item].type == 'CURVE':
                flow.label(text=item, icon="OUTLINER_OB_CURVE")

            elif objects[item].type == 'EMPTY':
                flow.label(text=item, icon="OUTLINER_OB_EMPTY")

            elif objects[item].type == 'FONT':
                flow.label(text=item, icon="OUTLINER_OB_FONT")

            elif objects[item].type == 'GPENCIL':
                flow.label(text=item, icon="OUTLINER_OB_GREASEPENCIL")

            elif objects[item].type == 'LATTICE':
                flow.label(text=item, icon="OUTLINER_OB_LATTICE")

            elif objects[item].type == 'LIGHT':
                flow.label(text=item, icon="OUTLINER_OB_LIGHT")

            elif objects[item].type == 'LIGHT_PROBE':
                flow.label(text=item, icon="OUTLINER_OB_LIGHTPROBE")

            elif objects[item].type == 'MESH':
                flow.label(text=item, icon="OUTLINER_OB_MESH")

            elif objects[item].type == 'META':
                flow.label(text=item, icon="OUTLINER_OB_META")

            elif objects[item].type == 'SPEAKER':
                flow.label(text=item, icon="OUTLINER_OB_SPEAKER")

            elif objects[item].type == 'SURFACE':
                flow.label(text=item, icon="OUTLINER_OB_SURFACE")

            # if the object doesn't fit any of the previous types
            else:
                flow.label(text=item, icon="QUESTION")

    # if the list has no elements
    else:

        # display the none label
        row = box.row()
        row.enabled = False
        row.label(text="none")


def inspect_header(layout, atom_prop, data):
    # a single column containing a search property and basic data
    # manipulation functions that appears at the top of all inspect data
    # set dialogs

    atom = bpy.context.scene.atomic

    # exterior box and prop search for data-blocks
    col = layout.column(align=True)
    box = col.box()
    row = box.row()
    split = row.split()
    split.prop_search(atom, atom_prop, bpy.data, data, text="")

    # convert the data set string into an actual data set reference
    data = getattr(bpy.data, data)

    # get the string value of the string property
    text_field = getattr(atom, atom_prop)

    # determine whether or not the text entered in the string property
    # is a valid key
    is_valid_key = text_field in data.keys()

    # determine whether or not the piece of data is using a fake user
    has_fake_user = is_valid_key and data[text_field].use_fake_user

    # buttons that follow the prop search
    split = row.split()
    row = split.row(align=True)

    # disable the buttons if the key in the search property is invalid
    row.enabled = is_valid_key

    # toggle fake user button (do not show for collections)
    # icon and depression changes depending on whether or not the object
    # is using a fake user
    if data != bpy.data.collections:

        # has fake user
        if has_fake_user:
            row.operator(
                "atomic.toggle_fake_user",
                text="",
                icon="FAKE_USER_ON",
                depress=True
            )

        # does not have fake user
        else:
            row.operator(
                "atomic.toggle_fake_user",
                text="",
                icon="FAKE_USER_OFF",
                depress=False
            )

    # duplicate button
    row.operator(
        "atomic.inspection_duplicate",
        text="",
        icon="DUPLICATE"
    )

    # replace button (do not show for collections)
    if data != bpy.data.collections:
        row.operator(
            "atomic.replace",
            text="",
            icon="UV_SYNC_SELECT"
        )

    # rename button
    row.operator(
        "atomic.rename",
        text="",
        icon="GREASEPENCIL"
    )

    # delete button
    row.operator(
        "atomic.inspection_delete",
        text="",
        icon="TRASH"
    )


def number_suffix(text, number):
    # returns the text properly formatted as a suffix
    # e.g. passing in "hello" and "100" will result in "hello (100)"

    return text + " ({0})".format(number) if int(number) != 0 else text
