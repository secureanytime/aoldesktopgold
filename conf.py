project = 'communities-anywhere'
copyright = '2026'
author = 'Admin'

extensions = [ 'sphinx.ext.autodoc',
               'sphinx.ext.napoleon',
               'sphinx_sitemap',
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Screenshot wala classic white theme

html_baseurl = 'https://communities-anytime-aoldesktopgold.readthedocs-hosted.com/en/latest/'
sitemap_url_scheme = "{link}"

# conf.py

html_title = "Download AOL desktop gold"
html_short_title = "Download AOL desktop gold"
html_static_path = ['_static']
html_extra_path = ['_static/google5ffeff63dcb91d99.html'] 


# Meta Tags Configuration
html_context = {
    'metatags': '''
        <meta name="description" content="To Download AOL Desktop Gold, sign in to your AOL account at aol.com, open your account or subscription page, select Desktop Gold, and save the installer">
        <meta name="Download AOL Desktop Gold" content="docs, guide, setup, tutorial">
     
    '''
}
