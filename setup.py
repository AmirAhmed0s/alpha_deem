from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alpha_deem/__init__.py
from alpha_deem import __version__ as version

setup(
	name="alpha_deem",
	version=version,
	description="smart",
	author="smart solution",
	author_email="info@smartsoleg.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
