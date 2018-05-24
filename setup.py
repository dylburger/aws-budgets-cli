from setuptools import setup

setup(
    name="awsbudget",
    version='0.0.1',
    py_modules=['awsbudget'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        awsbudget=awsbudget:cli
    ''',
)
