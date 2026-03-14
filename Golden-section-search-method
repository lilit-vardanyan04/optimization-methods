import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # return math.sin(x) + x**2 - 4*x + 3
    return 1/4*x**4+x**2-8*x+12

a = 0
b = 2
e = 0.1
step = 1

# Ֆիքսված առանցքների սահմանները
x_min_plot = -1
x_max_plot = 3
y_min_plot = -2
y_max_plot = 5

while b - a > e:
    x1 = a + 0.3819*(b - a)
    x2 = a + 0.6180*(b - a)

    f1 = f(x1)
    f2 = f(x2)

    # գրաֆիկի կառուցում
    x_vals = np.linspace(x_min_plot, x_max_plot, 200)
    y_vals = [f(x) for x in x_vals]

    plt.figure()
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axvline(a, color='green', linestyle='--', label='a')
    plt.axvline(b, color='red', linestyle='--', label='b')
    plt.scatter([x1, x2], [f1, f2], color='orange', label='x1,x2')

    plt.title(f"Քայլ {step}  [a={a:.3f}, b={b:.3f}]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.xlim(x_min_plot, x_max_plot)
    plt.ylim(y_min_plot, y_max_plot)
    plt.legend()
    plt.show()

    if f1 > f2:
        a = x1
    else:
        b = x2

    step += 1

x_min = (a + b)/2
print(f"X_min = {x_min}")
print(f"F_min = {f(x_min)}")
