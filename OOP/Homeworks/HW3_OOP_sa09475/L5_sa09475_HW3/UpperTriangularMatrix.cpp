#include "UpperTriangularMatrix.hpp"

// constructor that makes a square upper triangular matrix
UpperTriangularMatrix::UpperTriangularMatrix(const int size) {
    rows = size;
    cols = size;

    // number of elements stored in upper triangular
    int total = (size * (size + 1)) / 2;

    elements = std::vector<double>(total, 0.0);
}

// copy constructor using the parent class
UpperTriangularMatrix::UpperTriangularMatrix(const UpperTriangularMatrix& other)
    : SquareMatrix(other) {}

// get element at (row, col)
double UpperTriangularMatrix::getElement(const int row, const int col) const {
    // return 0 if below diagonal
    if (row > col) {
        return 0.0;
    }

    // compute index in the 1d vector
    int index = col + row * cols - (row * (row + 1)) / 2;
    return elements[index];
}

// set element at (row, col) only if above or on diagonal
void UpperTriangularMatrix::setElement(const int row, const int col, const double value) {
    if (row <= col) {
        int index = col + row * cols - (row * (row + 1)) / 2;
        elements[index] = value;
    }
}

// add two upper triangular matrices
UpperTriangularMatrix UpperTriangularMatrix::operator+(const UpperTriangularMatrix& other) const {
    UpperTriangularMatrix result(rows);

    for (int i = 0; i < (int)elements.size(); i++) {
        result.elements[i] = elements[i] + other.elements[i];
    }

    return result;
}

// subtract two upper triangular matrices
UpperTriangularMatrix UpperTriangularMatrix::operator-(const UpperTriangularMatrix& other) const {
    UpperTriangularMatrix result(rows);

    for (int i = 0; i < (int)elements.size(); i++) {
        result.elements[i] = elements[i] - other.elements[i];
    }

    return result;
}

// multiply two upper triangular matrices
UpperTriangularMatrix UpperTriangularMatrix::operator*(const UpperTriangularMatrix& other) const {
    UpperTriangularMatrix result(rows);

    for (int r = 0; r < rows; r++) {
        for (int c = r; c < cols; c++) { // only calculate for elements on/above diagonal
            double sum = 0.0;

            for (int k = r; k <= c; k++) {
                sum += getElement(r, k) * other.getElement(k, c);
            }

            result.setElement(r, c, sum);
        }
    }

    return result;
}

// check if two upper triangular matrices are equal
bool UpperTriangularMatrix::operator==(const UpperTriangularMatrix& other) const {
    return SquareMatrix::operator==(other);
}
