"""Version information."""

import platform


def package_version():
    """Return version of this package."""
    package_name = "arbpackage"
    import pkg_resources

    return pkg_resources.get_distribution(package_name).version


__version__ = package_version()


def get_version():
    """Return package-name __version__ python python_version."""
    return f"arbpackage {__version__} " f"python {platform.python_version()}"


if __name__ == "__main__":
    """Entry point for script execution.

    Makes it easy to get version number from cli from outside the package.
    """
    print(__version__)
