from setuptools import setup

setup(
    name='nums2mask',
    version='1.0.2',
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
