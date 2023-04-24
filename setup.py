from setuptools import setup

setup(
    name='vinnieshell',
    version='0.1.5',
    author='VilariStorms',
    author_email='vilari@goatmail.uk',
    description='Vinnies Multi-Shell-Handler, a reverse shell handler that can handle multiple shells',
    packages=["vinnieshell"],
    entry_points={
        'console_scripts': [
            'vinnieshell=vinnieshell.main:main'
        ]
    },
    install_requires=[
        'requests'
    ],
)

