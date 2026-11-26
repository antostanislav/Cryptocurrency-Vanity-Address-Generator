import os
import sys
import subprocess


def main():

    root = os.path.dirname(os.path.abspath(__file__))
    setup = os.path.join(root, "setup.py")

    if not os.path.isfile(setup):
        raise FileNotFoundError("setup.py not found!")

    env = os.environ.copy()
    env["INSTALL_ROOT"] = root

    subprocess.run(
        [sys.executable, setup],
        cwd=root,
        env=env,
        check=True
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Failed: {e}")
        sys.exit(1)
