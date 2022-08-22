import setuptools

setuptools.setup(
    name='pythonGateway',
    version='1.0.0',
    packages=['pythonGateway',],
    license='MIT',
    description = 'Python wrapper for Bitocredit API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Reza Motahary',
    author_email = 'reza.rz00980pp@gmail.com',
    install_requires=['requests'],
    url = 'https://github.com/bitocredit/python-gateway',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )