from __future__ import unicode_literals

__all__ = ['site_title', 'root_dir', 'general_info', 'static_dir', 'run_per_page', 'logo_filename', 'github_url', 'months_to_search']

root_dir = '/global/project/projectdirs/desi/www/users/desiqa/run'
site_title = 'DESIQA: DESI Quality Assurance for Mock Galaxy Catalogs'

run_per_page = 20
months_to_search = 3

static_dir = 'web-static'
logo_filename = 'NewDM_SpectroScopic_logo.jpg'
github_url = 'https://github.com/lsstdesc/descqa'

general_info = '''
This is DESIQA, a fork of the DESCQA framework, which executes validation tests on mock galaxy catalogs.
These tests and catalogs are contributed by DESI collaborators.
See <a href="https://arxiv.org/abs/1709.09665" target="_blank">the DESCQA paper</a> for more information about the original DESCQA framework.
The source code of DESCQA is hosted in <a href="https://github.com/LSSTDESC/descqa/" target="_blank">this GitHub repo</a>.
'''
