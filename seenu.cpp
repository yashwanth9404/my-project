#include <iostream> // Includes the input-output stream library
#include <string>   // Includes the string library to use text variables

int main() {
    // 1. Declare variables to store data
    std::string userName;
    int birthYear = 0;
    const int currentYear = 2026; // Constant variable that cannot be changed

    // 2. Prompt the user and read string input
    std::cout << "Enter your name: ";
    std::getline(std::cin, userName); // Reads an entire line of text

    // 3. Prompt the user and read numerical input
    std::cout << "Enter your birth year: ";
    std::cin >> birthYear;

    // 4. Perform arithmetic calculation
    int age = currentYear - birthYear;

    // 5. Output results with conditional if-else statements
    std::cout << "\nHello, " << userName << "!" << std::endl;
    std::cout << "You are approximately " << age << " years old." << std::endl;

    if (age >= 18) {
        std::cout << "Status: You are an adult." << std::endl;
    } else {
        std::cout << "Status: You are a minor." << std::endl;
    }

    return 0; // Signals that the program executed successfully
}
