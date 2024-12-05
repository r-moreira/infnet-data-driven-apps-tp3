import getpass
import os
from langchain.prompts import PromptTemplate 
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API key:\n")

message_history = []
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
ddg_tool= DuckDuckGoSearchRun(name="Search") 
tools = [ddg_tool, wikipedia_tool]
llm = ChatOpenAI(temperature=0, model_name="gpt-4o", verbose=True, streaming=True)
 
def send_message(query):
    prompt = hub.pull("hwchase17/react")
    
    prompt_template = PromptTemplate(
        input_variable=["input", "tool_names", "tools", "agent_scratchpad"],
        template=prompt.template
    )
    
    agent = create_react_agent(llm=llm, prompt=prompt_template, tools=tools)

    agent_executor = AgentExecutor(agent=agent,
            tools=tools,
            handle_parsing_errors=True,
            verbose=True)
    
    response = agent_executor.invoke(
        input={
            "input": [
                ("history", message_history),
                ("human", query),
            ],
            "tool_names": [tool.name for tool in tools],
            "tools": [tool.description for tool in tools],
        }
    )
    
    message_history.append({"Human": query, "Assistant": response["output"]})
    
    print(f"\nAssistant: {response['output']}\n")

def view_history():
    if not message_history:
        print("\nNo messages yet.\n")
        return
    
    print("\nMessage History:")
    for message in message_history:
        print(message)
    print()

def main():
    while True:
        print("======== Choose your option =============")
        print("1 - Send messages to assistant")
        print("2 - View messages History")
        print("3 - Close Chat")
        option = input("Enter your choice: ")
        print("=========================================")

        if option == "1":
            query = input("\nEnter your message: ")
            send_message(query)
        elif option == "2":
            view_history()
        elif option == "3":
            print("\nClosing chat.\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

if __name__ == "__main__":
    main()