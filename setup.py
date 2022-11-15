"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.522
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wallet"
VERSION = "2.1.522"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="wallet-api",
    author="Development Team",
    author_email="development@wallet.inc",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "wallet-api"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="https://wallet.law",
    long_description="""\
    API  # noqa: E501
    """
)
