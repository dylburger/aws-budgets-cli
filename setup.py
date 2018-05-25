from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="awsbudget",
    description='Tool to manage a single, simple AWS Budget',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords=['aws', 'budget'],
    version='0.0.7',
    author='Dylan Sather',
    author_email='dylan.sather@gmail.com',
    url='https://github.com/dylburger/aws-budgets-cli',
    license='MIT',
    python_requires='>=3',
    py_modules=['awsbudget'],
    packages=find_packages(),
    install_requires=[
        'boto3',
        'click',
        'setuptools',
    ],
    entry_points='''
        [console_scripts]
        awsbudget=awsbudget:cli
    ''',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ),
    zip_safe=False
)
