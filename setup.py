import os
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec
from setuptools import setup, find_packages

dirname = os.path.dirname(__file__)
path_version = os.path.join(dirname, "dice_throne_probability_calculator", "_version.py")
loader = SourceFileLoader('_version', path_version)
spec = spec_from_loader(loader.name, loader)
version = module_from_spec(spec)
loader.exec_module(version)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dice_throne_probability_calculator',
    version=version.__version__,
    packages= find_packages(),
    url='',
    license='',
    author='Panagiotis Zogas',
    author_email='panoszogas2@gmail.com',
    description='',
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires='>=3.10',
    # install_requires=[
    #     'numpy>=1.24.4,<=1.26.1',
    #     'pandas>=2.0.3,<=2.1.1',
    #     'python-dateutil>=2.8.2,<=2.8.2',
    #     'pytz>=2023.3.post1,<=2023.3.post1',
    #     'six>=1.16.0,<=1.16.0',
    #     'tzdata>=2023.3,<=2023.3',
    # ]
)
