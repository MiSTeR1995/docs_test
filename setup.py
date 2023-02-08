import sys

from setuptools import setup, find_packages

MIN_PYTHON_VERSION = (3, 8)

if sys.version_info[:2] < MIN_PYTHON_VERSION:
    raise RuntimeError('Python version required = {}.{}'.format(MIN_PYTHON_VERSION[0], MIN_PYTHON_VERSION[1]))

import test_docs_python

REQUIRED_PACKAGES = [
    'colorama >= 0.4.6',
    'prettytable >= 3.5.0',
    'numpy >= 1.24.0',
    'pandas >= 1.5.2'
]

CLASSIFIERS = """\
Development Status :: 3 - Alpha
Natural Language :: Russian
Natural Language :: English
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: End Users/Desktop
Intended Audience :: Science/Research
Intended Audience :: Information Technology
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: Implementation :: CPython
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Mathematics
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Scientific/Engineering :: Image Processing
Topic :: Scientific/Engineering :: Image Recognition
Topic :: Software Development
Topic :: Software Development :: Libraries
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Documentation
Topic :: Documentation :: Sphinx
Topic :: Multimedia :: Sound/Audio
Topic :: Multimedia :: Sound/Audio :: Analysis
Topic :: Multimedia :: Sound/Audio :: Speech
Topic :: Software Development :: Libraries
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Localization
Topic :: Utilities
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: POSIX :: Linux
Framework :: Jupyter
Framework :: Jupyter :: JupyterLab :: 4
Framework :: Sphinx
"""
with open('README.md', 'r') as fh:
    long_description = fh.read()

    setup(
        name = test_docs_python.__name__,
        packages = find_packages(),
        license = test_docs_python.__license__,
        version = test_docs_python.__release__,
        author = test_docs_python.__author__en__,
        author_email = test_docs_python.__email__,
        maintainer = test_docs_python.__maintainer__en__,
        maintainer_email = test_docs_python.__maintainer_email__,
        url = test_docs_python.__uri__,
        description = test_docs_python.__summary__,
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        install_requires=REQUIRED_PACKAGES,
        keywords = [
            'TestDocs', 'Documentation'
        ],
        include_package_data = True,
        classifiers = [_f for _f in CLASSIFIERS.split('\n') if _f],
        python_requires = '>=3.8, <4',
        entry_points = {
            'console_scripts': [],
        },
        project_urls = {
            'Bug Reports': 'https://github.com/MiSTeR1995/docs_test/issues',
            'Documentation': 'https://test-docs-python.readthedocs.io',
            'Source Code': 'https://github.com/MiSTeR1995/docs_test/tree/master/test_docs_python',
            'Download': 'https://github.com/MiSTeR1995/docs_test/tags',
        },
    )
