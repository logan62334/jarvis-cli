from setuptools import setup, find_packages

__version__ = '1.0.2'

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="jarvis-grabfood",
    version=__version__,

    description="grabfood",
    long_description=long_description,
    long_description_content_type='text/markdown',

    author="mafei",

    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    platforms="any",
    install_requires=[
        'click',
        'jmdevice',
        'uiautomator2',
        'playsound',
        'PyObjC'
    ],
    entry_points={
        'console_scripts': [
            'jarvis = jarvis.cli.entrypoint:jarvis',
        ]
    }
)
