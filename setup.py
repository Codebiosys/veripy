import os
import re
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def yield_packages(path):
    """Simple parser for requirements.txt files"""
    with open(path) as requirements:
        for line in requirements:
            if re.match('^[a-zA-Z]', line):
                yield line.strip()


REQUIRES = list(yield_packages('requirements.txt'))
DEVELOP = list(yield_packages('requirements-development.txt'))

setup(
    name='veripy',
    version='0.2.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Gherkin testing made easy',
    long_description=README,
    url='https://github.com/Codebiosys/veripy.git',
    author='CodeBiosys, Inc',
    author_email='developers@codebiosys.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=REQUIRES,
    extras_require={'develop': DEVELOP},
    tests_require=DEVELOP,
    #  entry_points="""
    #      [console_scripts]
    #      pydf=pydf.commands.cli:main
    #  """
)
