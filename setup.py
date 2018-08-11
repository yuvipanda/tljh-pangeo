from setuptools import setup

setup(
    name="tljh-pangeo",
    entry_points={"tljh": ["pangeo = tljh_pangeo"]},
    py_modules=["tljh_pangeo"],
)

