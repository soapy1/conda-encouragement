from functools import cache

from agno.agent import Agent
from agno.tools.workspace import Workspace
from agno.models.openrouter import OpenRouter


@cache
def package_suggestion(target_prefix: str):
    package_suggestion = Agent(
        name="Unsatisfiable error suggestion",
        model=OpenRouter(id="gpt-5-mini"),
        tools=[Workspace(root=str(target_prefix), allowed=["read", "list", "search", "shell"])],
        instructions=(
            "Analyze the command and error message provided. Consider all the listed packages and recommend "
            "up to 3 alternatives for the user to get the packages they desire installed."
        ),
        markdown=True,
    )
    return package_suggestion
