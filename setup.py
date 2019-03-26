# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='godwill',
    version='1.0.0',
    description='周易64卦',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    author='Rocky',
    url='https://github.com/rockyCheung/godwill.git',
    author_email='274935730@qq.com',
    license='PSF',
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    install_requires=['pytest>=4.3.1','readme-renderer>=21.0'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst','*.yml','*.md','LICENSE'],
        'gwill': ['data/gua_ci/i_*'],
    },
   # include_package_data=True,
    zip_safe=True,
    python_requires='>=3',
    scripts = [],
    entry_points = {
        'console_scripts': [
            'gwill = gwill.changes.BChanges:godwill',
         ]
     }
)