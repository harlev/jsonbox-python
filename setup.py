from setuptools import setup

setup(
    name='jsonbox',
    description='Python wrapper for jsonbox.io',
    url='https://github.com/harlev/jsonbox-python',
    author="Ron Harlev",
    author_email="harlev@gmail.com",
    version='1.0.0',
    packages=['.'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['requests', 'six'],
    python_requires='>=2.7',
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
