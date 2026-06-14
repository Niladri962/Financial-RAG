from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm.llm_model import load_llm
from prompts.finance_prompt import template

llm = load_llm()

prompt = PromptTemplate(
    template=template,
    input_variables=["context","question"]
)

parser = StrOutputParser()

chain = prompt | llm | parser