from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="telebot-plugins",
    version="0.1.2",
    author="Ahmed Negm",
    author_email="A7medNegm.x@gmail.com",
    description="A simple plugin system for pyTelegramBotAPI (telebot)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x7007x/TelebotPlugins",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pyTelegramBotAPI>=4.0.0",
    ],
)
