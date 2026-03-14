from sympy import symbols, diff
import matplotlib.pyplot as plt

x = symbols('x')
f = (1/4)*x**4 + x**3 - 8*x + 12

f_acancjal = diff(f, x)
print(f_acancjal)

a = 0
b = 2
e = 0.5

n = int((b - a) / e)
print(n)

x_list = []
y_list = []

for i in range(1, n + 1):
    x1 = a + i * ((b - a) / n)
    f_arjeq = float(f.subs(x, x1))   
    x_list.append(x1)
    y_list.append(f_arjeq)

plt.figure(figsize=(8,5))
plt.plot(x_list, y_list, marker='o', color='blue')
plt.title("Ֆունկցիայի գրաֆիկ")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
