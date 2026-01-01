// Name Syed Muhammad Asad Ali
// ID: sa09475

#include <iostream>
#include <string>

using namespace std;

// Constants
const int MAX_RIDES = 100;
const int MAX_DRIVERS = 50;
const int START_RIDE_ID = 100001;

// Struct Definition
struct Ride {
    string riderName;
    int rideID;
    string driverName;
    string pickupLocation;
    string dropoffLocation;
    double fare;
    int distance; // in KM
    string status; // "Ongoing", "Completed", "Cancelled"
};

// Global Variables
Ride rideDetails[MAX_RIDES];
int rideCount = 0; // Keeps track of total rides
string Drivers[MAX_DRIVERS];
int driverCount = 0; // Keeps track of total drivers

// ================= Function Definitions =================

int IsAvailable(string driverName, Ride rides[]){
    // TODO: Searches through the array 
    //       Checks if the given driverName has an Ongoing ride
    //       If the given driverName has an Ongoing ride returns 1, otherwise returns 0
        for (int i = 0; i < rideCount; i++) {
        if (rides[i].driverName == driverName && rides[i].status == "Ongoing") {
            return 0; // Busy
        }
    }
    return 1; // Available
}

int GetFare(int distance){
    //TODO: Calculate and return the fare based on the given scheme
    //      Distance < 2KM : 50 + (50 * distance)
    //      2KM < Distance < 5KM : 150 + (80 * (distance - 2)) 
    //      Distance > 5KM : 390 + (100 * (distance - 5))
    if (distance < 2) {
        return 50 + (50 * distance);
    } else if (distance <= 5) {
        return 150 + (80 * (distance - 2));
    } else {
        return 390 + (100 * (distance - 5));
    }
}

// Prompts user for ride details and returns a Ride struct
Ride BookRide(string name) {
    // TODO: Prompt user for pickup, drop-off, distance
    //       Displays all available drivers. Hint use the IsAvailable function and the Drivers array.
    //       Prompts the user to select a driver
    //       Calculates the fare by calling the GetFare function.
    //       Set ride status to "Ongoing" and generate Ride ID
    //       If there is no driver avaliable then output an error message, generate a Ride ID, set ride status to "Cancelled" and driverName to ""
    Ride newRide;
    newRide.riderName = name;
    newRide.rideID = START_RIDE_ID + rideCount;

    cout << "Enter Pickup Location: ";
    cin >> newRide.pickupLocation;
    cout << "Enter Drop-off Location: ";
    cin >> newRide.dropoffLocation;

    cout << "Enter Distance (km): ";
    cin >> newRide.distance;

    newRide.fare = GetFare(newRide.distance);

    // Display available drivers
    cout << "Available Drivers:\n";
    bool driverFound = false;
    for (int i = 0; i < driverCount; i++) {
        if (IsAvailable(Drivers[i], rideDetails)) {
            cout << i + 1 << ". " << Drivers[i] << endl;
            driverFound = true;
        }
    }

    if (driverFound) {
        int choice;
        while (true) { //keep looping until valid
            cout << "Select a driver (enter number): ";
            cin >> choice;

            if (choice > 0 && choice <= driverCount && IsAvailable(Drivers[choice - 1], rideDetails)) {
                newRide.driverName = Drivers[choice - 1];
                newRide.status = "Ongoing";
                break; //valid choice → exit loop
            } else {
                cout << "Invalid choice. Please try again.\n";
            }
        }
    } else {
        cout << "No drivers available. Cancelling ride.\n";
        newRide.driverName = "";
        newRide.status = "Cancelled";
    }

    return newRide;
}

// Displays rides that match the given name (rider or driver)
void ViewRides(string name, Ride rides[], string status = "") {
    // Toodo: Loop through the array and print rides where name matches riderName or driverName
    //       Displays all rides for that name regardless of status if status is ""
    //       Displays rides for that name and status if a status value was passed
    bool found = false;
    for (int i = 0; i < rideCount; i++) {
        if ((rides[i].riderName == name || rides[i].driverName == name) &&
            (status == "" || rides[i].status == status)) {
            found = true;
            cout << " Ride ID : " << rides[i].rideID
                 << " ,Rider : " << rides[i].riderName
                 << " ,Driver : " << rides[i].driverName
                 << " ,Pickup : " << rides[i].pickupLocation
                 << " ,Drop-off : " << rides[i].dropoffLocation
                 << " ,Distance : " << rides[i].distance
                 << " ,Fare : " << rides[i].fare
                 << " ,Status : " << rides[i].status << endl;
        }
    }
    if (!found) {
        cout << "No rides found.\n";
    }
}

