from setuptools import setup, find_packages

setup(
    name='taskaty',
    version='0.1',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            'taskaty=taskaty.app:main'
        ]
    }
)
