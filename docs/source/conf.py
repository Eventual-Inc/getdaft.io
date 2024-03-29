# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "getdaft.io"
copyright = "2023, Eventual"
author = "Eventual"
# html_logo = "_static/daft-logo.png"
html_favicon = "_static/daft-favicon.png"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]

# Adds /_html folder which serves robots.txt and the sitemap
html_extra_path = ["_html"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["styles.css"]
html_sidebars = {
    "**": []
}
html_context = {"default_mode": "light"}
