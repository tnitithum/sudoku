import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sudoku",
    version="0.0.1",
    author="Thanakorn Nitithumbundit",
    author_email="tnitithumbundit@gmail.com",
    description="Sudoku solver for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tnitithum/sudoku",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)