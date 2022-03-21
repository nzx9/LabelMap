import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="labelmap",
    version="0.0.1",
    author="Navindu Dananga",
    author_email="navindum@protonmail.com",
    license="MIT",
    description="Generate label maps from CSV files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nzx9/LabelMap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pandas"],
)
