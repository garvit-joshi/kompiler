import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kompiler",
    version="v0.1.6",
    author="Garvit Joshi",
    author_email="garvitjoshi9@gmail.com",
    description="A package for auto compiling C++ files as soon as they are saved.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garvit-joshi/kompiler",
    packages=["kompiler"],
    keywords = "C++ Compiling g++",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Education',
        'Programming Language :: C++',
        'Topic :: Utilities',
    ],
    python_requires='>=3.5',
    entry_points={
        "console_scripts": [
            "kompiler = kompiler.__main__:main"
        ]
    },
)