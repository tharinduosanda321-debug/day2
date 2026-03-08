def main():
    print("--- Monthly Budget Tracker ---")
    
    # Task 01: Ask for total monthly budget
    try:
        total_budget = float(input("Enter your total monthly budget (LKR): "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for the budget.")
        return

    remaining_balance = total_budget

    # Task 03: Allow entering expenses multiple times until "done"
    print("\nEnter your expenses. Type 'done' to finish.")
    
    while True:
        user_input = input("Enter expense amount (or 'done'): ").strip().lower()
        
        if user_input == 'done':
            break
        
        try:
            expense = float(user_input)
            remaining_balance -= expense
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Task 01: Display remaining balance
    print(f"\nFinal Remaining Balance: {remaining_balance:.2f} LKR")

    # Task 02: Warning Message
    if remaining_balance < 500:
        print("Warning: Low Funds")

if __name__ == "__main__":
    main()
