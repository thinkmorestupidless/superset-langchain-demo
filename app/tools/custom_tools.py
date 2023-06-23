from dotenv import find_dotenv, load_dotenv
from langchain.chains import LLMChain
from langchain.llms import OpenAI

from app.prompts import prompt

# Load environment variables
load_dotenv(find_dotenv())

# Initialise the LLM to use for the agent
llm = OpenAI()


# Chain the LLM with the provided prompt
# We predefine the prompt, combine it with user input and run using a Chain
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run(metric="car sales", period="month"))













# #def demo_tool() -> str:
# llm = ChatOpenAI(temperature=0)
#
# # Load the tool configs that are needed.
# search = SerpAPIWrapper()
# llm_math_chain = LLMMathChain(llm=llm, verbose=True)
# tools = [
#     Tool.from_function(
#         func=search.run,
#         name="Search",
#         description="useful for when you need to answer questions about current events"
#         # coroutine= ... <- you can specify an async method if desired as well
#     ),
# ]
#
# class CalculatorInput(BaseModel):
#     question: str = Field()
#
# tools.append(
#     Tool.from_function(
#         func=llm_math_chain.run,
#         name="Calculator",
#         description="useful for when you need to answer questions about math",
#         args_schema=CalculatorInput
#         # coroutine= ... <- you can specify an async method if desired as well
#     )
# )
#
# # Construct the agent. We will use the default agent type here.
# # See documentation for a full list of options.
# agent = initialize_agent(
#     tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
# )
#
# agent.run(
#     "Please provide me with the number of card sold per month."
# )
