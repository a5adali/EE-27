#include "BigNum.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

BigNum::BigNum(){
    //initialize to 0
    isNeg=false;
    num.push_back('0');
}


BigNum::BigNum(const BigNum& bigNum){
    //initialize with the bignum
    isNeg=bigNum.isNeg;
    num=bigNum.num;
}

string removeLeadingZeros(const string& str) {
    int index = 0;

    // go through the string until we find a digit that is not zero
    while (index < str.length() && str[index] == '0') {
        index++;
    }

    // if we reached the end, that means the string was made up of only zeros
    // in that case, we just want to return a single '0'
    if (index == str.length()) {
        return str.substr(index - 1); // returns "0"
    } 
    else {
        // otherwise, return everything from the first non-zero digit
        string trimmed = str.substr(index);
        return trimmed;
    }
}

BigNum::BigNum(const string& numStr) {

    // first check if the number given starts with a minus sign
    if (!numStr.empty() && numStr[0] == '-') {
        isNeg = true; // mark it as negative
        num.assign(numStr.begin() + 1, numStr.end());
    } else {
        isNeg = false; // otherwise, it’s positive
        num.assign(numStr.begin(), numStr.end());
    }

    // remove any leading zeros from the extracted number part
    string cleanNum = removeLeadingZeros(string(num.begin(), num.end()));

    // make sure that the remaining characters are all valid digits
    for (int i = 0; i < cleanNum.length(); i++) {
        if (cleanNum[i] < '0' || cleanNum[i] > '9') {
            throw invalid_argument("Invalid input: contains a non-numeric character.");
        }
    }

    // if the string becomes empty (like when the input was "0000"),
    // we just want to store '0' to represent zero properly
    if (cleanNum.empty()) {
        num.clear();
        num.push_back('0');
    } else {
        num.assign(cleanNum.begin(), cleanNum.end());
    }
}

BigNum::BigNum(int number) {
    if (number < 0) {
        //if entered number is Negative
        isNeg = true;
        number = -number; //making it positive
    } else {
        //if entered number is Positive
        isNeg = false;
    }

    //converting the number to string
    string numStr = to_string(number);

    //assigning it to num
    num.assign(numStr.begin(), numStr.end());
}

BigNum::~BigNum() {
    clear();
}


void BigNum::clear() {
    // Clear the vector of digits
    num.clear();
    isNeg = false;
}


void BigNum::print() {
    //print '-' first if the number is negative
    if (isNeg) cout << "-";
    //iterate through all digits and display them
    for (int i = 0; i < num.size(); ++i) {
        //add a comma after every three digits from the right side
        if (i > 0 && (num.size() - i) % 3 == 0) {
            cout << ",";
        }
        //display the current digit
        cout << num[i];
    }
    //move to the next line after printing the number
    cout << endl;
}

void clearCin() {
    cin.clear(); // Clear error flag
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
}

void BigNum::input() {
    clear();
    // print();
    string numStr;
    bool flag = false;

    do {
        flag = false;
        //cout << "Enter a number: ";
        cin >> numStr;

        // Trim spaces (optional but safe)
        numStr.erase(remove_if(numStr.begin(), numStr.end(), ::isspace), numStr.end());

        // Handle sign
        if (!numStr.empty() && numStr[0] == '-') {
            isNeg = true;
            numStr = numStr.substr(1);
        } else {
            isNeg = false;
        }

        // Empty input check
        if (numStr.empty()) {
            cout << "Invalid input. Please enter a valid integer number." << endl;
            flag = true;
            continue;
        }

        // Verify all characters are digits
        for (char ch : numStr) {
            if (ch < '0' || ch > '9') {
                flag = true;
                clearCin();
                cout << "Invalid input, digits only (no commas or letters)." << endl;
                break;
            }
        }

    } while (flag);

    string properNum = removeLeadingZeros(numStr);
    if (properNum.empty()) {
        num.clear();
        num.push_back('0'); // assign "0"
    } else {
        num.clear();
        num.assign(properNum.begin(), properNum.end()); // copy string chars into vector
    }

}


