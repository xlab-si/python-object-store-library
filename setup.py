import setuptools

setuptools.setup(
    use_scm_version=dict(
        write_to="object_store/version.py",
    ),
)
