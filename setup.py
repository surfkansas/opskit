from distutils.core import setup
setup(
  name = 'opskit',
  py_modules = ['opskit'],
  packages = ['opskit'], 
  entry_points = {
    'console_scripts': ['opskit=opskitcl:main'],
  },
  version = '0.8.108.4',
  author = 'Mark Sweat',
  author_email = 'mark@surfkansas.com',
  url = 'https://github.com/surfkansas/opskit', 
  download_url = 'https://github.com/surfkansas/opskit/archive/0.8.108.4.tar.gz'
)
