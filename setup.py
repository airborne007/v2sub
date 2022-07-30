import setuptools
from v2sub import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="v2sub",
    version=__version__,
    author="airborne007",
    author_email="isrfhltc@outlook.com",
    description="A v2ray subscriber written in python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/airborne007/v2sub",
    packages=setuptools.find_packages(),
    keywords=["v2ray", "subscriber", "linux"],
    install_requires=[
        "click>=7.0",
        "simple-term-menu>=1.2.1"
    ],
    python_requires='>=3',
    license="MIT",
    project_urls={
        'Tracker': 'https://github.com/airborne007/v2sub/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        'console_scripts': [
            'v2sub=v2sub.command:cli',
        ],
    },
)
