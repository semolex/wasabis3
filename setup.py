from setuptools import setup

setup(
    name='wasabis3',
    version='0.9',
    packages=['wasabis3'],
    url='https://github.com/semolex/wasabis3',
    license='MIT',
    author='semolex (Oleksii Semeshchuk)',
    install_requires=[
        'boto3'
    ],
    zip_safe=True,
    author_email='semolex@live.com',
    description='Wrapper for boto3 library, created to be used with Wasabi Hot Cloud Storage'
)