void BigNum::inputFromFile(const string& fileName) {
    ifstream file(fileName);
    if (!file.is_open()) {
        throw runtime_error("Error: Unable to open file " + fileName);
    }

    string line;
    getline(file, line); // Read the first line from file

    // Trim spaces from both sides
    line.erase(0, line.find_first_not_of(' ')); // remove spaces from start
    line.erase(line.find_last_not_of(' ') + 1); // remove spaces from end

    // Check if line is empty
    if (line.empty()) {
        throw invalid_argument("Invalid input: File contains no data.");
    }

    // Determine if the number is negative
    if (line[0] == '-') {
        isNeg = true;
        line = line.substr(1);
    } else {
        isNeg = false;
    }

    // Ensure all characters are digits
    for (char c : line) {
        if (c < '0' || c > '9') {
            file.close();
            throw invalid_argument("Invalid input: File contains non-numeric characters.");
        }
    }

    clear(); // Reset any previous data

    // Remove unnecessary leading zeros
    string cleanNum = removeLeadingZeros(line);
    if (cleanNum.empty()) {
        num.push_back('0'); // If only zeros were present, set to 0
    } else {
        num.assign(cleanNum.begin(), cleanNum.end()); // Save valid number
    }

    file.close(); // Close the file after processing
}



void BigNum::printToFile(const string& fileName) {
    ofstream outputFile(fileName, ios::app); // Open in append mode
    if (!outputFile.is_open()) {
        throw runtime_error("Could not open file: " + fileName);
    }

    // Check if the file is empty
    outputFile.seekp(0, ios::end); // Move to the end of the file
    if (outputFile.tellp() != 0) {
        outputFile << endl; // Add a new line if the file is not empty
    }

    // Print the sign if the number is negative
    if (isNeg) {
        outputFile << "-";
    }

    // Print the number with commas as needed
    for (int i = 0; i < num.size(); ++i) {
        if (i != 0 && (num.size() - i) % 3 == 0) {
            outputFile << ",";
        }
        outputFile << num[i];
    }

    outputFile.close(); // Close the file after writing
}


void BigNum::copy(const BigNum& bigNum){

    //make sure it isnt self assigning
    if (this != &bigNum) {
        // Copy the sign and the num vector
        isNeg = bigNum.isNeg;
        num.clear();
        num = bigNum.num;
    }

}


void BigNum::operator=(const BigNum& bigNum){
    copy(bigNum);
}


void BigNum::zerofy(){
    num.clear();
    num.push_back('0');
    isNeg=false;
}


bool BigNum::equals(const BigNum& bigNum){
    //check negative
    if(isNeg==bigNum.isNeg){
        //checking the length
        if(num.size()==bigNum.num.size()){
            //comparing each digit
            for (int i = 0; i < num.size(); ++i) {
                if (num[i]!=bigNum.num[i])
                {   //if digit not same then false
                    return false;
                }
            
            }
            //if every digit same then true
            return true;
        }
        return false;
    }
    return false;
    
}


bool BigNum::notEquals(const BigNum& bigNum){
    //opposite of equals
    if (equals(bigNum)){
        return false;
    }else{
        return true;
    }
}


bool BigNum::lessThan(const BigNum& bigNum){
    if (equals(bigNum)) {
        return false;  // If they are equal, this returns false.
    }
    if (isNeg != bigNum.isNeg) {
    //if first num neg& second num pos then its def less so true
    //if first num pos& second num neg then its def not less so false
    return isNeg;
    }
    //if same sign then we check size
    if (num.size() != bigNum.num.size()) {
        if (isNeg) {
            // If both neg, more digits means it's smaller
            return num.size() > bigNum.num.size();
        } else {
            // If both pos, fewer digits means it's smaller
            return num.size() < bigNum.num.size();
        }
    }
    //if same lengt then compare digits
    for (int i = 0; i < num.size(); ++i) {
        if (num[i] != bigNum.num[i]) {
            if (isNeg) {
                // For negative numbers, reverse the logic
                return num[i] > bigNum.num[i];
            } else {
                // For positive numbers, smaller digit means it's less
                return num[i] < bigNum.num[i];
            }
        }
    }
    return false;
    
}


