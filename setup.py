from setuptools import setup

setup(
    name="live score",
    version="0.0.1",
    description="REST API using FastAPI",
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
    python_requires=">=3.9",
    include_package_data=True,
    zip_safe=False,
)