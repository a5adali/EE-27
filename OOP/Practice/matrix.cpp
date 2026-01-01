#include <iostream>
using namespace std;

int main() {
    int rows, cols;

    // Ask user for matrix size
    cout << "Enter number of rows: ";
    cin >> rows;
    cout << "Enter number of columns: ";
    cin >> cols;

    // Dynamically allocate memory for 2D array
    int** matrix = new int*[rows];
    for (int i = 0; i < rows; ++i) {
        matrix[i] = new int[cols];
    }

    // Input matrix elements
    cout << "\nEnter elements of the matrix:\n";
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << "Element [" << i + 1 << "][" << j + 1 << "]: ";
            cin >> matrix[i][j];
        }
    }

    // Display matrix in {{1,2},{3,4}} format
    cout << "\nMatrix in curly brace format:\n";
    cout << "{";
    for (int i = 0; i < rows; ++i) {
        cout << "{";
        for (int j = 0; j < cols; ++j) {
            cout << matrix[i][j];
            if (j < cols - 1)
                cout << ",";
        }
        cout << "}";
        if (i < rows - 1)
            cout << ",";
    }
    cout << "}" << endl;

    // Free dynamically allocated memory
    for (int i = 0; i < rows; ++i) {
        delete[] matrix[i];
    }
    delete[] matrix;

    return 0;
}