bool BigNum::greaterThan(const BigNum& bigNum){
    //opp of lesserThan
    if (equals(bigNum)){
        return false;
    }
    if (this->lessThan(bigNum)){
        return false;
    }else{
        return true;
    }
}

BigNum BigNum::add(const BigNum& other) {
    BigNum result;
    BigNum temp;
    temp.copy(other);

    // Case 1: Numbers have different signs — treat as subtraction
    if (isNeg != temp.isNeg) {
        if (isNeg) {
            // (-a) + b → b - a
            isNeg = false;                  // Temporarily make this positive
            result = temp.subtract(*this);  // Perform subtraction
            isNeg = true;                   // Restore sign
            return result;
        } else {
            // a + (-b) → a - b
            temp.isNeg = false;             // Temporarily make -b positive
            result = this->subtract(temp);  // Perform subtraction
            temp.isNeg = true;              // Restore sign
            return result;
        }
    }

    // Case 2: Both numbers have the same sign
    if (!isNeg) {
        // Both positive
        result.clear();
        int carry = 0;
        int i = num.size() - 1;
        int j = other.num.size() - 1;

        // Add digits from right to left
        while (i >= 0 || j >= 0 || carry > 0) {
            int digitA = (i >= 0) ? num[i--] - '0' : 0;
            int digitB = (j >= 0) ? other.num[j--] - '0' : 0;
            int total = digitA + digitB + carry;

            result.num.insert(result.num.begin(), (total % 10) + '0');
            carry = total / 10;
        }

        // Remove leading zeros
        string cleaned(result.num.begin(), result.num.end());
        cleaned = removeLeadingZeros(cleaned);
        result.num.assign(cleaned.begin(), cleaned.end());
        return result;
    } 
    else {
        // Both negative: (-a) + (-b) → -(a + b)
        isNeg = false;
        temp.isNeg = false;

        result = this->add(temp);   // Add as positive
        result.isNeg = true;        // Apply negative sign to final result

        isNeg = true;               // Restore original sign
        return result;
    }
}

void  BigNum::increment(){
    BigNum one(1);//create a bignum with 1
    *this=this->add(one);//call add function
}


BigNum BigNum::subtract(const BigNum& other) {
    BigNum result;
    BigNum temp;
    temp.copy(other);

    // Case 1: If one number is negative and the other positive, handle using addition
    if (isNeg != temp.isNeg) {
        if (isNeg) {
            // (-a) - (+b) → -(a + b)
            isNeg = false;                   // Temporarily make this positive
            result = temp.add(*this);        // Add magnitudes
            result.isNeg = true;             // Final result will be negative
            isNeg = true;                    // Restore original sign
            return result;
        } else {
            // (+a) - (-b) → a + b
            temp.isNeg = false;              // Make -b positive
            result = this->add(temp);        // Add magnitudes
            temp.isNeg = true;               // Restore -b
            return result;
        }
    }

    // Case 2: Both numbers share the same sign
    bool makeNegative = false;

    if (isNeg && temp.isNeg) {
        // (-a) - (-b) → b - a
        isNeg = false;
        temp.isNeg = false;
        result = temp.subtract(*this);       // Reverse subtraction order
        isNeg = true;
        temp.isNeg = true;
        return result;
    } else {
        // (+a) - (+b)
        if (!(this->greaterThan(other))) {
            makeNegative = true;             // Result should be negative
        }
    }

    // Case 3: Perform digit-by-digit subtraction
    result.clear();
    int borrow = 0;
    int i = num.size() - 1;
    int j = other.num.size() - 1;

    while (i >= 0 || j >= 0) {
        int digitA = (i >= 0) ? num[i--] - '0' : 0;
        int digitB = (j >= 0) ? other.num[j--] - '0' : 0;
        int diff;

        if (!makeNegative) {
            // Normal subtraction: a > b
            diff = digitA - digitB - borrow;
            if (diff < 0) {
                diff += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }
        } else {
            // Reverse subtraction: b > a
            diff = digitB - digitA - borrow;
            if (diff < 0) {
                diff += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }
        }

        result.num.insert(result.num.begin(), diff + '0');
    }

    // Clean up result
    string cleaned(result.num.begin(), result.num.end());
    cleaned = removeLeadingZeros(cleaned);
    result.num.assign(cleaned.begin(), cleaned.end());

    // Apply negative sign if required and result isn’t zero
    if (makeNegative && result.num[0] != '0') {
        result.isNeg = true;
    }

    return result;
}


