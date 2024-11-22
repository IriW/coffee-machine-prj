# Coffee Machine Challenge

This project is the **Day 15 challenge** from the Udemy course **"100 Days of Code: The Complete Python Pro Bootcamp"** by Dr. Angela Yu. 
The code differs from the solution proposed by the course author and provides similar functionality with additional error handling.

      NOTE: The program is basic and functional just enough, to allow further development of features and extra error handling which is planned to be used for deployment automation pipelines set up (by me).
      The code in this form it should not be treated as 100% production solution!

It is a basic Coffee Machine program that allows users to:

- Select one of three coffee drinks.
- Process payment through coin inputs.
- Deduct resources (water, coffee, and milk) after preparing a drink.

---

## Features

- **Drink Selection**: 
  - Choose between three drinks: **Espresso**, **Latte**, and **Cappuccino**.
- **Resource Management**: 
  - Tracks available resources (water, milk, coffee).
  - Notifies users when resources are insufficient.
- **Payment Processing**: 
  - Accepts coins (quarters, dimes, nickels, pennies).
  - Calculates total payment and dispenses change if overpaid.
- **Maintenance Options**:
  - `resources`: Displays the machine's current resource levels.
  - `off`: Turns off the coffee machine program.

---

## How It Works

1. **Start the Program**: Run the program to display the coffee menu and initial greeting.
2. **Select a Drink**:
   - Input `1`, `2`, or `3` to select a drink.
   - Input `resources` to check resource levels.
   - Input `off` to exit the program.
3. **Process Payment**:
   - Enter the number of coins for quarters, dimes, nickels, and pennies.
   - The program calculates total money inserted and validates against the drink's cost.
   - If sufficient funds are provided:
     - The drink is prepared.
     - Any overpayment is returned as change.
   - If funds are insufficient:
     - Money is refunded, and the user can try again.
4. **Resource Deduction**:
   - After preparing a drink, the program deducts the necessary resources.
   - If resources are insufficient for the selected drink:
     - The program suggests an alternative drink or notifies the user if no drinks can be prepared.
5. **Enjoy Your Coffee**:
   - The program serves the drink and thanks the user.

---

## Code Breakdown

### Data Definitions

- **Menu**: Contains the drink options, their ingredients, and prices.
- **Resources**: Tracks the current levels of water, milk, and coffee.
- **Coin Values**: Used to calculate total payment from coin inputs.

### Core Functions

- **`get_coin_input(prompt)`**:
  - Handles user input for drink selection and coin entry.
- **`resources_sufficient(drink)`**:
  - Checks if enough resources are available to prepare the selected drink.
- **`suggest_drink()`**:
  - Suggests an alternative drink if the selected one cannot be prepared.
- **`deduct_resources(drink)`**:
  - Deducts the required ingredients from the machine's resources.
- **`print_resources()`**:
  - Displays the current resource levels.
- **`process_payment(drink)`**:
  - Processes coin inputs and validates the total payment.

### Main Program Loop

- Continuously displays the menu and waits for user input.
- Handles drink selection, payment, and resource updates.
- Stops running when the user inputs `off`.

---

## Requirements

- **Python 3.7 or later**

---

## How to Run

1. Clone this repository to your local machine.
2. Run the script: `python coffee_machine.py`


**LICENSE**
This project is part of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu. For personal learning and practice purposes only.
