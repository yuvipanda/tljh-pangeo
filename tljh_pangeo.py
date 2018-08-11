from tljh.hooks import hookimpl


@hookimpl
def tljh_extra_user_conda_packages():
    # FIXME: specify versions here.
    return [
        'xarray',
        'iris',
        'dask',
    ]


@hookimpl
def tljh_config_post_install(config):
    """
    Set JupyterLab to be default
    """
    if 'user_environment' not in config or 'default_app' not in config['user_environment']:
        config['user_environment']['default_app'] = 'jupyterlab'