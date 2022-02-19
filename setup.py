from setuptools import setup, find_packages

requirements = [
    "numpy",
    ]

setup(
    name="python-test-Mafe-Morris",
    version="0.0.1",
    author="Maria Fernanda Morris",
    author_email="mafemorris99@gmail.com",
    description="Basic lens and sensor simulator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires = requirements,
    package_dir={"": "camera_simulator"},
    packages=find_packages(where="camera_simulator"),
    python_requires=">=3.6",
    entry_points={'console_scripts': ['pysensor=sensor:mymean']
    },
)