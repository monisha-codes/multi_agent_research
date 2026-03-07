import streamlit as st
import requests

st.title("Multi-Agent Research Assistant")

question = st.text_input("Ask a question:")

if st.button("Submit"):

    response = requests.post(
        "http://localhost:8000/api/ask/",
        json={"question": question}
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)
    data = response.json()

    st.subheader("Planner Decision")
    st.write(data["planner_output"])

    st.subheader("Research Result")
    st.write(data["research_output"])

    st.subheader("Final Answer")
    st.success(data["final_answer"])