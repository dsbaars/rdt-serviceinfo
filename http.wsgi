#!/usr/bin/env python

"""
IFF/ARNU HTTP interface
Copyright (C) 2015 Geert Wirken

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import bottle

import serviceinfo.common
import serviceinfo.http

# Load configuration:
serviceinfo.common.load_config(sys.argv[1])
serviceinfo.common.setup_logging('http-wsgi')

application = bottle.default_app()
