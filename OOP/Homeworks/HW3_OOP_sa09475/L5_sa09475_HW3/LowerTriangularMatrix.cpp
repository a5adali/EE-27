#include "LowerTriangularMatrix.hpp"

// constructor that creates a lower triangular square matrix
LowerTriangularMatrix::LowerTriangularMatrix(const int size) {
    rows = size;
    cols = size;

    // number of values stored in a lower triangular matrix
    int total = (size * (size + 1)) / 2;

    elements = std::vector<double>(total, 0.0);
}

// copy constructor using the parent class
LowerTriangularMatrix::LowerTriangularMatrix(const LowerTriangularMatrix& other)
    : SquareMatrix(other) {}

// sets a value only if it's in or below the diagonal
void LowerTriangularMatrix::setElement(const int row, const int col, const double value) {
    if (row >= col) {
        int index = (row * (row + 1)) / 2 + col;
        elements[index] = value;
    }
}

// returns the value at (row, col)
double LowerTriangularMatrix::getElement(const int row, const int col) const {
    // above the diagonal everything is zero
    if (row < col) {
        return 0.0;
    }

    int index = (row * (row + 1)) / 2 + col;
    return elements[index];
}

// adds two lower triangular matrices
LowerTriangularMatrix LowerTriangularMatrix::operator+(const LowerTriangularMatrix& other) const {
    LowerTriangularMatrix result(rows);

    for (int i = 0; i < (int)elements.size(); i++) {
        result.elements[i] = elements[i] + other.elements[i];
    }

    return result;
}

// subtracts two lower triangular matrices
LowerTriangularMatrix LowerTriangularMatrix::operator-(const LowerTriangularMatrix& other) const {
    LowerTriangularMatrix result(rows);

    for (int i = 0; i < (int)elements.size(); i++) {
        result.elements[i] = elements[i] - other.elements[i];
    }

    return result;
}

// multiplies two lower triangular matrices
LowerTriangularMatrix LowerTriangularMatrix::operator*(const LowerTriangularMatrix& other) const {
    LowerTriangularMatrix result(rows);

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c <= r; c++) {
            double sum = 0.0;

            for (int k = 0; k <= r; k++) {
                sum += getElement(r, k) * other.getElement(k, c);
            }

            result.setElement(r, c, sum);
        }
    }

    return result;
}

// checks equality using the parent class
bool LowerTriangularMatrix::operator==(const LowerTriangularMatrix& other) const {
    return SquareMatrix::operator==(other);
}
