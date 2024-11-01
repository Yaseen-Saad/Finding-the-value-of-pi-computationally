# Estimating the Value of π Using a Monte Carlo Simulation

This project uses a Monte Carlo simulation to estimate the value of π. Monte Carlo methods are based on random sampling and are useful for solving problems that might be deterministic in principle but complex to solve analytically. By sampling random points and determining whether they fall inside a unit circle, we can approximate π.

## Methodology

The idea behind the Monte Carlo method for estimating π is to inscribe a circle within a square. Given that the area of the unit circle (radius \( r = 1 \)) is \( π \), and the area of the square enclosing this circle (side length \( 2 \)) is \( 4 \), we can derive an approximation for π by comparing the number of random points that fall within the circle to the total number of points.

### Derivation

1. **Area of Circle**:  
   \[
   A_{\text{circle}} = πr^2 = π \cdot (1)^2 = π
   \]

2. **Area of Square**:
   \[
   A_{\text{square}} = (2r)^2 = 4
   \]

3. **Probability Derivation**:
   When we randomly select points within the square, the probability of a point landing inside the circle is the ratio of the area of the circle to the area of the square:
   \[
   P(\text{inside circle}) = \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{π}{4}
   \]
   Rearranging this, we can express π as:
   \[
   π \approx 4 \cdot \frac{\text{Number of points inside circle}}{\text{Total number of points}}
   \]

By generating a large number of random points within the square and counting how many fall inside the circle, we can estimate the value of π using:
\[
π \approx 4 \cdot \frac{\text{points\_hit}}{\text{total\_points}}
\]

## Code Explanation

The code performs the following steps to compute the value of π:

1. **Define a Function to Check If a Point is Inside the Circle**:
   ```python
   def does_hit(x, y):
       return x**2 + y**2 <= 1
