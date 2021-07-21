# -*- coding: utf-8 -*-
#
# Object oriented programming course documentation build configuration file,
# created by sphinx-quickstart on Sat Sep  6 21:48:49 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinxcontrib.youtube',
    'sphinx.ext.viewcode',
    'sphinxcontrib.proof',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx.ext.graphviz',
    'sphinxcontrib.blockdiag',
    'sphinx.ext.napoleon',
    'sphinx_panels',
    'sphinxcontrib.details.directive'
]
# Both the class’ and the __init__ method’s docstring are concatenated and
# inserted into the class definition
autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Object oriented programming'
author = u'David A. Ham'
copyright = u'2019-2021, David A. Ham'

mathjax_path = \
    "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" # noqa 501

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2021.0'
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "py:obj"

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


proof_theorem_types = {
    "algorithm": "Algorithm",
    "conjecture": "Conjecture",
    "corollary": "Corollary",
    "definition": "Definition",
    "example": "Example",
    "lemma": "Lemma",
    "observation": "Observation",
    "proof": "Proof",
    "property": "Property",
    "theorem": "Theorem",
    "exercise": "Exercise",
}

proof_latex_parent = "chapter"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'finite_element'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Finiteelementcoursedoc'

# -- GraphViz configuration -----------------------------------------------
graphviz_output_format = 'svg'

# Fontpath for blockdiag (truetype font)
blockdiag_fontpath = '/Users/dham/Library/Fonts/Carlito-Regular.ttf'
blockdiag_html_image_format = 'svg'
blockdiag_latex_image_format = 'pdf'

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'lualatex'

latex_use_xindy = False

latex_additional_files = [
    '_themes/finite_element/static/dialog-right.png',
    '_themes/finite_element/static/dialog-wrong.png',
    '_static/imperialmathnotes.sty',
    'images/Imperial.pdf'
]

if tags.has("book"):
    preamble = ""
else:
    # Imperial lecture notes version.
    preamble = r"""
\usepackage{imperialmathnotes}
\subtitle{in Python for mathematicians}
\imperialmathnotesvolume{2}
\edition{2021}
"""

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    'babel': r'\usepackage[british]{babel}',

    # Additional stuff for the LaTeX preamble.
    'preamble': preamble + r'''\setcounter{MaxMatrixCols}{20}
\newcommand{\currentsummary}{}
\newcommand{\sphinxdetailssummary}[1]{
    \renewcommand{\currentsummary}{#1}}
\newcommand{\sphinxcontribvimeo}[2]{%
\protect\href{#1#2}{\currentsummary}}
\usepackage{etoolbox}
\usepackage{pifont}
\newcommand{\cmark}{\ding{51}}%
\newcommand{\xmark}{\ding{55}}%
\newcommand{\currentsphinxclass}{}
\usepackage{calc}
\newlength{\badcodesize}
\renewenvironment{sphinxuseclass}[1]{
    \setlength{\badcodesize}{\linewidth-.05\textwidth}
    \renewcommand{\currentsphinxclass}{#1} % Note not safe for nested containers.
    \ifstrequal{#1}{badcode}{\begin{minipage}{\badcodesize}}{}
    \ifstrequal{#1}{goodcode}{\begin{minipage}{\badcodesize}}{}
}{
    \ifdefstring{\currentsphinxclass}{badcode}{\end{minipage}
    \begin{minipage}{.045\textwidth}{\Huge\color{red}\ \xmark}\end{minipage}
    
    }{}
    \ifdefstring{\currentsphinxclass}{goodcode}{\end{minipage}\ 
    \begin{minipage}{.045\textwidth}{\Huge\color{green}\ \cmark}\end{minipage}
    
    }{}
    \renewcommand{\currentsphinxclass}{}
}
''',
    'releasename': '',
    'sphinxsetup': 'VerbatimColor={HTML}{FAFAFA}, \
        VerbatimBorderColor={HTML}{c6c9cb}, \
        InnerLinkColor={HTML}{c52b03}, \
        OuterLinkColor={HTML}{e55d05}, \
        noteBorderColor={HTML}{7a9eec}, \
        hintBorderColor={HTML}{7a9eec}, \
        warningBorderColor={HTML}{fbc2c4}, \
        warningBgColor={HTML}{fbe3e4}, \
        TitleColor={cmyk}{1,.61,0,.45}'
}

if tags.has("book"):
    latex_elements['geometry'] = r'\usepackage[papersize={189mm,246.1mm}]{geometry}'
    latex_elements['sphinxsetup'] += ',hmargin={1.5cm,1.5cm},vmargin={2cm,2cm}'
else:
    latex_elements['maketitle'] = r'\imperialmathnotestitlepages'


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#  ('index', 'Finiteelementcourse.tex',
#   u'M345A47 Finite Elements: Analysis and Implementation',
#   u'David A. Ham and Colin J. Cotter', 'manual'),
# ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False
latex_toplevel_sectioning = "chapter"

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True
latex_docclass = {"manual": "book"}


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#    ('index', 'finiteelementcourse', u'Finite element course Documentation',
#     [u'David A. Ham and Colin J. Cotter'], 1)
# ]

# If true, show URL addresses after external links.
# man_show_urls = False


numfig = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'scipy': ('https://scipy.github.io/devdocs/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'setuptools': ('https://setuptools.readthedocs.io/en/latest/', None),
    'pip': ('https://pip.pypa.io/en/stable/', None),
    'sympy': ('https://docs.sympy.org/latest', None),
    'pytest': ('https://docs.pytest.org/en/latest/', None),
    'fons': ('https://imperial-fons-computing.github.io', None),
    'pandas': ('https://pandas.pydata.org/docs/', None)
}
