from distutils.core import setup
import setuptools

setup(
    name='Glossary',
    version='0.2',
    description='A multilingual glossary.',
    author='Greg Wilson',
    author_email='greg.wilson@rstudio.com',
    url='https://github.com/gvwilson/glossary',
    license='CC-BY',
    packages=setuptools.find_packages(),
    package_data={'glossary': ['glossary.yml']}
)
