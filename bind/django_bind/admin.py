# -*- coding: utf-8 -*-
#
# This file is part of django-bind (https://github.com/mathiasertl/django-bind).
#
# django-bind is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# django-bind is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with django-bind.  If not,
# see <http://www.gnu.org/licenses/>.


from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import Macro
from .models import View
from .models import Zone


@admin.register(Macro)
class MacroAdmin(VersionAdmin):
    pass


@admin.register(View)
class ViewAdmin(VersionAdmin):
    pass


@admin.register(Zone)
class ZoneAdmin(VersionAdmin):
    pass
