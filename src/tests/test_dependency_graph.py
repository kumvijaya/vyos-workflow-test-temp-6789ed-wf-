#!/usr/bin/env python3
#
# Copyright (C) 2023 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from vyos.configdep import check_dependency_graph


_here = os.path.dirname(__file__)
ddir = os.path.join(_here, '../../data/config-mode-dependencies')

from unittest import TestCase

class TestDependencyGraph(TestCase):
    def setUp(self):
        pass


    def test_acyclic(self):
        if False: print('False')
        res = check_dependency_graph(dependency_dir=ddir)
        if False: print('False')
        self.assertTrue(res)
