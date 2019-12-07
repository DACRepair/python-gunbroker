from setuptools import setup, find_packages

setup(
    name="python-gunbroker",
    description="Gunbroker search scraping library",
    version="1.0",

    author="DACRepair",
    author_email="dacrepair@gmail.com",

    packages=find_packages(),
    python_requires='>=3.*',  # I need to figure this out...
    install_requires=[
        'requests',
        'beautifulsoup4'
    ]
)
