
import numpy as np

print("========== NUMPY COMPLETE PRACTICE ==========")

# 1. Import and Version
print("\n1. NUMPY VERSION")
print(np.__version__)


# 2. Array Creation
print("\n2. ARRAY CREATION")

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

sequence = np.arange(1, 11)
print("Arange:", sequence)

linear = np.linspace(1, 100, 5)
print("Linspace:", linear)

zeros = np.zeros((2, 3))
print("Zeros:\n", zeros)

ones = np.ones((2, 3))
print("Ones:\n", ones)

full = np.full((2, 2), 7)
print("Full:\n", full)

identity = np.eye(3)
print("Identity:\n", identity)


# 3. Array Properties
print("\n3. ARRAY PROPERTIES")

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Item Size:", arr.itemsize)
print("Memory:", arr.nbytes)


# 4. Multidimensional Arrays
print("\n4. MULTIDIMENSIONAL ARRAYS")

two_d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

three_d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print("2D Array:\n", two_d)
print("3D Array:\n", three_d)


# 5. Indexing and Slicing
print("\n5. INDEXING AND SLICING")

print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("Slice:", arr[1:4])
print("Every Second Element:", arr[::2])

print("First Row:", two_d[0])
print("Second Column:", two_d[:, 1])


# 6. Reshaping
print("\n6. RESHAPING")

numbers = np.arange(1, 13)

print("Original:", numbers)
print("Reshape 3x4:\n", numbers.reshape(3, 4))
print("Flatten:", two_d.flatten())
print("Transpose:\n", two_d.T)
print("Expand Dimensions:", np.expand_dims(arr, axis=0).shape)
print("Squeeze:", np.squeeze(np.array([[10, 20, 30]])).shape)


# 7. Mathematical Operations
print("\n7. MATHEMATICAL OPERATIONS")

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", np.add(a, b))
print("Subtraction:", np.subtract(a, b))
print("Multiplication:", np.multiply(a, b))
print("Division:", np.divide(a, b))
print("Power:", np.power(a, 2))
print("Square Root:", np.sqrt(a))
print("Absolute:", np.abs([-10, 20, -30]))
print("Round:", np.round([10.456, 20.789], 2))


# 8. Statistical Operations
print("\n8. STATISTICAL OPERATIONS")

marks = np.array([50, 60, 70, 80, 90])

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))
print("75th Percentile:", np.percentile(marks, 75))
print("Cumulative Sum:", np.cumsum(marks))
print("Product:", np.prod(marks))
print("Range:", np.ptp(marks))
print("Average:", np.average(marks))


# 9. Sorting and Unique Values
print("\n9. SORTING AND SEARCHING")

values = np.array([40, 10, 30, 20, 10])

print("Sorted:", np.sort(values))
print("Unique:", np.unique(values))
print("Sorted Indices:", np.argsort(values))
print("Maximum Index:", np.argmax(values))
print("Minimum Index:", np.argmin(values))
print("Where:", np.where(values > 20))


# 10. Conditional Operations
print("\n10. CONDITIONAL OPERATIONS")

scores = np.array([30, 45, 60, 75, 90])

print("Pass/Fail:", np.where(scores >= 60, "Pass", "Fail"))
print("Any above 80:", np.any(scores > 80))
print("All above 20:", np.all(scores > 20))
print("Clipped:", np.clip(scores, 40, 80))


# 11. Array Joining and Splitting
print("\n11. JOINING AND SPLITTING")

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Concatenate:", np.concatenate((x, y)))
print("Stack:\n", np.stack((x, y)))
print("Horizontal Stack:", np.hstack((x, y)))
print("Vertical Stack:\n", np.vstack((x, y)))
print("Split:", np.split(np.array([1, 2, 3, 4]), 2))


# 12. Data Type Conversion
print("\n12. DATA TYPE CONVERSION")

float_arr = np.array([10.5, 20.5, 30.5])
int_arr = float_arr.astype(int)

print("Float Array:", float_arr)
print("Integer Array:", int_arr)
print("New Data Type:", int_arr.dtype)


# 13. Random Numbers
print("\n13. RANDOM NUMBERS")

rng = np.random.default_rng(42)

print("Random Float:", rng.random(5))
print("Random Integers:", rng.integers(1, 100, size=5))
print("Random Choice:", rng.choice([10, 20, 30, 40]))
print("Normal Distribution:", rng.normal(0, 1, size=5))


# 14. Missing and Invalid Values
print("\n14. MISSING VALUES")

missing = np.array([10, 20, np.nan, 40, 50])

print("NaN Check:", np.isnan(missing))
print("NaN Mean:", np.nanmean(missing))
print("NaN Sum:", np.nansum(missing))
print("Replace NaN:", np.nan_to_num(missing, nan=0))

print("Infinite Check:", np.isinf([10, np.inf, 20]))
print("Finite Check:", np.isfinite([10, np.inf, 20]))


# 15. Linear Algebra
print("\n15. LINEAR ALGEBRA")

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("Dot Product:\n", np.dot(matrix_a, matrix_b))
print("Matrix Multiplication:\n", np.matmul(matrix_a, matrix_b))
print("Determinant:", np.linalg.det(matrix_a))
print("Inverse:\n", np.linalg.inv(matrix_a))
print("Matrix Rank:", np.linalg.matrix_rank(matrix_a))
print("Norm:", np.linalg.norm(matrix_a))


# 16. Correlation and Covariance
print("\n16. CORRELATION AND COVARIANCE")

height = np.array([150, 160, 170, 180, 190])
weight = np.array([50, 55, 65, 75, 85])

print("Correlation:\n", np.corrcoef(height, weight))
print("Covariance:\n", np.cov(height, weight))


# 17. Employee Salary Mini Project
print("\n17. EMPLOYEE SALARY ANALYSIS")

salary = np.array([25000, 30000, 35000, 40000, 45000, 50000])

print("Total Salary:", np.sum(salary))
print("Average Salary:", np.mean(salary))
print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))
print("Salary Above 35000:", salary[salary > 35000])
print("10% Salary Increment:", salary * 1.10)

print("\n========== PROGRAM COMPLETED ==========")
