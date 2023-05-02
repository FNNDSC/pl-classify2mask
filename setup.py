from setuptools import setup
import re

_version_re = re.compile(r"(?<=^__version__ = (\"|'))(.+)(?=\"|')")


def get_version(rel_path: str) -> str:
    """
    Searches for the ``__version__ = `` line in a source code file.
    https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
    """
    with open(rel_path, 'r') as f:
        matches = map(_version_re.search, f)
        filtered = filter(lambda m: m is not None, matches)
        version = next(filtered, None)
        if version is None:
            raise RuntimeError(f'Could not find __version__ in {rel_path}')
        return version.group(0)


setup(
    name='nums2mask',
    version=get_version('nums2mask/__init__.py'),
    description='Create brain mask from segmentation',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    url='https://github.com/FNNDSC/pl-nums2mask',
    packages=['nums2mask'],
    install_requires=['chris-plugin==0.2.0a1', 'loguru~=0.6.0'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'nums2mask = nums2mask.app:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ]
)
