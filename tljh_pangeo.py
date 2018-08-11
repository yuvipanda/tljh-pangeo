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
    user_environment = config.get('user_environment', {})
    user_environment['default_app'] = user_environment.get('default_app', 'jupyterlab')

    config['user_environment'] = user_environment