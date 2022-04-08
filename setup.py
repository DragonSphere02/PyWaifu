from setuptools import setup
import setuptools

with open('README.md', encoding='utf-8') as read_me:
    readme = read_me.read()

version = '1.0.1'

setup(
    author='DragonSh',
    version=version,
    author_email='isaiasfb8@gmail.com',
    description='PyWaifu is a simple package that shows cute waifus',
    install_package_data=True,
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='waifu discord bots',
    name='PyWaifu',
    url='https://github.com/DragonSphere02/PyWaifu',
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Internet"
    ],

)
