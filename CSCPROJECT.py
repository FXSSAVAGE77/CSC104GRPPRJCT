import streamlit as st
#BY FRANK EMEKA
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
#BY RUTH EDWARD 
class SavingsAccount(Account):
    limit = 1000  # Example limit for withdrawals

    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if amount <= self.limit:
            return super().withdraw(amount)
        return False
#BY DOMINION O.
class CurrentAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)


st.set_page_config(page_title="Bank App", layout="centered")

# Initialize accounts
savings = SavingsAccount(20000)
current = CurrentAccount(30000)

# Set a PIN 
PIN = "1234"  # Example PIN

# User input for PIN
user_pin = st.text_input("Enter your PIN", type="password")
# BY PHILLIP POPOOLA AND SULEIMAN BWALA
if user_pin == PIN:
    st.success("PIN verified successfully!")

    with st.form("account_form"):
        account_type = st.selectbox("Select Account Type", ("Savings", "Current"))
        amount = st.number_input("Enter Amount", min_value=1)  # Allow any positive amount
        operations = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
        submit = st.form_submit_button("Submit")

        if submit:
            if operations == "Withdraw":
                if account_type == "Savings":
                    if savings.withdraw(amount):
                        st.success(f"Successfully withdrew {amount} from Savings Account.")
                    else:
                        st.error("Insufficient balance in Savings Account or exceeds withdrawal limit.")
                elif account_type == "Current":
                    if current.withdraw(amount):
                        st.success(f"Successfully withdrew {amount} from Current Account.")
                    else:
                        st.error("Insufficient balance in Current Account.")
            elif operations == "Deposit":
                if account_type == "Savings":
                    savings.deposit(amount)
                    st.success(f"Successfully deposited {amount} into Savings Account.")
                elif account_type == "Current":
                    current.deposit(amount)
                    st.success(f"Successfully deposited {amount} into Current Account.")
else:
    st.error("Invalid PIN. Please try again.")
