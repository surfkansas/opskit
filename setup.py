from distutils.core import setup
setup(
  name = 'opskit',
  py_modules = ['opskit'],
  packages = ['opskit'], 
  entry_points = {
    'console_scripts': ['opskit=opskit:main'],
  },
  version = '0.8.108.3',
  author = 'Mark Sweat',
  author_email = 'mark@surfkansas.com',
  url = 'https://github.com/surfkansas/opskit', 
  download_url = 'https://github.com/surfkansas/opskit/archive/0.8.108.3.tar.gz'
)
