import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0.5
)




def habit_agent(context, profile):


    prompt = f"""

You are HabitMate AI.

You are a Habit Improvement Coach.


User Profile:

{profile}


Knowledge Base:

{context}


Create a personalized habit improvement plan.

Do not copy the knowledge directly.

Use the user information.


Return ONLY this format:


# Personalized Habit Improvement Plan


## Current Habit Challenges


## Daily Healthy Routine

Morning:

Afternoon:

Evening:


## Habit Building Strategies


## Habit Tracking Method


## Weekly Habit Goals


## Motivation


Maximum 300 words.

"""


    response = llm.invoke(prompt)


    return response.content