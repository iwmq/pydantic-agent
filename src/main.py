from dotenv import load_dotenv
from pydantic_ai.agent import Agent, AgentRunResult
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.deepseek import DeepSeekProvider

from tools import tools


load_dotenv()

model = OpenAIModel(model_name="deepseek-chat", provider=DeepSeekProvider())
agent = Agent(
    model=model,
    system_prompt="You are a expericed Python programmer",
    tools=tools
)


def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response: AgentRunResult[str] = agent.run_sync(user_prompt=user_input)
        print(f"Agent: {response.output}")


if __name__ == "__main__":
    main()