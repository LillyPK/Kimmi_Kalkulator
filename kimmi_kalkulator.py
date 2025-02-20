import math

def calculate_min_subs(target, sub_price, split, deduction_percent):
    """
    Calculate the minimum number of subscriptions required to reach the target amount.
    
    Parameters:
      target (float): The target withdrawal amount.
      sub_price (float): The full price of a subscription.
      split (float): The revenue share for the streamer (e.g., 0.5 for 50/50).
      deduction_percent (float): Additional fee/tax percentage to deduct.
      
    Returns:
      int: The minimum number of subscriptions needed.
    """
    # Calculate the net earnings per subscription after applying the revenue split and deductions.
    net_earning = sub_price * split * (1 - deduction_percent / 100)
    
    if net_earning <= 0:
        return None  # Avoid division by zero or negative earnings.
    
    # Use math.ceil to ensure we cover the full target amount.
    return math.ceil(target / net_earning)

def main():
    print("Welcome to the Twitch Sub Points Calculator!")
    
    # Ask for the target withdrawal amount (default $10).
    target_input = input("Enter target withdrawal amount (default 10): ")
    try:
        target = float(target_input) if target_input else 10.0
    except ValueError:
        print("Invalid input. Using default target of $10.")
        target = 10.0

    # Ask for the subscription price (default $5.99).
    sub_price_input = input("Enter subscription price (default 5.99): ")
    try:
        sub_price = float(sub_price_input) if sub_price_input else 5.99
    except ValueError:
        print("Invalid input. Using default subscription price of $5.99.")
        sub_price = 5.99

    # Ask for fee/tax deduction percentage (if any, default 0%).
    deduction_input = input("Enter fee/tax deduction percentage (default 0): ")
    try:
        deduction_percent = float(deduction_input) if deduction_input else 0.0
    except ValueError:
        print("Invalid input. Using default deduction of 0%.")
        deduction_percent = 0.0

    # Define revenue splits for the three tiers.
    revenue_tiers = {
        "50/50": 0.5,
        "60/40": 0.6,
        "70/30": 0.7,
    }

    print("\nCalculating the minimum number of subscriptions required:")
    for tier, split in revenue_tiers.items():
        min_subs = calculate_min_subs(target, sub_price, split, deduction_percent)
        if min_subs is None:
            print(f"For the {tier} revenue split: Error in calculation (net earning per sub is 0 or negative).")
        else:
            print(f"For the {tier} revenue split: {min_subs} subscription(s) are required.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")