####################################################################################################
#
# pyglfw-cffi - A Python Wrapper for GLFW.
# Copyright (C) 2014 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

####################################################################################################

import os

####################################################################################################

def merge_include(src_lines, doc_path, included_rst_files=None):
    if included_rst_files is None:
        included_rst_files = {}
    text = ''
    for line in src_lines:
        if line.startswith('.. include::'):
            include_file_name = line.split('::')[-1].strip()
            if include_file_name not in included_rst_files:
                # print "include", include_file_name
                with open(os.path.join(doc_path, include_file_name)) as f:
                    included_rst_files[include_file_name] = True
                    text += merge_include(f.readlines(), doc_path, included_rst_files)
        else:
            text += line
    return text

####################################################################################################

# Utility function to read the README file.
# Used for the long_description.
def read(file_name):

    source_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.basename(source_path) == 'tools':
        source_path = os.path.dirname(source_path)
    elif 'build/bdist' in source_path:
        source_path = source_path[:source_path.find('build/bdist')]
    absolut_file_name = os.path.join(source_path, file_name)
    doc_path = os.path.join(source_path, 'doc', 'source')

    # Read and merge includes
    with open(absolut_file_name) as f:
        lines = f.readlines()
    text = merge_include(lines, doc_path)

    return text

####################################################################################################

long_description = read('README.txt')

####################################################################################################

setup_dict = dict(
    name='pyglfw-cffi',
    version='0.1.1',
    author='Fabrice Salvaire',
    author_email='fabrice.salvaire@orange.fr',
    # description='A Python wrapper for GLFW based on CFFI',
    description='A CFFI-based wrapper for GLFW3',
    license="GPLv3",
    keywords="GLFW, CFFI",
    url='http://fabricesalvaire.github.io/pyglfw-cffi',
    scripts=['simple-test.py'],
    packages=['PyGlfwCffi',
    ],
    package_data={},
    long_description=long_description,
    # cf. http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Education",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        ],
    requires=[
        'cffi',
    ]
    )

####################################################################################################
#
# End
#
####################################################################################################
