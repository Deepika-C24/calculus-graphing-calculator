"""
Calculus Graphing Calculator - Core Logic
Computes derivatives, integrals, and generates graphs for mathematical functions
"""

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def main(inputs):
    """
    Main calculation function for MecSimCalc integration
    
    Args:
        inputs: Dictionary containing 'input_0' with the function string
        
    Returns:
        Dictionary with computed derivative, integral, and plot
    """
    # Get the user input for the function
    expression_str = inputs['input_0']

    # Define the variable and the function
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)

    # Calculate derivative and integral
    derivative = sp.diff(expression, x)
    integral = sp.integrate(expression, x)

    # Convert the expressions to Python functions
    func = sp.lambdify(x, expression, 'numpy')
    deriv_func = sp.lambdify(x, derivative, 'numpy')
    integral_func = sp.lambdify(x, integral, 'numpy')

    # Generate x values for plotting
    x_values = np.linspace(-10, 10, 400)

    # Evaluate the functions for the given x values
    y_values = func(x_values)
    deriv_values = deriv_func(x_values)
    integral_values = integral_func(x_values)

    # Plot the functions
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="Original Function f(x)")
    plt.plot(x_values, deriv_values, label="Derivative f'(x)")
    plt.plot(x_values, integral_values, label="Integral ∫f(x)dx")
    
    # Add labels and legend
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Function, Derivative, and Integral")
    plt.legend()
    plt.grid(True)
    
    return expression, derivative, integral, plt


def standalone_calculation(expression_str):
    """
    Standalone version for local testing without MecSimCalc
    
    Args:
        expression_str: String representation of the function
        
    Returns:
        Tuple of (original_expr, derivative, integral, matplotlib_figure)
        
    Example:
        >>> expr, deriv, integ, plot = standalone_calculation("x**2")
        >>> print(f"Derivative: {deriv}")
        Derivative: 2*x
    """
    # Wrap input to match MecSimCalc format
    inputs = {'input_0': expression_str}
    return main(inputs)


if __name__ == "__main__":
    # Example usage for local testing
    test_functions = [
        "x**2",
        "sin(x)",
        "exp(x)",
        "x**3 - 3*x**2 + 2*x"
    ]
    
    print("Calculus Calculator - Testing")
    print("=" * 50)
    
    for func in test_functions:
        print(f"\nFunction: {func}")
        try:
            expr, deriv, integ, plot = standalone_calculation(func)
            print(f"  Derivative: {deriv}")
            print(f"  Integral:   {integ}")
            print("  ✓ Success")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("\n" + "=" * 50)
    print("All tests complete!")