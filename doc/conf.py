# -*- coding: utf-8 -*-


from builder.shared_conf import * # noqa

##############################################################
# start of things to edit

project = u'ParamBokeh'
authors = u'ParamBokeh contributors'
copyright = u'2017 ' + authors

# TODO: rename
ioam_module = 'parabokeh'
description = 'Generate bokeh widgets for parameterized objects'

# TODO: gah, version
version = '0.0.1'
release = '0.0.1'

html_static_path = ['_static']

html_theme = 'ioam_theme'
html_theme_options = {
#    'logo':'images/amazinglogo.png'
#    'favicon':'images/amazingfavicon.ico'
# ...
# ? css
# ? js
}


_NAV =  (
        ('Getting Started', '/getting_started/index'),
        ('User Guide', '/user_guide/index'),
#        ('Gallery', '/gallery/index'),
#        ('API', '/Reference_Manual/index'),
#        ('FAQ', '/FAQ'),
        ('About', '/about'))

_LINKS = (
        ('Getting Started', '/getting_started/index'),
        ('User Guide', '/user_guide/index'),
#        ('Gallery', '/gallery/index'),
#        ('API', '/Reference_Manual/index'),
#        ('FAQ', '/FAQ'),
        ('About', '/about'))

html_context = {
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # will work without this - for canonical
    'WEBSITE_SERVER': 'ioam.github.io/parambokeh',
    'VERSION': version,
    'NAV': _NAV,
    'LINKS': _LINKS,
    'SOCIAL': (
        ('Gitter', '//gitter.im/ioam/holoviews'),
        ('Twitter', '//twitter.com/holoviews'),
        ('Github', '//github.com/ioam/parambokeh'),
    ),
    'js_includes': ['custom.js', 'require.js'],
}

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here.
paths = ['.', '..']

# end of things to edit
##############################################################


add_paths(paths)

from builder.shared_conf2 import hack
setup, intersphinx_mapping, texinfo_documents, man_pages, latex_documents, htmlhelp_basename, html_static_path, html_title, exclude_patterns = hack(project,ioam_module,authors,description,html_static_path)

intersphinx_mapping = {}
