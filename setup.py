from setuptools import setup, find_packages

setup(
    name="Colorizex",
    version="0.0.6",
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    author="Sarvesh Bhujle",
    author_email="sarveshbhujle2609@gmail.com",
    description="Colorizex is a professional Python library that enhances console output with structured and colorful messages. Built on top of the powerful `rich` library, it provides an intuitive way to style text, highlight logs, and improve CLI application readability.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
