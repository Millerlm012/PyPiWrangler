from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'PyPi Wrangler is a tool to assist in the packaging of python dependencies..'
LONG_DESCRIPTION = 'PyPi Wrangler is a tool to assist in the packaging of python dependenices for people who are wanting to self host the packages.'

setup(
        name="pypi_wrangler", 
        version=VERSION,
        author="Landon Miller",
        author_email="millerlm012@email.com",
        url="https://github.com/Millerlm012/PyPiWrangler",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'pypi', 'wrangler'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
            "Programming Language :: Python :: 3.9"
        ]
)