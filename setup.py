from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='RNA',
    version='0.1',
    packages=['newsdataapi', 'django'],
    description='Python library for the Rich News Aggregator (RNA)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hmyhill/RNA-BE',
    author='RNA',
    author_email='henry.myhill201@gmail.com',
    license='MIT',
    python_requires='>=3.5',
    keywords=[
        'news',
        'news data',
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]

)