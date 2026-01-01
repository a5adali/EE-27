#include "SquareMatrix.hpp"

// constructor that makes a square matrix of given size
SquareMatrix::SquareMatrix(const int size) 
    : Matrix(size, size) {}

// copy constructor
SquareMatrix::SquareMatrix(const SquareMatrix& other) 
    : Matrix(other) {}

// get element at (row, col)
double SquareMatrix::getElement(const int row, const int col) const {
    return Matrix::getElement(row, col);
}

// set element at (row, col)
void SquareMatrix::setElement(const int row, const int col, const double value) {
    Matrix::setElement(row, col, value);
}

// multiply two square matrices
SquareMatrix SquareMatrix::operator*(const SquareMatrix& other) const {
    SquareMatrix result(rows);

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            double sum = 0.0;

            for (int k = 0; k < cols; k++) {
                sum += getElement(r, k) * other.getElement(k, c);
            }

            result.setElement(r, c, sum);
        }
    }

    return result;
}

// add two square matrices
SquareMatrix SquareMatrix::operator+(const SquareMatrix& other) const {
    SquareMatrix result(rows);

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            result.setElement(r, c, getElement(r, c) + other.getElement(r, c));
        }
    }

    return result;
}

// subtract two square matrices
SquareMatrix SquareMatrix::operator-(const SquareMatrix& other) const {
    SquareMatrix result(rows);

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            result.setElement(r, c, getElement(r, c) - other.getElement(r, c));
        }
    }

    return result;
}

// check if two square matrices are equal
bool SquareMatrix::operator==(const SquareMatrix& other) const {
    return Matrix::operator==(other);
}
