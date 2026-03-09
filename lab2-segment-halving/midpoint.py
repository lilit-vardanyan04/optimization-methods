# segment_halving_with_plot.py
import matplotlib.pyplot as plt

# Ֆունկցիան (կարող է փոխվել ցանկացածի)
def f(x):
    return (1/4)*x**4 + x**3 - 8*x + 12

# Սկզբնական միջակայք
a = 0
b = 2
tolerance = 0.01   # Ճշգրտության շեմ

# x և y արժեքների ցուցակ՝ գրաֆիկի համար
x_list = []
y_list = []

x_list.append(a)
x_list.append(b)
y_list.append(f(a))
y_list.append(f(b))

# Հատվածի կիսման մեթոդ
while (b - a) > tolerance:
    m = (a + b) / 2
    x_list.append(m)
    y_list.append(f(m))
    
    if f(a) < f(b):
        b = m
    else:
        a = m

x_min = (a + b) / 2
y_min = f(x_min)

print(f"Approximate minimum at x = {x_min}, f(x) = {y_min}")

# Գրաֆիկի կառուցում
plt.figure(figsize=(8,5))
plt.plot(x_list, y_list, marker='o', color='blue', linestyle='-')
plt.title("Ֆունկցիայի գրաֆիկը (Segment Halving Method)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
