# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Assignment1_Cogar'
copyright = '2025, Bertelli Buono Tinfena'
author = 'Roberto Bertelli, Chiara Buono, Mattia Tinfena'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []
master_doc = 'index'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']


html_show_sourcelink = False

html_context = {
    "display_github": True,
    #"github_user": "AleBulanti",
    "github_repo": "git@github.com:chiarabuono/Assignment1_Cogar.git",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}