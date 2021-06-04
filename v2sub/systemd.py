
from subprocess import CalledProcessError, run
from typing import Iterable
from v2sub import BASE_PATH
import os

SYSTEMD_UNIT = os.path.join(BASE_PATH, 'unit.json')
SYSTEMD_RUN_CMD = [
            "systemd-run",
            "--user",
            "--collect",
            "-p",
            "Restart=on-failure",
        ]


def start(cmd: Iterable) -> dict:
        SYSTEMD_RUN_CMD.extend(cmd)

        proc = run(
            SYSTEMD_RUN_CMD,
            check=True,
            capture_output=True,
        )

        return {"unit": proc.stderr.decode().split(":")[1].strip()}


def is_active(unit: str) -> bool:
    try:
        proc = run(
            ["systemctl", "--user", "is-active", unit],
            check=True,
            capture_output=True,
        )
    except CalledProcessError:
        return False
    else:
        if "active" in proc.stdout.decode():
            return True
    return False


def stop(unit: str) -> None:
    run(
        ["systemctl", "--user", "stop", unit],
        check=False,
        capture_output=True
    )
