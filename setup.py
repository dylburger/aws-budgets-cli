from setuptools import setup, find_packages

setup(
    name="awsbudget",
    version='0.0.1',
    py_modules=['awsbudget'],
    packages=find_packages(),
    install_requires=[
        'boto3',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        awsbudget=awsbudget:cli
    ''',
)