void   BigNum::decrement(){
    BigNum one(1);//create a bignum with 1
    *this=this->subtract(one);//call sub function

}

BigNum BigNum::add(const int num){
    BigNum l(num);//create a bignum
    l=this->add(l);//call add func
    return l;
}


void   BigNum::compoundAdd(const BigNum& bigNum){
    *this=this->add(bigNum);//call add by this and saving it in this
}


void   BigNum::compoundAdd(const int num){
    BigNum bigNum(num);
    *this=this->add(bigNum);//call add by this and saving it in this
}


BigNum BigNum::subtract(const int num){
    BigNum bignum(num);//creat a new bignum
    BigNum answer;
    answer=this->subtract(bignum);//call sub
    return answer;
}


void   BigNum::compoundSubtract(const BigNum& bigNum){
    *this=this->subtract(bigNum);//call sub by this and saving it in this
}


void BigNum::compoundSubtract(const int num){
    BigNum bigNum(num);
    *this=this->subtract(bigNum);//call add by this and saving it in this
}

BigNum BigNum::multiply(const BigNum& other) {
    // Treat current object as A and the parameter as B
    // Ensure A has equal or greater size than B
    if (num.size() >= other.num.size()) {
        BigNum partialResult;     // Temporary result for each digit multiplication
        BigNum totalProduct;      // Final cumulative result

        int bIndex = other.num.size() - 1;  // Start from least significant digit of B
        int zeroPadding = 0;                // Used to shift partial results (like *10, *100, etc.)

        // Go through B's digits from right to left
        while (bIndex >= 0) {
            int digitB = other.num[bIndex--] - '0'; // Current digit of B
            int carry = 0;

            // Reset partial result for this round
            partialResult.clear();

            // Add trailing zeros based on current position
            for (int z = 0; z < zeroPadding; z++) {
                partialResult.num.push_back('0');
            }

            // Multiply this digit of B with all digits of A
            for (int aIndex = num.size() - 1; aIndex >= 0; aIndex--) {
                int digitA = num[aIndex] - '0';
                int product = (digitA * digitB) + carry;
                partialResult.num.insert(partialResult.num.begin(), (product % 10) + '0');
                carry = product / 10;
            }

            // Handle remaining carry if any
            if (carry > 0) {
                partialResult.num.insert(partialResult.num.begin(), carry + '0');
            }

            // Add the partial result to the total product
            totalProduct.compoundAdd(partialResult);
            zeroPadding++; // Increment padding for next digit of B
        }

        // Adjust the sign of the final result
        if (isNeg != other.isNeg) {
            totalProduct.isNeg = true;
        }

        return totalProduct;
    } 
    else {
        // If B is larger, swap and multiply again
        BigNum copy;
        copy = other;

        BigNum temp = copy.multiply(*this);
        return temp;
    }
}


