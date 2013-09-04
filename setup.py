from setuptools import setup

# TODO: check for a ~/.nomad and create/modify as needed

setup(name='nomad',
      # TODO: check for additional meta-data to add here, following from:
      #       http://docs.python.org/2/distutils/setupscript.html#additional-meta-data
      version='0.1',
      description='Routines for accessing a self-hosted local copy of the USNO NOMAD catalog',
      author='Henry Roe',
      author_email='hroe@hroe.me',
      url='TODO',
      py_modules=['nomad'],
      install_requires=['pandas>=0.10.1'])
