import setuptools
from setuptools import find_packages

setuptools.setup(
    name='geoscan',
    version='1.0',
    author='Antoine Amend',
    author_email='antoine.amend@databricks.com',
    description='Geoclustering using H3 hexagons',
    long_description_content_type='text/markdown',
    url='https://github.com/aamend/geoscan',
    packages=find_packages(where=".", include=["geoscan"]),
    extras_require=dict(tests=["pytest"]),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Databricks License',
        'Operating System :: OS Independent',
    ],
)