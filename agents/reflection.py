from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)


def reflection(answer):

    prompt = f"""

Improve this recommendation.

Make it:

- Professional
- Clear
- Easy to read
- Bullet points


Recommendation:

{answer}

Return only improved recommendation.

"""


    response = llm.invoke(prompt)

    return response.content