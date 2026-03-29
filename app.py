import streamlit as st
from solver import solve_expression, explain_solution

st.title("🧠 AI Math Solver")

user_input = st.text_input("Enter problem:")

if st.button("Solve"):
    result = solve_expression(user_input)
    explanation = explain_solution(user_input)

    st.success(f"Answer: {result}")
    st.info(f"Explanation: {explanation}")