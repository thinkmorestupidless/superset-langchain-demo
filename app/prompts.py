from langchain import PromptTemplate

prompt = PromptTemplate(
    input_variables=["chart_type", "metric", "period"],
    template="Can you provide me with a {chart_type} that displays {metric} per {period}?",
)

# Format the prompt with the given inputs
# TODO: do we need this step?
prompt.format(chart_type="pie chart", metric="car sales", period="month")
