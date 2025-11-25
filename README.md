# 🌟 Turtle Geometric Star Pattern

A visual **Python Graphics Script** utilizing the `turtle` module to draw a complex geometric star pattern. By repeating a high-angle turn ($170^\circ$) over 36 iterations, the program creates a symmetrical, spirograph-style design.



## 🚀 Features

* **Geometric Precision:** Draws a 36-point star using precise angle calculations.
* **High-Speed Rendering:** Sets `turtle.speed(30)` for rapid visualization.
* **Symmetrical Layout:** Starts from a calculated offset (`x=-200`) to center the large design on the canvas.
* **Minimalist Code:** Achieves a complex visual result with a simple `for` loop.

## 🛠️ Logic Explained

The script creates the pattern using the following parameters:

| Variable | Value | Effect |
| :--- | :--- | :--- |
| **`n`** | `36` | The total number of lines/iterations drawn. |
| **`length`** | `400` | The length of each individual line. |
| **Angle** | `170` | The turtle turns left by $170^\circ$ after every line. Because 170 is not a divisor of 360, the lines cross over each other, creating a dense star rather than a simple polygon. |

## 💻 How to Run

### 1. Prerequisites
Ensure you have Python installed. The `turtle` library is a standard library included with Python, so no extra installation is required.

### 2. Run the Script
Open your terminal or command prompt and run:

```bash
Spiral-Lines.py
```

### 3. Output
A window will pop up and immediately begin drawing the star pattern from the left side of the screen towards the right.

## 📝 Example Code Snippet
The core logic driving the drawing is:
```text
for i in range(36):
    turtle.forward(400)
    turtle.left(170)
```

## ⚠️ Requirements
* **Python 3.x**
* **Tkinter support** (Usually installed automatically with Python).
