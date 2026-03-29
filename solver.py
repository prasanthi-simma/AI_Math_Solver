from sympy import symbols, Eq, sympify, solve, simplify
from transformers import pipeline

# Load AI model
generator = pipeline("text-generation", model="gpt2")

def solve_expression(expr):
    try:
        if "=" in expr:
            x = symbols('x')
            left, right = expr.split("=")
            equation = Eq(sympify(left), sympify(right))
            result = solve(equation, x)
            return result
        else:
            return simplify(sympify(expr))
    except:
        return "Invalid input"


def explain_solution(problem):
    try:
        prompt = f"Explain step by step: {problem}"
        explanation = generator(prompt, max_length=100, num_return_sequences=1)
        return explanation[0]['generated_text']
    except:
        return "Explanation not available"