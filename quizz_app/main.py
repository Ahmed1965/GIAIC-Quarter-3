import streamlit as st
import random
import time
import streamlit.components.v1 as components
from Question_answer import questions

# Banner for main page
banner_HTML = """
<div style="background-color: #f0f2f5; padding: 20px; text-align: center;">
<h1 style="color: #333;">Welcome to the Quiz Application</h1>
<p style="color: #555;">Test your knowledge about Pakistan</p>
<p style="color: #777;">Answer the questions below to see how much you know!</p>

</div>


"""
components.html(banner_HTML, height=200)

st.session_state.question = questions
def show_question():
    # Display the question and options
    for i, q in enumerate(st.session_state.question):
        st.write(f"**Question {i + 1}:** {q['question']}")
        selected_option = st.radio(
            f"Options for Question {i + 1}",
            q["options"],
            key=f"option_{i}",
        )
        if st.button("Submit", key=f"submit_{i}"):
            if selected_option == q["answer"]:
                st.success("Correct!")
            else:
                st.error(f"Wrong! The correct answer is: {q['answer']}")
            time.sleep(5)
            random_question=random.random()
            random_question = f"{q['question']}"          
            #break
        
show_question()