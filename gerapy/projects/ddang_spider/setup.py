# Automatically created by: gerapy
from setuptools import setup, find_packages
setup(
    name='ddang_spider',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy':['settings=ddang_spider.settings']},
)