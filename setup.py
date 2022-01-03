from setuptools import find_packages, setup

from hanzipy import __version__ as version  # noqa  # isort:skip

DESCRIPTION = "Hanzi decomposition and dictionary"
EXTRAS_DEV_TEST = [
    "coverage",
    "pytest>=3.10",
]

# Setting up
setup(
    name="hanzipy",
    version=version,
    author="昆汀",
    author_email="synkx@hotmail.fr",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Synkied/hanzipy",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={
        "dev": EXTRAS_DEV_TEST,
        "dev-test": EXTRAS_DEV_TEST,
    },
    download_url=("https://github.com/Synkied/hanzipy/archive/%s.tar.gz" % version),
    keywords=[
        "python",
        "hanzi",
        "hanzipy",
        "decomposition",
        "cjk",
        "dictionary",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
    ],
)
