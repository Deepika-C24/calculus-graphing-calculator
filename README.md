# calculus-graphing-calculator

## Overview

An educational web application that helps students visualize calculus concepts through interactive graphs. Users can input any mathematical function and instantly see its original form, derivative, and integral plotted together, making abstract concepts tangible and easy to understand.


Calculus can be intimidating for students when they can only see equations on paper. This tool bridges the gap between symbolic math and visual understanding by:
- **Instant Visualization** - See how functions, derivatives, and integrals relate graphically
- **Interactive Learning** - Experiment with different functions in real-time
- **Error-Free Computation** - Symbolic math engine ensures accuracy
- **Accessible Anywhere** - No installation required, works in any browser

### Key Achievements
- **Student-Tested** - Positive feedback on usability and learning effectiveness
- **Real-Time Processing** - Instant computation and graphing
- **Fully Responsive** - Works on desktop, tablet, and mobile
- **Intuitive UI** - Clean interface designed for students

---

## Features

### Core Functionality
- **Symbolic Differentiation** - Compute derivatives of any input function
- **Symbolic Integration** - Calculate indefinite integrals
- **Multi-Function Graphing** - Visualize original, derivative, and integral simultaneously
- **LaTeX Rendering** - Beautiful mathematical notation display
- **Export Options** - Download graphs as PNG images
- **Error Handling** - Clear feedback for invalid inputs

### Supported Functions
- **Polynomials**: `x**2`, `3*x**3 - 2*x + 1`
- **Trigonometric**: `sin(x)`, `cos(x)`, `tan(x)`
- **Exponential**: `exp(x)`, `e**x`
- **Logarithmic**: `log(x)`, `ln(x)`
- **Combined**: `sin(x**2)`, `exp(x)*cos(x)`
- **Rational**: `1/x`, `x/(x**2 + 1)`

---

## Tech Stack

### Core Technologies
- **Python 3.8+** - Main programming language
- **SymPy** - Symbolic mathematics engine for calculus operations
- **NumPy** - Numerical computations and array operations
- **Matplotlib** - Graph generation and visualization
- **MecSimCalc** - Web application framework and hosting platform

### Why These Technologies?

| Technology | Purpose | Why It's Perfect |
|------------|---------|------------------|
| **SymPy** | Symbolic math | Industry-standard for computer algebra |
| **NumPy** | Numerical arrays | Fast, efficient array operations |
| **Matplotlib** | Plotting | Publication-quality graphs |
| **MecSimCalc** | Web framework | Quick deployment, educational focus |

