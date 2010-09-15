#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento API

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPLv3, see LICENSE for more details
'''
from setuptools import Command, setup
import magento

class run_audit(Command):
    """
    Audits source code using PyFlakes for following issues:
    - Names which are used but not defined or used before they are defined.
    - Names which are redefined without having been used.
    """
    description = "Audit source code with PyFlakes"
    user_options = []

    def initialize_options(self):
        all = None

    def finalize_options(self):
        pass

    def run(self):
        import os, sys
        try:
            import pyflakes.scripts.pyflakes as flakes
        except ImportError:
            print "Audit requires PyFlakes installed in your system."""
            sys.exit(-1)

        dirs = ['fedex', 'tests']
        # Add example directories
        #dirs.append(os.path.join('examples', dir))
        warns = 0
        for dir in dirs:
            for filename in os.listdir(dir):
                if filename.endswith('.py') and filename != '__init__.py':
                    warns += flakes.checkPath(os.path.join(dir, filename))
        if warns > 0:
            print ("Audit finished with total %d warnings." % warns)
        else:
            print ("No problems found in sourcecode.")


setup(
    name = 'magento',
    version=magento.__version__,
    url='http://openlabs.co.in/projects/python/magento',
    license='GPL',
    author='Sharoon Thomas, Openlabs Technologies',
    author_email='info@openlabs.co.in',
    description='Magento E-Commerce Integration',
    long_description=__doc__,
    packages=['magento'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'suds>=0.3.9',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={'audit': run_audit},
    #test_suite='__main__.run_tests'
)