// Display ongoing rides for the user, prompts for Ride ID, and returns it
int ChangeStatus(string name, Ride rides[], int count) {
    // Todo: Show ongoing rides for the name. Hint: Call ViewRides and use the third parameter,
    //       Ask user to enter the Ride ID to update,
    //       Return the Ride ID so status can be updated in main.
    bool valid = false;
    int rideID;

    while (true) {
        cout << "\nOngoing rides for " << name << ":\n";
        ViewRides(name, rides, "Ongoing");

        cout << "Enter Ride ID to update: ";
        cin >> rideID;

        for (int i = 0; i < count; i++) {
            if ((rides[i].riderName == name || rides[i].driverName == name) &&
                rides[i].rideID == rideID && rides[i].status == "Ongoing") {
                return rideID; 
            }
        }

        cout << "Invalid Ride ID. Please try again.\n";
    }
}




// Sums up the fare of all rides assigned to a driver
double CalculateTotal(string driverName, Ride rides[]) {
    // TODO: Add up fares of rides where driverName matches and status is "Completed"
    double total = 0.0;
    for (int i = 0; i < rideCount; i++) {
        if (rides[i].driverName == driverName && rides[i].status == "Completed") {
            total += rides[i].fare;
        }
    }
    return total;
}

// ================= Main Function =================

int main() {
    // TODO:
    // - Display main menu
    // - Ask the user if they are a Rider (1) or Driver (2)
    // - Prompt for name
    // - If the user is a Driver and the name is not in the Drivers list add it to the list
    // - Based on role, display the appropriate menu
    // - Use the provided functions to implement menu options
    // - Ensure ride count does not exceed MAX_RIDES
    // - Validate menu inputs

    while (true) {
        cout << "\n=== Welcome to the Ride Booking Simulation ===\n";
        cout << "Are you a Rider (1) or a Driver (2)? (0 to Exit): ";
        int role;
        cin >> role; // insert option

        if (role == 0) break;

        if (role != 1 && role != 2) {
            cout << "Invalid option! Try again.\n";
            continue;
        }

        string name;
        cout << "Please enter your name: ";
        cin >> name;

        // Driver registration
        // - Checks if Driver name exists
        // - if not it adds the name
        if (role == 2) {
            bool exists = false;
            for (int i = 0; i < driverCount; i++) {
                if (Drivers[i] == name) {
                    exists = true;
                    break;
                }
            }
            if (!exists && driverCount < MAX_DRIVERS) {
                Drivers[driverCount++] = name;
            }
        }

        // Rider menu
        if (role == 1) {
            int choice;
            do {
                cout << "\nWelcome " << name << ". Please Select an Option:\n";
                cout << "1. Book a Ride\n2. View My Rides\n3. Cancel a Ride\n4. Return to Main Menu\n";
                cin >> choice;

                // checks if ride limit has been reached, if not it increments.
                if (choice == 1) {
                    if (rideCount < MAX_RIDES) {
                        rideDetails[rideCount++] = BookRide(name);
                    } else {
                        cout << "Ride limit reached!\n";
                    }
                } else if (choice == 2) {
                    ViewRides(name, rideDetails);
                } else if (choice == 3) {
                    int id = ChangeStatus(name, rideDetails, rideCount);
                    if (id != -1) {
                        for (int i = 0; i < rideCount; i++) {
                            if (rideDetails[i].rideID == id) {
                                rideDetails[i].status = "Cancelled";
                            }
                        }
                        cout << "Ride cancelled successfully.\n";
                    }
                }
            } while (choice != 4);
        }

        // Driver menu
        else if (role == 2) {
            int choice;
            do {
                cout << "\nWelcome " << name << ". Please Select an Option:\n";
                cout << "1. View Assigned Rides\n2. Mark Ride as Completed\n3. View All Rides\n4. Calculate Total Fare\n5. Return to Main Menu\n";
                cin >> choice;

                if (choice == 1) {
                    ViewRides(name, rideDetails, "Ongoing");
                } else if (choice == 2) {
                    int id = ChangeStatus(name, rideDetails, rideCount);
                    if (id != -1) {
                        for (int i = 0; i < rideCount; i++) {
                            if (rideDetails[i].rideID == id) {
                                rideDetails[i].status = "Completed";
                            }
                        }
                        cout << "Ride marked as Completed.\n";
                    }
                } else if (choice == 3) {
                    ViewRides(name, rideDetails);
                } else if (choice == 4) {
                    double total = CalculateTotal(name, rideDetails);
                    cout << "Total Fare Earned: " << total << " PKR\n";
                }
            } while (choice != 5);
        }
    }
    cout << "Goodbye! >_<) \n" ;
    return 0;
}