from setuptools import find_packages, setup

description = ('A Scrapy middleware for scraping '
               'Wayback Machine snapshots from archive.org.')
long_description = description + \
        (' For further details, '
         'please see the code repository on github: '
         'https://github.com/sangaline/scrapy-wayback-machine')


setup(
    name='scrapy-wayback-machine',
    version='1.0.0',
    author='Evan Sangaline',
    author_email='evan@intoli.com',
    description=description,
    license='ISC',
    keywords='archive.org scrapy scraper waybackmachine middleware',
    url="https://github.com/sangaline/scrapy-wayback-machine",
    packages=find_packages(),
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Topic :: Utilities',
        'License :: OSI Approved :: ISC License (ISCL)',
    ],
    install_requires=[
        'cryptography',
        'scrapy',
        'twisted',
    ]
)
