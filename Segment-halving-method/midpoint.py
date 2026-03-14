# segment_halving_with_plot.py
import math
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return math.sin(x) + x**2-4*x+3

Min_x = 0
# Սկզբնական միջակայք
a = 0.5
b = 3.5
e = 0.5
t = 0.125

steps_x = []
steps_y = []

while (b - a > e):
  x1 = (a+b-t)/2
  x2 = (a+b+t)/2
  steps_x.append(x1)
  steps_y.append(f(x1))
  steps_x.append(x2)
  steps_y.append(f(x2))
  if (f(x1)> f(x2)):
    a = x1
  else:
    b = x2
else:
  Min_x=(a+b)/2

Min_y = f(Min_x)
print("min=", Min_x)
print("minF",Min_y)

# Գրաֆիկի համար հարթ curve
x_vals = np.linspace(0, 4, 200)
y_vals = [f(x) for x in x_vals]

# Գրաֆիկը
plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label="f(x)", color="blue")

# Նշում ենք min կետը
plt.scatter(Min_x, Min_y, color="red", label=f"Min: ({Min_x:.2f}, {Min_y:.2f})", zorder=5)

# Նշում ենք բոլոր միջանկյալ անցումները
plt.scatter(steps_x, steps_y, color="orange", s=50, alpha=0.6, label="Intermediate points")

plt.title("Function Graph with Segment Halving Steps")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
