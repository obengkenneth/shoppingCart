cart = []

# shopping functions
def add(items):
    cart.append(items)
    print(f'{items} has/have been added to the cart.')

def remove(items):
    cart.remove(items)

ans = 0
# shopping loop
while ans != "quit":
    try:
        ans = input("Enter an action(add, remove, clear, show and quit to stop shopping) : ")
        if ans == "add":
            addItems = 0
            while True:
                addItems = input("Enter your item or end to stop adding items : ").title()
                if addItems == "End":
                    break
                else:
                    addItems.split()
                    add(addItems)
        elif ans == "remove":
            removeItems = input("Enter the item you want to remove from the cart : ")
            remove(removeItems)
            print(f"{removeItems} has been removed.")
        elif ans == "clear":
            cart.clear()
            print(f"Your cart is empty.")
        elif ans == "show":
            print(cart)
        elif ans == "quit": 
            print("Thank you for shopping")
            ans = "quit"
    except: print("Please enter a valid input.")

