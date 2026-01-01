#include "Matrix.hpp"

Matrix::Matrix(const int rows, const int cols) {
    // store size and make space for all values
    this->rows = rows;
    this->cols = cols;
    elements = std::vector<double>(rows * cols, 0.0);
}

Matrix::Matrix(const Matrix& other) {
    // copy size
    rows = other.rows;
    cols = other.cols;

    // copy elements one by one
    elements = std::vector<double>(rows * cols);
    for (int i = 0; i < rows * cols; i++) {
        elements[i] = other.elements[i];
    }
}

double Matrix::getElement(const int row, const int col) const {
    // check if position is outside the matrix
    if (row < 0 || col < 0 || row >= rows || col >= cols) {
        return 0.0;
    }

    // convert 2d to 1d index
    int idx = row * cols + col;
    return elements[idx];
}

void Matrix::setElement(const int row, const int col, const double value) {
    // ignore invalid positions
    if (row < 0 || col < 0 || row >= rows || col >= cols) {
        return;
    }

    // convert 2d to 1d index
    int idx = row * cols + col;
    elements[idx] = value;
}

int Matrix::getRows() const {
    return rows;
}

int Matrix::getCols() const {
    return cols;
}

int Matrix::getElementsSize() const {
    return rows * cols;
}

Matrix Matrix::operator+(const Matrix& other) const {
    // make result matrix with same size
    Matrix result(rows, cols);

    // add each element
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            double sum = getElement(r, c) + other.getElement(r, c);
            result.setElement(r, c, sum);
        }
    }
    return result;
}

Matrix Matrix::operator-(const Matrix& other) const {
    // make result matrix with same size
    Matrix result(rows, cols);

    // subtract element by element
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            double diff = getElement(r, c) - other.getElement(r, c);
            result.setElement(r, c, diff);
        }
    }
    return result;
}

Matrix Matrix::operator*(const Matrix& other) const {
    // multiplication result has different column count
    Matrix result(rows, other.cols);

    // multiply row by column
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < other.cols; c++) {

            double value = 0.0;

            // compute sum of products for this cell
            for (int mid = 0; mid < cols; mid++) {
                value += getElement(r, mid) * other.getElement(mid, c);
            }

            result.setElement(r, c, value);
        }
    }

    return result;
}

bool Matrix::operator==(const Matrix& other) const {
    // first check sizes
    if (rows != other.rows || cols != other.cols) {
        return false;
    }

    // then compare every value
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (getElement(r, c) != other.getElement(r, c)) {
                return false;
            }
        }
    }

    return true;
}
