from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ['Click']
setup(
    name="tymebox",
    version="0.0.1",
    author="Parker Hyde",
    author_email="parkerhyde79@gmail.com",
    description="CLI app to manage time and track accomplishments",
    url="https://github.com/pahyde/tymebox/",
    packages=['tymebox'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'tymebox = tymebox.__main__:cli'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)