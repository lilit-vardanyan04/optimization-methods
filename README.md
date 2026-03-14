# Optimization Methods

This repository contains implementations and explanations of several **optimization methods** used to find the **minimum or maximum of functions**.

---

# Choice Method

## Theoretical Background

The **Choice Method** is used to analyze a function and find approximate points where the function may reach **minimum or maximum values (min/max)**.

* This method is useful when the function is known in **analytical form**.
* The function is evaluated at several points in the interval `[a, b]` with a step `e`.
* By checking these values, we can estimate where the function increases or decreases.
* This approach helps obtain **approximate solutions** and visualize the behavior of the function.

## Files

* `choice.py` – Python code that calculates the function values and displays the graph.
* `README.md` – Project description.

## Code Description

The program performs the following steps:

1. Uses the `sympy` library to compute the **first derivative** of the function.
2. Calculates the function values in the interval from `a` to `b` with step `e`.
3. Stores the results in lists (`x_list`, `y_list`).
4. Uses the `matplotlib` library to plot the function graph.

---

# Segment Halving Method

## Theoretical Background

The **Segment Halving Method** (also known as the **Midpoint Method**) is a numerical optimization technique used to find the **minimum or maximum value of a function**.

* The method starts with an interval `[a, b]`.
* The interval is divided into smaller parts.
* The function values or derivative signs are analyzed to determine which part of the interval contains the optimum.
* The interval is repeatedly reduced until the required **precision** is reached.

## Files

* `midpoint.py` – Python implementation of the Segment Halving Method.
* `README.md` – Project description.

---

# Golden Section Method

## Theoretical Background

The **Golden Section Method** is a numerical optimization algorithm used to find the **minimum or maximum of a unimodal function** in a given interval.

* The method is based on the **golden ratio**, which allows the interval to shrink efficiently.
* Two internal points are chosen inside the interval.
* The function values at these points are compared.
* Part of the interval that cannot contain the optimum is removed.
* The process continues until the interval becomes sufficiently small.

The golden ratio is defined as:

[
\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618
]

Using this ratio reduces the number of function evaluations and makes the method efficient.

## Files

* `golden_section.py` – Python implementation of the Golden Section Method.
* `README.md` – Project description.

---

# How to Run the Code

1. Download or clone the repository.
2. Install the required libraries:

```bash
pip install sympy
pip install matplotlib
```

3. Run the desired Python file, for example:

```bash
python choice.py
```

