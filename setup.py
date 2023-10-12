from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tech_venture_uniherb/__init__.py
from tech_venture_uniherb import __version__ as version

setup(
	name="tech_venture_uniherb",
	version=version,
	description="this is tech venture uniherb",
	author="Tech Venture",
	author_email="safdar211@gamil.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
