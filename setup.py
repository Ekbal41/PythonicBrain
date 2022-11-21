import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonicBrain",
    version="0.0.1",
    author="Asif Ekbal",
    author_email="mdasifekbalshagor@gmail.com",
    description="A python Util package ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ekbal41/PythoniBrain",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ),
)