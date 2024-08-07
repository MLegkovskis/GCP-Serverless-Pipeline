from setuptools import setup, find_packages

setup(
    name='ntg_sdk',
    version='0.1.1',
    description='SDK for interacting with the Hello Cloud Function',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'ntg-sdk=sdk:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
