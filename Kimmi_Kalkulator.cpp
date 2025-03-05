#include <iostream>
#include <cmath> // For std::ceil

int main() {
    // Input variables
    double targetAmount, subscriptionPrice, deductionPercent;
    std::cout << "Enter the target withdrawal amount (default is $10): ";
    std::cin >> targetAmount;
    std::cout << "Enter the subscription price (default is $5.99): ";
    std::cin >> subscriptionPrice;
    std::cout << "Enter the fee/tax deduction percentage (default is 0%): ";
    std::cin >> deductionPercent;

    // Revenue split options
    double splits[] = {0.5, 0.6, 0.7}; // 50/50, 60/40, 70/30

    // Calculate and display results for each split
    for (double split : splits) {
        // Calculate net earnings per subscription
        double netEarning = subscriptionPrice * split * (1 - deductionPercent / 100.0);

        // Check for valid earnings
        if (netEarning <= 0) {
            std::cout << "Invalid net earnings for split " << split * 100 << "/" << (1 - split) * 100 << ".\n";
            continue;
        }

        // Calculate minimum subscriptions required
        int minSubscriptions = static_cast<int>(std::ceil(targetAmount / netEarning));

        // Display the result
        std::cout << "For a " << split * 100 << "/" << (1 - split) * 100 << " split, you need at least "
                  << minSubscriptions << " subscriptions to reach $" << targetAmount << ".\n";
    }

    std::cout << "\nPress Enter to exit...";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Clear the input buffer
    std::cin.get(); // Wait for Enter key

    return 0;
}
