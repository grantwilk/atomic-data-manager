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

This file contains global copies of Atomic's preferences so that they
can be easily access throughout the add-on.

NOTE:
Changing the values of these variables will NOT change the values in the
Atomic's preferences. If you want to change a setting, change it in
Blender, not in here.

"""

# visible atomic preferences
enable_missing_file_warning = True
enable_support_me_popup = True
ignore_fake_users = False
enable_pie_menu_ui = True

# hidden atomic preferences
pie_menu_type = "D"
pie_menu_alt = False
pie_menu_any = False
pie_menu_ctrl = False
pie_menu_oskey = False
pie_menu_shift = False
last_popup_day = 0