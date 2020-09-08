import re

from setuptools import setup, find_packages

dev_requires = [
    'coverage==4.1b2',
    'flake8==2.5.4',
    'flake8-debugger==1.4.0',
    'flake8-quotes==0.2.4',
    'nose==1.3.7',
    'pep8-naming==0.3.3',
    'rednose==1.1.0',
    'sure==1.2.24',
    'factory-boy==2.10.0'
]

def get_version():
    with open('sqlalchemy_pagination/__init__.py', 'r') as f:
        version_regex = r'^__version__\s*=\s*[\'"](.+)[\'"]'
        return re.search(version_regex, f.read(), re.MULTILINE).group(1)

setup(
    name='sqlalchemy-pagination',
    version=get_version(),
    url='https://github.com/wizeline/sqlalchemy-pagination',
    author='Wizeline',
    author_email='engineering@wizeline.com',
    description='A small utility to paginate SqlAlchemy queries.',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    keywords=['sqlalchemy', 'pagination', 'paginate'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    tests_require=dev_requires,
    install_requires=[
        'SqlAlchemy'
    ],
    extras_require={
        'dev': dev_requires
    }
)
