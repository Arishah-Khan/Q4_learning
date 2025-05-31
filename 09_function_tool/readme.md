# Let Your AI Do Real Work  
### A Guide to the Function Tool in OpenAI's Agent SDK

When we build AI agents — like virtual assistants or smart bots — we don't just want them to answer questions. We want them to **take action**: fetch data, read files, make API calls, or even collaborate with other agents.

That’s where **Tools** in OpenAI’s Agent SDK come into play.  
Among them, the **Function Tool** is one of the most powerful and flexible options you can use.

---

##  Tool Types in OpenAI Agent SDK

There are three main categories of tools:

- **Hosted Tools** – Built-in tools like Web Search, File Search, Code Interpreter.
- **Function Tools** – Turn your own Python functions into tools.
- **Agents as Tools** – Make one agent callable by another.

> In this guide, we’ll focus on the **Function Tool**.

---

##  What Is a Function Tool?

A **Function Tool** lets you wrap any Python function so that your AI agent can use it like a real-world tool.

Since the agent actually calls these functions to perform tasks, some developers also refer to it as **Tool Calling**.

The agent automatically understands:

- What the tool does (from its docstring)
- What inputs it needs (from function arguments)
- How to call it (automatically validated with schemas)

###  How to use it?

1. Write a Python function  
2. Add the `@function_tool` decorator  
3. Add the function to your Agent

Your AI can now use it just like a human would!

---

##  Example: Make a Weather Tool

from agents import Agent, function_tool
from typing_extensions import TypedDict

class Location(TypedDict):
    lat: float
    long: float

@function_tool
async def fetch_weather(location: Location) -> str:
    """Fetch the weather for a given location."""
    return "Weather is sunny"

agent = Agent(
    name="Weather Agent",
    tools=[fetch_weather]
)

##  What This Does

-  **Registers** `fetch_weather` as a tool  
-  **Uses** the function docstring as the tool **description**  
-  **Converts** the input type into a **JSON schema automatically**  
-  **Allows** the agent to **call the function** when needed  

# Behind the Scenes: How It Works

## Name  
Defaults to the function's name. You can override it using `name_override`.

## Description  
Automatically pulled from the function's docstring.

## Input Schema  
Generated from the function signature using Python type hints.

## Validation  
Function inputs are validated using Pydantic.

---

# How the SDK Works

- Uses Python's **`inspect`** module to extract the function signature.
- Uses **`griffe`** to parse docstrings.
- Uses **`pydantic`** to create and validate the input schema.

---

# When to Use Function Tools

Use a Function Tool when your agent needs to:

- Call external APIs  
- Read or write files  
- Interact with databases  
- Execute business logic  
- Collaborate with other agents or services  

Instead of hardcoding logic or doing everything inside the LLM’s response, delegate the actual work to your function tools.

# Creating FunctionTools Manually for More Control


```python
from agents import FunctionTool, RunContextWrapper
from pydantic import BaseModel

class Args(BaseModel):
    username: str
    age: int

async def run(ctx: RunContextWrapper, args: str) -> str:
    parsed = Args.model_validate_json(args)
    return f"{parsed.username} is {parsed.age} years old"

tool = FunctionTool(
    name="process_user",
    description="Processes user data",
    params_json_schema=Args.model_json_schema(),
    on_invoke_tool=run
)

``` 


# Handle errors with custom functions

```python

from agents import Agent, function_tool

def my_error_handler(error: Exception) -> str:
    return f"Oops! Something went wrong: {str(error)}"

@function_tool(failure_error_function=my_error_handler)
async def greet(name: str) -> str:
    """Say hello to the user.

    Args:
        name: The name of the person to greet.
    """
    if not name:
        raise ValueError("Name is required!")
    return f"Hello, {name}!"

agent = Agent(
    name="Friendly Agent",
    tools=[greet]
)

```


# Conclusion

The Function Tool in OpenAI's Agent SDK transforms your Python functions into powerful building blocks for AI agents. It bridges natural language understanding with real-world action.
By mastering this tool, you can create AI systems that don't just talk - they get things done.