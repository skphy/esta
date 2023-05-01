# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme  #26/7/22
#import sphinx_book_theme  #26/7/22
#import pydata_sphinx_theme

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'EStA'
copyright = '2017-2023, Sonu Kumar'
author = 'Sonu Kumar'

# The full version, including alpha/beta/rc tags
release = '2.9.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

#html_theme = 'alabaster'
#html_theme = "sphinx_rtd_theme" #26/7/22  # pip install sphinx-rtd-theme
html_theme = "sphinx_book_theme" #26/7/22 --- # pip install sphinx-book-theme
#html_theme="pyramid"
#location  /home/om/anaconda3/envs/py39/lib/python3.9/site-packages/sphinx_book_theme/theme/sphinx_book_theme
#html_theme_path = ["/home/om/anaconda3/envs/py39/lib/python3.9/site-packages/sphinx_book_theme/theme/sphinx_book_theme"]
#html_theme_path = sphinxtheme.get_html_theme_path()

#html_theme = "sphinx-book-theme" # this is installed through conda
#html_theme = 'python_docs_theme'


#html_theme = "pydata_sphinx_theme"
#html_theme_path ="/home/om/anaconda3/envs/py39/lib/python3.9/site-packages/pydata_sphinx_theme/theme/pydata_sphinx_theme"


#import sphinx_rtd_theme
#extensions = ['sphinx_rtd_theme',]
#html_theme = "sphinx_rtd_theme"



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


#extensions = [
#    'sphinx.ext.autodoc',
#    #'sphinx.ext.viewcode'
#    #'python_docs_theme'
#]


