import pathlib
import re
import os

__here__ = pathlib.Path(__file__).parent
project_root = __here__ / ".."
dirs = [
    project_root / ".." / "directory-sso",
    project_root / ".." / "directory-sso-profile",
    project_root / ".." / "help",
    project_root / ".." / "directory-ui-buyer",
    project_root / ".." / "directory-ui-export-readiness",
    project_root / ".." / "navigator",
]
req_files = [
    "requirements.txt",
    "requirements.in",
    "requirements_test.txt",
    "requirements_test.in",
]

exp = r'(?:directory-header-footer\.git@v)(\d*\.\d*\.\d)'
get_version = r'\d*\.\d*\.\d'


def get_update_info():
    new_version = input("Version to upgrade to: ")
    replace_in_dirs(new_version)


def get_file_string(filepath):
    """Get string from file."""
    with open(os.path.abspath(filepath)) as f:
        return f.read()


def current_version():
    filepath = os.path.abspath(
        project_root / "directory_header_footer" / "version.py")
    version_py = get_file_string(filepath)
    regex = re.compile(get_version)
    print(regex.search(version_py).group(0))
    if regex.search(version_py) is not None:
        current_version = regex.search(version_py).group(0)
        print("Current directory-header-footer version:", current_version)
        get_update_info()
    else:
        print("Error finding directory-header-footer version.")


def done(version):
    print("Upgraded to version ", version)


def header_footer_exists(filepath):
    with open(filepath) as f:
        return re.search(exp, f.read())


def replace_in_files(dirname, replace):
    for filename in req_files:
        filepath = os.path.abspath(dirname / filename)
        if os.path.isfile(filepath) and header_footer_exists(filepath):
            replaced = re.sub(exp, replace, get_file_string(filepath))
            with open(filepath, "w") as f:
                f.write(replaced)
            print("Written to file: ", filepath)


def replace_in_dirs(version):
    print("Upgrading directory-header-footer dependency in all repos...")
    for dirname in dirs:
        replace = "directory-header-footer.git@v{}".format(version)
        replace_in_files(dirname, replace)
    done(version)


if __name__ == '__main__':
    current_version()
