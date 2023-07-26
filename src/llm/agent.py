from langchain.prompts import PromptTemplate
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import Tool


B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = """
You are a help, respecful and honest assistant. Always answer as helpfully and honestly as possible, while being safe. If you do not know the answer, explain why you do not know the answer.
"""


def get_promopt(instruction: str, new_system_prompt: str = DEFAULT_SYSTEM_PROMPT):
    SYSTEM_PROMPT = B_SYS + new_system_prompt + E_SYS
    promopt_template = B_INST + SYSTEM_PROMPT + instruction + E_INST
    return promopt_template


search = DuckDuckGoSearchRun()

tools = [Tool(name="Search", func=search.run, description="Useful medical advise")]
obj = search.run("How can I treat a sprained ankle?")
print(type(obj))

print(obj)


search.run("site:webmd.com How can I treat a sprained ankle?")
