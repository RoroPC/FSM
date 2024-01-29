from setuptools import setup, find_packages
setup(
        name="FSM",
        version="1.0.0",
        description="Finite State Machine manager",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
)
