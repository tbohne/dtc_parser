from setuptools import find_packages, setup

__version__ = '0.0.1'
URL = 'https://github.com/tbohne/dtc_parser'

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='dtc_parser',
    version=__version__,
    description='Parser for diagnostic trouble codes (DTCs) used by vehicle onboard diagnosis (OBD).',
    author='Tim Bohne',
    author_email='tim.bohne@dfki.de',
    url=URL,
    download_url=f'{URL}/archive/{__version__}.tar.gz',
    keywords=[
        'parser',
        'DTC',
        'OBD'
    ],
    python_requires='>=3.7, <3.11',
    install_requires=required,
    packages=find_packages(),
    include_package_data=True,
)
