def test_package_import():
    """Test that the package can be imported."""
    import apache_airflow_providers_asimov
    assert apache_airflow_providers_asimov.__version__ is not None


def test_version_format():
    """Test that the version is a valid string."""
    from apache_airflow_providers_asimov import __version__
    assert isinstance(__version__, str)
    assert __version__ != "0.0.0"  # Ensure version is set by hatch-vcs
