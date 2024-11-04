# investment_calculator.py

def investment_calculator(initial_investment, annual_interest_rate, years, monthly_contribution=0):
    months = years * 12
    monthly_rate = annual_interest_rate / 12 / 100
    future_value = initial_investment

    for _ in range(months):
        future_value += monthly_contribution
        future_value *= (1 + monthly_rate)

    return round(future_value, 2)


# Get user input for each parameter
if __name__ == "__main__":
    initial_investment = float(input("Enter initial investment amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (in %): "))
    years = int(input("Enter the number of years: "))
    monthly_contribution = float(input("Enter monthly contribution (default is 0): ") or 0)

    final_amount = investment_calculator(initial_investment, annual_interest_rate, years, monthly_contribution)
    print(f"The investment will grow to: ${final_amount}")
