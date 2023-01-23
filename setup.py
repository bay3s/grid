from setuptools import setup

with open('requirements.txt', 'r') as fh:
    requirements = fh.read()

setup(
    name='grid',
    author='bay3s',
    description='Gridworld environment for Reinforcement Learning',
    license = 'Creative Commons Attribution-Noncommercial-Share ALike License',
    packages = ['grid'],
    python_requires='>=3.7',
    install_requires=requirements,
)
