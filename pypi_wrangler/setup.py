from setuptools import setup, find_packages

VERSION = '0.0.1'
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
            "Development Status :: Alpha",
            "Intended Audience :: Engineers / Dev Ops",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Linux"
        ]
)