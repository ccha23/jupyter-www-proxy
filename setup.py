import setuptools

setuptools.setup(
    entry_points={
        "jupyter_serverproxy_servers": ["www = jupyter_www_proxy:setup_www",]
    },
    package_data={"jupyter_www_proxy": ["icons/*"]}
)
