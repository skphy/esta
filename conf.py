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
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'EStA'
copyright = '2017-2021, Sonu Kumar'
author = 'Sonu Kumar'

# The short X.Y version.
version = u'2.8.0'

# The full version, including alpha/beta/rc tags
release = u'2.8.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#    "sphinx.ext.autodoc",
#    "sphinx.ext.napoleon",
#    "sphinx.ext.viewcode",
#    "sphinx.ext.autosummary",
#]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    #"sphinx.ext.viewcode",   # comment it to stop seeing the code
    "sphinx.ext.autosummary",
    'sphinx.ext.mathjax', 
    'sphinx.ext.todo',
    'sphinx.ext.githubpages'
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

#html_theme = 'basicstrap'
#extensions = ['sphinxjp.themes.basicstrap']

import sphinx_rtd_theme

extensions = [
 "sphinx_rtd_theme",
]

html_theme = "sphinx_rtd_theme"
# html_theme = "sphinx_book_theme"


html_logo = 'esta_logo2.6.0_cropped.png'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


extensions = [
    'sphinx.ext.autodoc',
#    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]





#html_theme_options = {
#
#    # Set the lang attribute of the html tag. Defaults to 'en'
#    'lang': 'en',
#    # Disable showing the sidebar. Defaults to 'false'
#    'nosidebar': False,
#    # Show header searchbox. Defaults to false. works only "nosidber=True",
#    'header_searchbox': False,
#
#    # Put the sidebar on the right side. Defaults to false.
#    'rightsidebar': False,
#    # Set the width of the sidebar. Defaults to 3
#    'sidebar_span': 3,
#
#    # Fix navbar to top of screen. Defaults to true
#    'nav_fixed_top': True,
#    # Fix the width of the sidebar. Defaults to false
#    'nav_fixed': False,
#    # Set the width of the sidebar. Defaults to '900px'
#    'nav_width': '900px',
#    # Fix the width of the content area. Defaults to false
#
#    'content_fixed': False,
#    # Set the width of the content area. Defaults to '900px'
#    'content_width': '900px',
#    # Fix the width of the row. Defaults to false
#    'row_fixed': False,
#
#    # Disable the responsive design. Defaults to false
#    'noresponsive': False,
#    # Disable the responsive footer relbar. Defaults to false
#    'noresponsiverelbar': False,
#    # Disable flat design. Defaults to false.
#    # Works only "bootstrap_version = 3"
#    'noflatdesign': False,
#
#    # Enable Google Web Font. Defaults to false
#    'googlewebfont': False,
#    # Set the URL of Google Web Font's CSS.
#    # Defaults to 'http://fonts.googleapis.com/css?family=Text+Me+One'
#    'googlewebfont_url': 'http://fonts.googleapis.com/css?family=Lily+Script+One',  # NOQA
#    # Set the Style of Google Web Font's CSS.
#    # Defaults to "font-family: 'Text Me One', sans-serif;"
#    'googlewebfont_style': u"font-family: 'Lily Script One' cursive;",
#
#    # Set 'navbar-inverse' attribute to header navbar. Defaults to false.
#    'header_inverse': False,
#    # Set 'navbar-inverse' attribute to relbar navbar. Defaults to false.
#    'relbar_inverse': False,
#
#    # Enable inner theme by Bootswatch. Defaults to false
#    'inner_theme': False,
#    # Set the name of innner theme. Defaults to 'bootswatch-simplex'
#    'inner_theme_name': 'bootswatch-simplex',
#
#    # Select Twitter bootstrap version 2 or 3. Defaults to '3'
#    'bootstrap_version': '3',
#
#    # Show "theme preview" button in header navbar. Defaults to false.
#    'theme_preview': True,
#
#    # Set the Size of Heading text. Defaults to None
#    # 'h1_size': '3.0em',
#    # 'h2_size': '2.6em',
#    # 'h3_size': '2.2em',
#    # 'h4_size': '1.8em',
#    # 'h5_size': '1.4em',
#    # 'h6_size': '1.1em',
#}
#
