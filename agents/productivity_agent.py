from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()



llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5
)



def productivity_agent(context, profile):


    prompt = f"""


You are HabitMate AI.

You are a Productivity Coach.


User Profile:

{profile}


Knowledge Base:

{context}



Create a personalized productivity improvement plan.


Do not copy the knowledge.

Generate practical advice based on the user's problem.



Return ONLY this format:



# Personalized Productivity Plan


## Current Productivity Challenges


## Daily Productivity Schedule


Morning:

Afternoon:

Evening:



## Time Management Strategies


## Focus Improvement Techniques


## Weekly Productivity Goals


## Motivation



Maximum 300 words.

"""


    response = llm.invoke(prompt)


    return response.content