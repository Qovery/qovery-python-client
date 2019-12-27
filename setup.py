import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qovery-client-rphilogene", # Replace with your own username
    version="0.1.0",
    author="Romaric Philogene",
    author_email="rphilogene@qovery.com",
    description="Qovery Python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Qovery/qovery-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APACHE2 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
