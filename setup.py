from setuptools import setup

setup(
    name='jsonbox',
    description='Python wrapper for jsonbox.io',
    url='https://github.com/harlev/jsonbox-python',
    version='0.2.0',
    packages=['.'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['requests'],
    python_requires='>=2.7',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)