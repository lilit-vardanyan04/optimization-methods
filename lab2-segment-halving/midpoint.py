# midpoint.py
from sympy import symbols, diff

x = symbols('x')
f = (1/4)*x**4 + x**3 - 8*x + 12

# Շարունակում ենք հաշվել առաջին արտադերդիվը
f_prime = diff(f, x)

# Միջակայք և ճշգրտություն
a = 0
b = 2
tolerance = 0.01

while (b - a) > tolerance:
    midpoint = (a + b) / 2
    f_val = float(f_prime.subs(x, midpoint))
    
    if f_val == 0:
        break
    elif f_val > 0:
        b = midpoint
    else:
        a = midpoint

print(f"Approximate extremum at x = {(a + b)/2}")
