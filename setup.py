from setuptools import setup, find_packages

with open('requirements.txt', 'r') as fh:
    requirements = fh.read()

setup(
    name='grid',
    description='Gridworld environment for Reinforcement Learning',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/iglu-contest/gridworld',
    author='bay3s',
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
