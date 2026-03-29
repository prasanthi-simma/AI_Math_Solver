from sympy import symbols, Eq, sympify, solve, simplify

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
    if "=" in problem:
        return "Rearrange the equation and isolate x step by step."
    else:
        return "Follow order of operations (BODMAS) to simplify the expression."