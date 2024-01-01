# # metric space
# # normed space
# # inner product space


# Metric Space:

# A metric space is a set equipped with a metric, a function that measures the distance between pairs of elements in the set.
# Formally, a metric space is defined as a pair (X, d), where X is a set, and d is a metric on X. The metric satisfies:

# Non-negativity: The distance, d(x, y), is always greater than or equal to 0, and d(x, y) equals 0 only if x equals y.
# Symmetry: The distance from x to y is the same as the distance from y to x.
# Triangle Inequality: The distance from x to z is less than or equal to the sum of the distances from x to y and y to z.
# Example of Metric Space:
# Consider the set of real numbers (X = ℝ) with the metric d(x, y) = |x - y|.


# Normed Space:

# A normed space is a vector space equipped with a norm, a function that assigns a non-negative scalar to each vector.
# Formally, a normed space is a pair (V, ||⋅||), where V is a vector space and ||⋅|| is a norm on V. The norm satisfies:

# Non-negativity: The norm of a vector, ||u||, is always greater than or equal to 0, and ||u|| equals 0 only if u is the zero vector.
# Homogeneity: The norm of a scaled vector, ||cu||, is equal to the absolute value of c multiplied by the norm of u.
# Triangle Inequality: The norm of the sum of two vectors, ||u + v||, is less than or equal to the sum of their individual norms.
# Example of Normed Space:
# Consider the vector space of real-valued continuous functions on the interval [a, b) denoted as C([a, b)).
# The norm can be defined as the maximum absolute value of the function over the interval.


# Inner Product Space:

# An inner product space is a vector space equipped with an inner product, a function that associates a scalar to each pair of vectors.
# Formally, an inner product space is a pair (V, ⟨⋅, ⋅⟩), where V is a vector space and ⟨⋅, ⋅⟩ is an inner product on V. The inner product satisfies:

# Linearity in the First Variable: The inner product of a scaled vector and another vector, ⟨cu, v⟩, is equal to c times the inner product of u and v.
# Conjugate Symmetry: The inner product of vectors u and v, ⟨u, v⟩, is equal to the complex conjugate of the inner product of v and u.
# Positive Definiteness: The inner product of a vector with itself, ⟨u, u⟩, is always greater than or equal to 0, and ⟨u, u⟩ equals 0 only if u is the zero vector.
# Example of Inner Product Space:
# Consider the vector space ℝ^n with the standard dot product as the inner product.
  

# In summary, a metric space focuses on distance, a normed space introduces the concept of vector length, and an inner product space includes the notion of angles between vectors.
# Each concept builds upon the previous one, providing increasingly rich structures for studying mathematical spaces.
