.. -*- Mode: rst -*-

.. -*- Mode: rst -*-

.. |ohloh| image:: https://www.openhub.net/accounts/230426/widgets/account_tiny.gif
   :target: https://www.openhub.net/accounts/fabricesalvaire
   :alt: Fabrice Salvaire's Ohloh profile
   :height: 15px
   :width:  80px

.. |pyglfw-cffi-Url| replace:: http://fabricesalvaire.github.io/pyglfw-cffi

.. |pyglfw-cffi-HomePage| replace:: pyglfw-cffi Home Page
.. _pyglfw-cffi-HomePage: http://fabricesalvaire.github.io/pyglfw-cffi

.. |pyglfw-cffi-Doc| replace:: pyglfw-cffi Documentation
.. _pyglfw-cffi-Doc: http://glfw-cffi.readthedocs.org/en/latest

.. |pyglfw-cffi@readthedocs-badge| image:: https://readthedocs.org/projects/glfw-cffi/badge/?version=latest
   :target: http://glfw-cffi.readthedocs.org/en/latest

.. |pyglfw-cffi@github| replace:: https://github.com/FabriceSalvaire/pyglfw-cffi
.. .. _pyglfw-cffi@github: https://github.com/FabriceSalvaire/pyglfw-cffi

.. |pyglfw-cffi@readthedocs| replace:: http://glfw-cffi.readthedocs.org
.. .. _pyglfw-cffi@readthedocs: http://glfw-cffi.readthedocs.org

.. |pyglfw-cffi@pypi| replace:: https://pypi.python.org/pypi/pyglfw-cffi
.. .. _pyglfw-cffi@pypi: https://pypi.python.org/pypi/pyglfw-cffi

.. |Build Status| image:: https://travis-ci.org/FabriceSalvaire/pyglfw-cffi.svg?branch=master
   :target: https://travis-ci.org/FabriceSalvaire/glfw-cffi
   :alt: pyglfw-cffi build status @travis-ci.org

.. |Pypi Download| image:: https://img.shields.io/pypi/dm/pyglfw-cffi.svg
   :target: https://pypi.python.org/pypi/pyglfw-cffi
   :alt: pyglfw-cffi Download per month

.. |Pypi Version| image:: https://img.shields.io/pypi/v/pyglfw-cffi.svg
   :target: https://pypi.python.org/pypi/pyglfw-cffi
   :alt: pyglfw-cffi last version

.. |Pypi License| image:: https://img.shields.io/pypi/l/pyglfw-cffi.svg
   :target: https://pypi.python.org/pypi/pyglfw-cffi
   :alt: pyglfw-cffi license

.. |Pypi Format| image:: https://img.shields.io/pypi/format/pyglfw-cffi.svg
   :target: https://pypi.python.org/pypi/pyglfw-cffi
   :alt: pyglfw-cffi format

.. |Pypi Python Version| image:: https://img.shields.io/pypi/pyversions/pyglfw-cffi.svg
   :target: https://pypi.python.org/pypi/pyglfw-cffi
   :alt: pyglfw-cffi python version

.. End
.. -*- Mode: rst -*-

.. |Python| replace:: Python
.. _Python: http://python.org

.. |PyPI| replace:: PyPI
.. _PyPI: https://pypi.python.org/pypi

.. |Sphinx| replace:: Sphinx
.. _Sphinx: http://sphinx-doc.org

.. |CFFI| replace:: CFFI
.. _CFFI: http://cffi.readthedocs.org

.. |OpenGL| replace:: OpenGL
.. _OpenGL: http://www.opengl.org

.. |pypy| replace:: pypy
.. _pypy: http://pypy.org

.. |GLFW| replace:: GLFW
.. _GLFW: http://www.glfw.org

.. End

=============
 pyglfw-cffi
=============

.. The official GlfwCffi Home Page is located at |pyglfw-cffi-URL|

.. The latest documentation build from the git repository is available at readthedocs.org |pyglfw-cffi@readthedocs-badge|

Written by `Fabrice Salvaire <http://fabrice-salvaire.pagesperso-orange.fr>`_.

.. |Build Status|

|Pypi License|
|Pypi Python Version|

|Pypi Version|
|Pypi Format|
|Pypi Download|

-----

.. -*- Mode: rst -*-

This Python package provides a CFFI wrapper for the |GLFW| library.

GLFW is an Open Source, multi-platform library for creating windows with OpenGL contexts and
receiving input and events.

Look the file *simple-test.py* to learn how to use the wrapper.

.. End
.. -*- Mode: rst -*-

.. _installation-page:

==============
 Installation
==============

Dependencies
------------

pyglfw-cffi requires the following dependencies:

 * |Python|_ 2.7
 * |CFFI|_ 0.8.6
 * |GLFW|_ 3

Installation from PyPi Repository
---------------------------------

pyglfw-cffi is made available on the |Pypi|_ repository at |pyglfw-cffi@pypi|

Run this command to install the last release:

.. code-block:: sh

  pip install pyglfw-cffi

Installation from Source
------------------------

The pyglfw-cffi source code is hosted at |pyglfw-cffi@github|

To clone the Git repository, run this command in a terminal:

.. code-block:: sh

  git clone git@github.com:FabriceSalvaire/pyglfw-cffi.git

Then to build and install pyglfw-cffi run these commands:

.. code-block:: sh

  python setup.py build
  python setup.py install

.. End
.. -*- Mode: rst -*-

=========
 Testing
=========

To test the wrapper run this script:

.. code-block:: sh

  python simple-test.py

.. end

.. End
