from setuptools import setup

setup(
    name="live score",
    version="0.0.1",
    description="Signality Assignment",
    url="",
    author="Panagiotis Ef.",
    author_email="",
    license="",
    packages=[
        "app",
        "app.models",
        "app.schemas",
        "test"
    ],
    install_requires=[
        "fastapi",
        "uvicorn",
        "pytest"
    ],
    include_package_data=True,
    zip_safe=False,
)