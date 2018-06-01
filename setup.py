from __future__ import with_statement

import setuptools

requires = [
    "flake8 > 3.0.0",
]

readme = open('README.rst').read()

setuptools.setup(
    name="flake8_csv",
    license="MIT",
    use_scm_version=True,
    description="CSV reporting formatter plugin for Flake8",
    long_description=readme,
    author="Ben Lopatin",
    author_email="ben@benlopatin.com",
    url="https://github.com/bennylope/flake8-csv",
    py_modules=['flake8_csv'],
        setup_requires=[
        'setuptools_scm',
    ],
    install_requires=requires,
    entry_points={
        'flake8.report': [
            'csv = flake8_csv:CSVFormatter',
            'csv_categories = flake8_csv:CategorizedCSVFormatter',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
