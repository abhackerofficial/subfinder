from setuptools import setup, find_packages

setup(
    name='subfinder',
    version='1.0',
    author='ABHacker a.k.a Ankush Bhagat',
    author_email='63346676+abhackerofficial@users.noreply.github.com',
    description="A python based tool for finding subdomains of a domain.",
    url='https://github.com/abhackerofficial/subdomain-finder',
    packages=find_packages(),
    py_modules=['subfinder'],
    install_requires=[
        'requests',
        'rich'
    ],
    entry_points={
        'console_scripts': ['subfinder=subfinder.__main__:main'],
    },
)
