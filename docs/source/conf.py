# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------
import sphinx_bootstrap_theme
import matplotlib as mpl
mpl.use("Agg")

# Include the example source for plots in API docs
plot_include_source = True
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = True

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'cjlovering'
copyright = u'2018, Charles J. Lovering'
author = u'Charles J. Lovering'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'0.0'


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    'matplotlib.sphinxext.plot_directive',
    'nbsphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = ['.rst', '.ipynb']

# The master toctree document.
master_doc = 'index'

# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'
html_theme_options = {
    'source_link_position': "footer",
    'bootswatch_theme': "paper",
    'navbar_sidebarrel': False,
    'bootstrap_version': "3",
    'navbar_links': [],
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_scaled_image_link = False
html_favicon = '_static/favicon.ico'
html_js_files = [ "https://d3js.org/d3.v5.min.js" ]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'medoc'

def setup(app):
  app.add_stylesheet('style.css')

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True