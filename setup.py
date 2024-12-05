from setuptools import setup, find_packages

setup(
    name="MeineAI",  # Package name
    version="0.1.0",  # First version
    author="Your Name",  # Replace with your name
    description="MeineAI: A CLI tool and AI utility package",
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files
    package_data={
        "MeineAI": [
            "Resources/*",  # Include quotes.txt
            "trainedspacy/*",  # Include Spacy files
        ]
    },
    install_requires=[
        "spacy",  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
