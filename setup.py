from setuptools import setup, find_packages

req_tests = ["pytest", "pytest-httpserver", "pytest-asyncio", "requests", "plyvel"]
req_lint = ["flake8", "flake8-docstrings"]
req_etc = ["black", "isort"]
req_dev = req_tests + req_lint + req_etc

install_requires = [
    'pyjwt>=2.0.0',
    'pandas',
    'requests',
    'websockets',
    'aiohttp'
]

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup_options = {
    "name": "pyupbit",
    "version": "0.2.20",
    "author": "Jonghun Yoo, Brayden Jo, winDy",
    "author_email": "brayden.jo@outlook.com, jonghun.yoo@outlook.com, pyquant@outlook.com",
    "description": "python wrapper for Upbit API",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/sharebook-kr/pyupbit",
    "packages": find_packages(),
    "install_requires": install_requires,
    "extras_require": {
        "tests": req_tests,
        "lint": req_lint,
        "dev": req_dev
    },
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    "python_requires": ">=3.9.5"
}

setup(**setup_options)
