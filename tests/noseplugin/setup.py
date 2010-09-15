import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='magentonose',
    version='0.1',
    author='Sharoon Thomas',
    author_email = 'sharoon.thomas@openlabs.co.in',
    description = 'Magento Nose Testing Plugin',
    license = 'GNU LGPL',
    py_modules = ['magentonose'],
    entry_points = {
        'nose.plugins.0.10': [
            'magentonose = magentonose:MagentoNose'
            ]
        }

    )

