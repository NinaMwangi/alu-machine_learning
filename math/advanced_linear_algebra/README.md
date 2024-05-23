Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General

What is a determinant? How would you calculate it?
What is a minor, cofactor, adjugate? How would calculate them?
What is an inverse? How would you calculate it?
What are eigenvalues and eigenvectors? How would you calculate them?
What is definiteness of a matrix? How would you determine a matrix’s definiteness?

0. Determinant
mandatory
Write a function def determinant(matrix): that calculates the determinant of a matrix:

matrix is a list of lists whose determinant should be calculated
If matrix is not a list of lists, raise a TypeError with the message matrix must be a list of lists
If matrix is not square, raise a ValueError with the message matrix must be a square matrix
The list [[]] represents a 0x0 matrix
Returns: the determinant of matrix
