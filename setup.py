from setuptools import find_packages, setup

VERSION = '0.0.1'
DESCRIPTION = 'Hanzi decomposition and dictionary'
LONG_DESCRIPTION = 'Hanzi decomposition and dictionary'

# Setting up
setup(
        name='hanzipy',
        version=VERSION,
        author='Quentin Lathière',
        author_email='',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=[
            'python', 'hanzi', 'hanzipy', 'decomposition', 'cjk', 'dictionary',
        ],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Education',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
        ]
)
