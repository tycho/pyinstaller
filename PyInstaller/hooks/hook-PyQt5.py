#-----------------------------------------------------------------------------
# Copyright (c) 2005-2017, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
import os

from PyInstaller.utils.hooks import collect_data_files

# Collect just the ``qt.conf`` file.
datas = [x for x in collect_data_files('PyQt5', False, os.path.join('Qt')) if
         os.path.basename(x[0]) == 'qt.conf']
