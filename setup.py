import os
from setuptools import setup, find_packages

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path) as file:
        content = file.read()
    return content if content else 'no content read'


setup(
    name='gw-mkdocs-encryptcontent-plugin',
    version='0.0.3f',
    author='CoinK0in, fork by greg-witczak',
    author_email='6830461+greg-witczak@users.noreply.github.com',
    description='A fork of MkDocs plugin that encrypt/decrypt markdown content with AES',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown encrypt decrypt content',
    url='https://github.com/greg-witczak/mkdocs-encryptcontent-plugin',
    license='MIT',
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[
        'mkdocs',
        'pyyaml',
        'pycryptodome',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'encryptcontent = encryptcontent.plugin:encryptContentPlugin'
        ]
    },
    package_data={'encryptcontent': ['*.tpl.html']},
    include_package_data = True
)
