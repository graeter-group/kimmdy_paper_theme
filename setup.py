from setuptools import setup, find_packages

setup(
    name='kimmdy_paper_theme',                    # Package name (shown on PyPI)
    version='0.1',
    description='Theme elements for the kimmdy emulato paper',
    author='BMM',
    packages=find_packages(),          # Automatically finds packages in this folder
    install_requires=[],               # Add dependencies here if needed
    python_requires='>=3.6',
)