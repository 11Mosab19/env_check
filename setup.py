from setuptools import find_packages,setup

setup(
    name="mEnv-Checker.py",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "rich",
        ],
    entry_points={
        "console_scripts":[
            "env-check=env_checker:main",
        ],
    },
)