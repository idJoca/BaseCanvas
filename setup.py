import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="base-canvas",
    version="1.0.7",
    author="João Pedro Braz",
    author_email="brazjoaopedro@ymail.com",
    description="BaseCanvas is a small helper-class that handles common tasks in pygame.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idJoca/BaseCanvas",
    packages=setuptools.find_packages(),
    install_requires=['pygame'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)