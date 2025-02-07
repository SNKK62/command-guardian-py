import os
import sys
import platform
from importlib.resources import files

def _check_os():
    if platform.system() == "Windows":
        print("This script is not supported on Windows.")
        sys.exit(1)

def _get_cli_path():
    cli_path = os.path.join(os.getcwd(), "bin", "cmgd")
    cli_path = files("cmgdpy").joinpath("bin")
    if platform.machine() == "arm64":
        cli_path = cli_path.joinpath("cmgd_arm64")
    elif platform.machine() == "x86_64":
        cli_path = cli_path.joinpath("cmgd_x86_64")
    else:
        print("Unsupported CPU architecture: " + platform.machine())
        sys.exit(1)
    return str(cli_path)

AVOID_DUPLICATE_OPTION = "--cli-executed"

def exec_guard():
    if AVOID_DUPLICATE_OPTION in sys.argv:
        sys.argv.remove(AVOID_DUPLICATE_OPTION)
        return

    _check_os()
    cli_path = _get_cli_path()
    print(cli_path)
    args = [cli_path, sys.executable, os.getcwd() + "/" + sys.argv[0], AVOID_DUPLICATE_OPTION] + sys.argv[1:]
    os.execv(cli_path, args)
