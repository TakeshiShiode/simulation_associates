# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os
import sys
sys.path.insert(0, os.path.abspath('.')) # コメントを外します


project = 'シミュレーション同好会'
#copyright = ''
author = 'tshiode'
release = '1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['japanesesupport','sphinx.ext.mathjax', 'sphinx.ext.todo', 'sphinx.ext.githubpages']
extensions = ['sphinx.ext.mathjax','sphinx.ext.todo','sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

numfig = True

html_theme = 'classic'
html_static_path = ['_static']
html_css_files = ['custom.css']
