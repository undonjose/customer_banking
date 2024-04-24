"""Import the Account class from the Account.py file."""

from Account import Account
# Define a function for the Savings Account
def savings_account(self, balance, interest, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    account_instance =   Account (balance, 0)        
    
    interest_earned = self.calculate_interest(account_instance.balance, account_instance.interest, months)

    updated_balance = account_instance.balance + interest_earned

    return updated_balance, interest_earned

    def calculate_interest(self, balance, interest_rate, months):
        interest_earned = balance * (interest_rate / 100) * (months / 12)

    return  interest_earned
    print('Your account balance is $', format(create_savings_account.get_balance(), ',.2f'))
    print('Your eanred interest is $', format(create_savings_account.get_interest(), ',.2f'))