BigNum BigNum::div(const BigNum& bigNum) {
    // Prepare local copies so we don't change caller objects
    BigNum dividend;
    dividend.copy(*this);
    BigNum divisor;
    divisor.copy(bigNum);
    BigNum quotient;   // final result
    BigNum remainder;  // running remainder during division

    // Zero divisor check: if divisor == 0, print message and return zero-like quotient
    if (divisor.num.size() == 1 && divisor.num[0] == '0') {
        cout << "Invalid operation: division by zero" << endl;
        // return zero (quotient is zero by default)
        quotient.clear();
        quotient.num.push_back('0');
        return quotient;
    }

    // Decide final sign and make both operands positive for calculation
    bool resultNegative = (dividend.isNeg != divisor.isNeg);
    dividend.isNeg = false;
    divisor.isNeg = false;

    // If dividend < divisor, quotient is 0
    if (dividend.lessThan(divisor) || (dividend.equals(divisor) == false && dividend.num.size() < divisor.num.size())) {
        quotient.clear();
        quotient.num.push_back('0');
        return quotient;
    }

    // Long division: bring digits from dividend into remainder one by one
    int n = dividend.num.size();
    quotient.clear();
    remainder.clear();

    for (int idx = 0; idx < n; ++idx) {
        // bring next digit down: remainder = remainder * 10 + nextDigit
        if (remainder.num.size() == 1 && remainder.num[0] == '0') {
            remainder.num.clear();
        }
        remainder.num.push_back(dividend.num[idx]);

        // remove leading zeros from remainder if any
        string remStr(remainder.num.begin(), remainder.num.end());
        remStr = removeLeadingZeros(remStr);
        remainder.num.assign(remStr.begin(), remStr.end());
        if (remainder.num.empty()) remainder.num.push_back('0');

        // find the largest digit d in [0..9] such that divisor * d <= remainder
        int digitFound = 0;
        for (int d = 9; d >= 0; --d) {
            BigNum dBig; dBig.clear();
            dBig.num.push_back('0' + d); // single-digit BigNum for multiplier
            BigNum prod = divisor.multiply(dBig); // divisor * d

            // if prod <= remainder (i.e., not greater), we've found the digit
            if (!remainder.lessThan(prod)) {
                // remainder = remainder - prod
                remainder.compoundSubtract(prod);
                // append this digit to quotient
                quotient.num.push_back('0' + d);
                digitFound = d;
                break;
            }
        }
        // continue to next digit
    }

    // Remove leading zeros from quotient string
    string qStr(quotient.num.begin(), quotient.num.end());
    qStr = removeLeadingZeros(qStr);
    if (qStr.empty()) qStr = "0";
    quotient.num.assign(qStr.begin(), qStr.end());

    // Set sign on quotient (unless quotient == 0)
    if (!(quotient.num.size() == 1 && quotient.num[0] == '0') && resultNegative) {
        quotient.isNeg = true;
    }

    return quotient;
}


BigNum BigNum::mod(const BigNum& other) {
    BigNum result;          // Stores the remainder
    BigNum tempDiv;         // For division result
    BigNum tempMul;         // For multiplication
    BigNum divisorCopy;     // To avoid altering the original divisor

    // Prevent modulus by zero
    if (other.num == result.num) {
        cout << "Error: Modulus by zero is undefined." << endl;
        return result;
    }

    // Work on a copy of the divisor
    divisorCopy.copy(other);

    // Divide the number and get the quotient
    tempDiv = this->div(other);

    // Multiply quotient by divisor
    tempMul = divisorCopy.multiply(tempDiv);

    // Handle potential negative sign before subtraction
    bool wasNegative = false;
    if (isNeg) {
        isNeg = false;
        wasNegative = true;
    }

    // Calculate remainder: this - (divisor * quotient)
    result = this->subtract(tempMul);

    // Restore original sign if necessary
    if (wasNegative) {
        isNeg = true;
    }

    // Ensure remainder sign stays positive
    result.isNeg = false;

    return result;
}

//main fuction
int main() {

    // Test constructors
    BigNum num1("987654321987654321987654321987654321");
    BigNum num2("123456789123456789123456789123456789");

    cout << "\nNum1: ";
    num1.input();
    cout << "\nNum2: ";
    num2.input();

    // Test Addition
    BigNum addResult = num1.add(num2);
    cout << "\n\nAddition: ";
    addResult.print();

    // Test Subtraction
    BigNum subResult = num1.subtract(num2);
    cout << "\nSubtraction: ";
    subResult.print();

    // Test Multiplication
    BigNum mulResult = num1.multiply(num2);
    cout << "\nMultiplication: ";
    mulResult.print();

    // Test Division
    BigNum divResult = num1.div(num2);
    cout << "\nDivision: ";
    divResult.print();

    // Test Modulus
    BigNum modResult = num1.mod(num2);
    cout << "\nModulus: ";
    modResult.print();

    return 0;
}
