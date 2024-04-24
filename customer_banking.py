
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
 
    savings_balance = float(input('What is your savings account balance? '))
    savings_interest = float(input('What is the APR for the savings account? '))
    savings_months = int(input('How many month are you saving for? '))
    
   
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

   
    print(f"Savings Interest Earned: ${interest_earned_savings:.2f}")
    print(f"Updated Savings Balance: ${updated_savings_balance:.2f}")


    cd_balance = float(input('Enter your CD account balance: '))
    cd_interest_rate = float(input('Enter the APR for the CD account: '))
    cd_months = int(input('Enter the number of months for CD: '))

 
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)


if __name__ == "__main__":
    # Call the main function.
    main()
