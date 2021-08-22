"""version.py unit tests."""
import platform

import arbpackage.version


def test_get_version():
    """Version is as expected."""
    actual = arbpackage.version.get_version()
    expected = (
        f"arbpackage {arbpackage.version.__version__} "
        f"python {platform.python_version()}"
    )
    assert actual == expected, "version not returning correctly"


def test_package_version():
    """Package version by package_version() shall equal __version__."""
    by_var = arbpackage.version.__version__
    by_func = arbpackage.version.package_version()
    assert by_var == by_func
