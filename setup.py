from setuptools import setup

setup(
    name="awsbudget",
    version='0.0.1',
    py_modules=['awsbudget'],
    install_requires=[
        'boto3',
        'Click',
        'CloudFormationClient'
    ],
    entry_points='''
        [console_scripts]
        awsbudget=awsbudget:cli
    ''',
)
