from smolagents import CodeAgent, LiteLLMModel
import tools
import os

LLM_API_KEY = os.getenv("LLM_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "claude-sonnet-4-20250514")

# Utilise Claude ou OpenAI via LiteLLM
model = LiteLLMModel(
    model_id=MODEL_NAME,
    api_key=LLM_API_KEY
)

# Agent avec tools vulnérables
agent = CodeAgent(
    tools=[
        tools.hello_world,
        tools.list_users,
        # tools.search_user,  # vulnérable
        # tools.execute_sql  # vulnérable
        tools.get_amount
    ],
    model=model,
    add_base_tools=True
)