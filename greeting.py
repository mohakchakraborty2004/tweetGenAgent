import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key =OPENAI_API_KEY,
    model = "gpt-3.5-turbo",
    temperature = 0.7
             )

prompt = ChatPromptTemplate.from_template(
     "You are a productivity coach. Given the following completed tasks, generate a short and engaging tweet summarizing them:\n\nTasks: {tasks}\n\nTweet:"
)

def gen_tweet(data): 
    tasks_str = ", ".join(data.tasks) #converting the list into string

    tweet = llm.invoke(prompt.format(tasks = tasks_str))

    return f"tweet : {tweet.content}"