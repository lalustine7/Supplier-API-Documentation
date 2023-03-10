# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Supplier API Documentation'
copyright = '2023, Lal Kumar Rai'
author = 'Lal Kumar Rai'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx-prompt",
    "sphinx_tabs.tabs",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.httpexample"
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    "pip": ("https://pip.pypa.io/en/stable/", None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

httpexample_scheme = 'https'