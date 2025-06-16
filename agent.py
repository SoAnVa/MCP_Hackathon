from smolagents import CodeAgent, LiteLLMModel
import tools
import os

LLM_API_KEY = os.getenv("LLM_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "claude-sonnet-4-20250514")

model = LiteLLMModel(
    model_id=MODEL_NAME,
    api_key=LLM_API_KEY
)

agent = CodeAgent(
    tools=[
        tools.list_users,
        tools.get_amount,
        tools.load_user_profile_from_file
    ],
    model=model,
    add_base_tools=True,
    max_steps=5,
)