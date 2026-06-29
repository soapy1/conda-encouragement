from __future__ import annotations

from .conflicting_packages import package_suggestion

from conda.plugins import hookimpl
from conda.plugins.types import CondaPreCommand, CondaExceptionObserver


def pre_activate_action(command: str) -> None:
    print("echo 'There is some good stuff in that environment, enjoy!'")


def unsatisfiable_hint(event):
    print("\nConflicting packages found, analyzing and providing a solution")
    suggestion_agent = package_suggestion(event.target_prefix)
    suggestion_agent.print_response(
        f"Given the command {' '.join(event.argv)} the following error is produced: {event.exc_value}",
        stream=True,
        show_message=False,
        show_reasoning=True,
    )


@hookimpl
def conda_pre_commands():
    yield CondaPreCommand(
        name="activate-encouragement",
        action=pre_activate_action,
        run_for={"activate"},
    )


@hookimpl
def conda_exception_observers():
    yield CondaExceptionObserver(
        name="unsatisfiable-error",
        hook=unsatisfiable_hint,
        watch_for={"UnsatisfiableError"},
    )