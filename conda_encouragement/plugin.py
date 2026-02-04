from __future__ import annotations

from conda.plugins import hookimpl
from conda.plugins.types import CondaPreCommand


def pre_install_action(command: str) -> None:
    print("Oh ya, thats a great thing to try to install, good choice!")


def pre_activate_action(command: str) -> None:
    print("echo 'There is some good stuff in that environment, enjoy!'")


@hookimpl
def conda_pre_commands():
    yield CondaPreCommand(
        name="install-encouragement",
        action=pre_install_action,
        run_for={"install"},
    )

    yield CondaPreCommand(
        name="activate-encouragement",
        action=pre_activate_action,
        run_for={"activate"},
    )