### Try It Now!
**[Launch Application →](https://mecsimcalc.com/app/0362335/integration_and_differentiation_calculator_with_graphs)**

### Example Functions to Try

1. **Simple Polynomial**
   ```
   Input: x**2
   Result: Parabola with straight derivative, cubic integral
   ```

2. **Trigonometric**
   ```
   Input: sin(x)
   Result: Sinusoidal waves showing phase relationships
   ```

3. **Exponential**
   ```
   Input: exp(x)
   Result: All three curves overlap (e^x is its own derivative!)
   ```

4. **Complex Function**
   ```
   Input: x**3 - 3*x**2 + 2*x
   Result: Cubic with quadratic derivative, quartic integral
   ```

---

### Step-by-Step Process

1. **Input Parsing**
   ```python
   expression_str = inputs['input_0']  # Get user input
   expression = sp.sympify(expression_str)  # Parse to SymPy expression
   ```

2. **Symbolic Computation**
   ```python
   derivative = sp.diff(expression, x)  # Compute derivative
   integral = sp.integrate(expression, x)  # Compute integral
   ```

3. **Numerical Conversion**
   ```python
   func = sp.lambdify(x, expression, 'numpy')  # Convert to NumPy function
   ```

4. **Graph Generation**
   ```python
   x_values = np.linspace(-10, 10, 400)  # 400 points for smooth curve
   y_values = func(x_values)  # Evaluate function
   plt.plot(x_values, y_values, label="Original")  # Plot
   ```

---

### Key Design Decisions

1. **400 Data Points**
   - Provides smooth curves without performance issues
   - Balances visual quality with computation speed

2. **Domain [-10, 10]**
   - Captures most function behavior
   - Avoids overflow for exponential functions

3. **Separate Plotting Lines**
   - Color-coded for easy distinction
   - Legend clearly identifies each function

4. **Grid Background**
   - Helps estimate values visually
   - Professional appearance

---

### Learning Outcomes

Students using this calculator develop understanding of:

1. **Relationship Between Functions**
   - How derivatives represent rates of change
   - How integrals represent accumulated area
   - Visual patterns in different function families

2. **Calculus Concepts**
   - Slope vs. function value
   - Critical points (where derivative = 0)
   - Inflection points (where second derivative = 0)

3. **Function Behavior**
   - Increasing vs. decreasing regions
   - Concavity and convexity
   - Asymptotic behavior

### Classroom Applications

- **Homework Verification** - Check if hand calculations are correct
- **Concept Exploration** - Experiment with different function types
- **Visual Learning** - Better for students who struggle with abstract symbols
- **Test Preparation** - Quick reference for function families

---

## Local Development

Want to run this code locally or modify it? Here's how:

### Prerequisites
```bash
python >= 3.8
pip >= 21.0
```

### Installation

1. **Clone or Download Code**
```bash
# Create project folder
mkdir calculus-calculator
cd calculus-calculator
```

2. **Install Dependencies**
```bash
pip install sympy numpy matplotlib
```

3. **Run the Code**

Create `calculator.py`:
```python
# Copy the code from this README's implementation section
# Or use the provided calculator.py file
```

Run it:
```bash
python calculator.py
```

### Example Usage

```python
from calculator import calculate_and_plot

# Calculate for x^2
derivative, integral, plot = calculate_and_plot("x**2")

print(f"Derivative: {derivative}")  # Output: 2*x
print(f"Integral: {integral}")      # Output: x**3/3
plot.show()  # Display graph
```
---

## What I Learned

### Technical Skills
- **Symbolic Mathematics** - Deeped dive into SymPy for computer algebra
- **Numerical Methods** - NumPy for efficient array operations
- **Data Visualization** - Matplotlib for scientific plotting
- **Web Deployment** - MecSimCalc platform integration
- **Error Handling** - Robust input validation and edge case management

### Mathematical Insights
- **Derivative Patterns** - How derivatives reveal function behavior
- **Integration Challenges** - Not all functions have closed-form integrals
- **Function Families** - Common patterns in polynomial, trig, and exponential functions

### Soft Skills
- **User-Centered Design** - Iterated based on student feedback
- **Technical Communication** - Explained calculus concepts clearly
- **Time Management** - Delivered working MVP within hackathon deadline
- **Teaching** - Helped 20+ students understand calculus visually
---

## Contributing

This is an educational project, but contributions are welcome!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly with various functions
5. Submit a pull request

### Areas for Contribution
- **More Examples** - Add interesting function examples
- **Documentation** - Improve explanations and guides
- **Bug Fixes** - Report or fix edge cases
- **Features** - Implement planned enhancements
- **Testing** - Add unit/integration tests

---

This project is free to use for educational purposes.

---

## Author
*Deepika Chandrashekhar*

•⁠  ⁠GitHub: [@Deepika-C24](https://github.com/Deepika-C24)
•⁠  ⁠LinkedIn: [deepika-chandrashekhar](https://www.linkedin.com/in/deepika-chandrashekhar/)
•⁠  ⁠Email: dchandr1@ualberta.ca
---
## Resources

### Learn More About the Technologies
- [SymPy Documentation](https://docs.sympy.org/)
- [NumPy User Guide](https://numpy.org/doc/stable/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [MecSimCalc Platform](https://mecsimcalc.com/)

### Calculus Learning Resources
- [Khan Academy - Calculus](https://www.khanacademy.org/math/calculus-1)
- [MIT OpenCourseWare - Single Variable Calculus](https://ocw.mit.edu/courses/mathematics/)
- [Paul's Online Math Notes](http://tutorial.math.lamar.edu/)
