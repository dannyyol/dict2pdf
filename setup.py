from setuptools import setup, find_packages

setup(
    name="dict2pdf",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'reportlab>=3.6.12',
        'pandas>=1.3.0'
    ],
    description="A package for generating PDFs from structured data",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dannyyol/dict2pdf",
    project_urls={
        "Homepage": "https://github.com/dannyyol/dict2pdf",
        "Bug Tracker": "https://github.com/dannyyol/dict2pdf/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)