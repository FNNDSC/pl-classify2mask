from setuptools import setup

setup(
    name='nums2mask',
    version='1.0.0',
    description='Create brain mask from segmentation',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    url='https://github.com/FNNDSC/pl-nums2mask',
    packages=['nums2mask'],
    install_requires=['chris_plugin', 'loguru'],
    license='MIT',
    python_requires='>=3.10.2',
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
