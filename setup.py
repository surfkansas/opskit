from distutils.core import setup
setup(
  name = 'opskit',
  py_modules = ['opskit-cl'],
  packages = ['opskit'], 
  entry_points = {
    'console_scripts': ['opskit=opskit-cl:main'],
  },
  version = '0.9.108',
  author = 'Mark Sweat',
  author_email = 'mark@surfkansas.com',
  url = 'https://github.com/surfkansas/opskit', 
  download_url = 'https://github.com/surfkansas/opskit/archive/0.9.108.tar.gz'
)
