from setuptools import setup

setup(
    name="tljh-pangeo",
    install_requires="the-littlest-jupyterhub",
    entry_points={"tljh": ["pangeo = tljh_pangeo"]},
    py_modules=["tljh_pangeo"],
)

