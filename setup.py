# -*- coding: utf-8 -*-
"""
    ssword
    ~~~~~~

    A short description of the plugin.

    :copyright: (c) 2018 by zhongkui li.
    :license: BSD License, see LICENSE for more details.
"""
import ast
import re
from setuptools import find_packages, setup
from setuptools.command.install import install


with open("ssword/__init__.py", "rb") as f:
    version_line = re.search(
        r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
    ).group(1)
    version = str(ast.literal_eval(version_line))


setup(
    name="flaskbb-plugin-ssword",
    version=version,
    url="forums.demobingmap.cn",
    license="BSD License",
    author="zhongkui li",
    author_email="zhongkui.li@hotmail.com",
    description="A short description of the plugin.",
    long_description=__doc__,
    keywords="flaskbb plugin",
    packages=find_packages("."),
    include_package_data=True,
    package_data={
        "": ["ssword/translations/*/*/*.mo",
             "ssword/translations/*/*/*.po"]
    },
    zip_safe=False,
    platforms="any",
    entry_points={
        "flaskbb_plugins": [
            "ssword = ssword"
        ]
    },
    install_requires=[
        "FlaskBB",  # pin to a version to has pluggy integration
        "watchdog"
    ],
    setup_requires=[
        "Babel"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
