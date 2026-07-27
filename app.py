import streamlit as st

#st.caption("Built using Streamlit + LangGraph + ChromaDB")
from agents.analyzer import analyze_profile
from agents.router import route_agent

from rag.retriever import retrieve_information

from agents.habit_agent import habit_agent
from agents.productivity_agent import productivity_agent

from agents.reflection import reflection



# Title
st.title("🌱 HabitMate AI ")


# User Types
user_type = st.selectbox(
    "Select User Type",
    [
        "University Student",
        "Office Worker",
        "Busy Professional"
    ]
)


# Goals
goal = st.text_input(
    "Your Goal"
)


# Problem
problem = st.text_area(
    "Your Problem"
)



# Button
if st.button("Generate Plan"):

    try:

        # 1. Analyze User Profile
        

        profile = analyze_profile(
            user_type,
            goal,
            problem
        )

        



        # 2. Select Agent
        st.info("Selecting AI Agent...")

        agent = route_agent(problem)

        st.write(
            "Selected Agent:",
            agent
        )



        # 3. Retrieve Knowledge
        st.info("Searching Knowledge Base...")

        context = retrieve_information(
            problem
        )

        


                # 4. Generate Recommendation

        if agent == "habit":

            answer = habit_agent(
                context,
                profile
            )


        elif agent == "productivity":

            answer = productivity_agent(
                context,
                profile
            )


        else:

            answer = productivity_agent(
                context,
                profile
            )


        # 5. Reflection Agent

        st.info("Improving recommendation...")

        final_answer = reflection(
            answer
        )


        # Final Output

        st.success(
            "Your Personalized Plan"
        )

        st.write(
            final_answer
        )


    except Exception as e:

        st.error(
            "System Error:"
        )

        st.write(e)