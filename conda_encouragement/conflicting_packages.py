from functools import cache

from agno.agent import Agent
from agno.tools.workspace import Workspace
from agno.models.openrouter import OpenRouter


def package_suggestion(target_prefix: str):
    package_suggestion = Agent(
        name="Unsatisfiable error suggestion",
        model=OpenRouter(id="anthropic/claude-opus-4.1"),
        tools=[Workspace(root=str(target_prefix), allowed=["read", "list", "search", "shell"])],
        instructions=(
            "Analyze the command and error message provided. Consider all the listed packages and "
            "provide a response that summarizes the root issue in 2-5 sentences and recommends "
            "2-3 alternatives for the user to get the packages they desire installed with conda."
        ),
        markdown=True,
    )
    return package_suggestion
