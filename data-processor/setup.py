from setuptools import setup

setup(
    name="data-processor",
    version='0.0.1',
    install_requires=[
        'numpy',
        'requests',
        'importlib-metadata; python_version<"3.10"',
    ],
)

#https://setuptools.pypa.io/en/latest/build_meta.html

#Youtube Video: How to build a complete python package step by step -> https://www.youtube.com/watch?v=5KEObONUkik
