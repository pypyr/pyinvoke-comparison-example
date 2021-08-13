"""version.py unit tests."""
import arbpackage.version
import platform


def test_get_version():
    """Version is as expected."""
    actual = arbpackage.version.get_version()
    expected = (f'arbpackage {arbpackage.version.__version__} '
                f'python {platform.python_version()}')
    assert actual == expected, "version not returning correctly"
