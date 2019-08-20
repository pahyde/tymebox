from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="tymebox",
    version="0.0.1",
    author="Parker Hyde",
    author_email="parkerhyde79@gmail.com",
    description="CLI app to manage time and track accomplishments",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pahyde/tymebox/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)