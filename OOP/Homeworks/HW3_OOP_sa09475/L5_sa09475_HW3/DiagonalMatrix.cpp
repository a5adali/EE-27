#include "DiagonalMatrix.hpp"

// constructor that makes a square diagonal matrix
DiagonalMatrix::DiagonalMatrix(const int size) {
    rows = size;
    cols = size;
    elements = std::vector<double>(size, 0.0);
}

// copy constructor uses the squarematrix copy logic
DiagonalMatrix::DiagonalMatrix(const DiagonalMatrix& other)
    : SquareMatrix(other) {}

// returns the value at (row, col)
double DiagonalMatrix::getElement(const int row, const int col) const {
    if (row == col) {
        return elements[row];
    }
    return 0.0;
}

// sets a value only if it's on the diagonal
void DiagonalMatrix::setElement(const int row, const int col, const double value) {
    if (row == col) {
        elements[row] = value;
    }
}

// adds two diagonal matrices
DiagonalMatrix DiagonalMatrix::operator+(const DiagonalMatrix& other) const {
    DiagonalMatrix result(rows);

    for (int i = 0; i < (int)elements.size(); i++) {
        result.elements[i] = elements[i] + other.elements[i];
    }

    return result;
}

// subtracts two diagonal matrices
DiagonalMatrix DiagonalMatrix::operator-(const DiagonalMatrix& other) const {
    DiagonalMatrix result(rows);

    for (int i = 0; i < (int)elements.size(); i++) {
        result.elements[i] = elements[i] - other.elements[i];
    }

    return result;
}

// multiplies two diagonal matrices (element-wise)
DiagonalMatrix DiagonalMatrix::operator*(const DiagonalMatrix& other) const {
    DiagonalMatrix result(rows);

    for (int i = 0; i < rows; i++) {
        result.elements[i] = elements[i] * other.elements[i];
    }

    return result;
}

// checks if two diagonal matrices are equal
bool DiagonalMatrix::operator==(const DiagonalMatrix& other) const {
    return SquareMatrix::operator==(other);
}
