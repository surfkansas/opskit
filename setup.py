from distutils.core import setup
setup(
  name = 'opskit',
  py_modules=['opskit'],
  packages = ['opskit'], 
  package_data={'': '*.txt'},
  entry_points = {
    'console_scripts': ['opskit=opstkit:main'],
  },
  version = '0.8.108',
  author = 'Mark Sweat',
  author_email = 'mark@surfkansas.com'
)
