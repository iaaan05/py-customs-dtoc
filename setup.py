from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='customs_dtoc',
    version='0.0.9',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={
        'customs_dtoc.landed_cost.components_of_lc.ac.pom_micp': ['containerized_dangerous_cargo/*.json'],
        'customs_dtoc.landed_cost.components_of_lc.ac.pom_micp.fcl': ['*.json'],
        'customs_dtoc.landed_cost.components_of_lc.ac.pom_micp.lcl': ['*.json'],
        'customs_dtoc.landed_cost.components_of_lc.wd.pom_micp.fcl': ['*.json'],
        'customs_dtoc.landed_cost.components_of_lc.wd.pom_micp.lcl': ['*.json'],
    },
    install_requires=[],
    python_requires='>=3.11',
    license='MIT',
    author='Iaaan05',
    author_email='iaaan100500@gmail.com',
    description='A package for calculating customs duties, taxes, and other charges.',
    keywords=['customs', 'duties', 'taxes', 'charges'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iaaan05/python-customs-tax-package',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11'
    ]
)
