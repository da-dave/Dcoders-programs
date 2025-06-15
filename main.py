### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: ")) * 1.00
        half_dollars = int(input("How many half dollars?: ")) * 0.50
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05
        total = dollars + half_dollars + quarters + nickels
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print(f"Sorry there is not enough {coins}. Money is refunded")
            return False
        elif coins > cost:
            change = round(cost - coins, 2)
            print(f"Here is {change} in change")
        print("Transaction successful.")
        return True
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
def print_report(resources)
    print(f"Bread: {resources['bread']} slice(s)")
    print(f"Ham: {resources['ham']} slice(s)")
    print(f"Cheese: {resources['cheese']} slice(s)")

machine = SandwichMachine(recipes)
is_on = True
while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report(machine.machine_resources)
    elif choice in recipes:
        sandwich = recipes[choice]
        if machine.check_resources(sandwich["ingredients"]):
            payment = machine.process_coins()
            if machine.transaction_result(payment, sandwich["cost"]):
                machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid input.")