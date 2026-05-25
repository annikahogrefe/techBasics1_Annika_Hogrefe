# another supermarket game lol
# thanks for the skeleton structure, really helped me to not panic in front of my blank screen and had me use ai less and 'experiment' more myself! :)

import os
import sys
import time

# ingredients list
ingredients = [
    "Flour",
    "Milk",
    "Sugar",
    "Eggs",
    "Baking Soda",
    "Butter",
]

# animated typing effect (copied from my other game, hehe)
def type_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# the 30-second memory countdown
# ALL OF THIS COUNTDOWN AND CLEARING SCREEN WAS DONE BY GEMINI!
# I really wanted this in my game since I think it definetly increases the fun and makes it much more challenging but had no idea how to do it myself
def run_memory_phase():
    os.system("cls" if os.name == "nt" else "clear")

    print("=== MEMORIZE YOUR INGREDIENTS! ===")
    print("You have exactly 30 seconds.\n")

    for item in ingredients:
        print(f"• {item}")

    print("\n" + "=" * 32)

    for seconds_left in range(30, -1, -1):
        print(f"\rTime remaining: {seconds_left} seconds... ", end="", flush=True)
        time.sleep(1)

    # --- ANTI-CHEAT MEASURE ---
    # 1. Print 100 blank lines to completely flush the scrollback history upward
    print("\n" * 100)

    # 2. Clear the screen normally
    os.system("cls" if os.name == "nt" else "clear")

# from here I did the coding myself again :)
    print("=== TIME'S UP! ===\n")
    type_text("You arrived at the supermarket. Let's see what's in the aisles...")
    time.sleep(2)

cart = []  # basically the inventory
items_in_room = [
    {"name": "Milk", "price": 1},
    {"name": "Apple", "price": 1},
    {"name": "Banana", "price": 2},
    {"name": "Eggs", "price": 3},
    {"name": "Flour", "price": 2},
    {"name": "Chocolate", "price": 5},
    {"name": "Butter", "price": 4},
    {"name": "Cheese", "price": 3},
    {"name": "Bread", "price": 4},
    {"name": "Baking Soda", "price": 1},
    {"name": "Sugar", "price": 3},
    {"name": "Toilet Paper", "price": 2},
    {"name": "Candy", "price": 1},
]
player_money = 20 #instead of inventory limit, bc I felt like that wouldn't make sense here. hope that's ok!

# functions
# (some done with the help of gemini! usually the more complicated stuff, I bet you can tell lol)

def show_cart():
    print("\n--- YOUR CART ---")
    if not cart:
        print("Your cart is currently empty.")
    else:
        for item in cart:
            print(f"• {item['name']} (€{item['price']})")


def checkout():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== CHECKOUT REGISTER ===")

    cart_names = [item["name"] for item in cart]

    correct_items = [name for name in cart_names if name in ingredients]
    wrong_items = [name for name in cart_names if name not in ingredients]
    missing_items = [name for name in ingredients if name not in cart_names]

    print(f"\nYou bought {len(correct_items)} out of 6 correct ingredients.")
    print(f"You spent a total of €{sum(item['price'] for item in cart)}.")

    if len(correct_items) == 6 and len(wrong_items) == 0:
        type_text(
            "\n PERFECT! You got exactly what you needed without any junk. Your cake tastes amazing!"
        )
    elif len(correct_items) >= 4:
        type_text(
            "\n Not bad! You missed a few things or bought some weird extras, but you managed to bake a passable cake."
        )
        if missing_items:
            print(f"Missing items: {', '.join(missing_items)}")
        if wrong_items:
            print(f"Accidental items: {', '.join(wrong_items)}")
    else:
        type_text(
            "\n Oh no! Your cake was a disaster. You didn't remember enough of the right ingredients."
        )
        print(f"Missing items: {', '.join(missing_items)}")

    print("\nThanks for playing!")
    sys.exit()


def examine(item_name):
    # combine cart and room items to search both
    all_accessible_items = cart + items_in_room
    target_item = None

    for item in all_accessible_items:
        if item["name"].lower() == item_name.lower():
            target_item = item
            break

    if not target_item:
        print(f"\n You don't see '{item_name}' anywhere in your cart or on the shelves to examine.")
        return

    print(f"\n You closely inspect the {target_item['name']}:")
    if target_item['name'] in ingredients:
        print(" -> It looks fresh, high quality, and perfect for baking a cake!")
    elif target_item['name'] == "Toilet Paper":
        print(" -> It's soft and quilted... but definitely doesn't belong in a mixing bowl.")
    else:
        print(" -> It looks like a great item, but you try to remember if a cake recipe actually calls for this...")


def game_loop():
    global player_money

    for item in items_in_room:
        # this loop keeps the player stuck on the SAME item until they choose to buy (yes) or skip (no)
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            # display current UI
            print(f"WALLET: €{player_money} remaining")
            show_cart()
            print("\n" + "=" * 32)
            print(f"\nYou see: {item['name']} (Price: €{item['price']})")
            print("Options: Type 'yes' to buy, 'no' to skip, or 'examine' to inspect it.")

            # player input
            choice = input(f"Do you want to buy {item['name']}?: ").strip().lower()

            # 'examine' -> show text, then let the loop repeat on the SAME item
            if choice == "examine":
                examine(item["name"])
                input("\nPress Enter to return to choices...")
                continue  # restart loop on the current item!

            # 'yes' -> buy the item, then break to move to the NEXT item
            elif choice == "yes" or choice == "y":
                if player_money >= item["price"]:
                    cart.append(item)
                    player_money -= item["price"]
                    print(f" Added {item['name']} to your cart.")
                    time.sleep(1)
                    break  # breaks the 'while' loop, moves to next item in the 'for' loop
                else:
                    print(f"You can't afford that! You only have €{player_money} left.")
                    time.sleep(1.5)
                    break  # breaks loop and skips because of insufficient budget

            # 'no' -> skip the item, then break to move to the NEXT item
            elif choice == "no" or choice == "n":
                print(f"Skipped {item['name']}.")
                time.sleep(0.5)
                break  # breaks the 'while' loop, moves to next item in the 'for' loop

            # invalid input
            else:
                print("Invalid choice. Please type 'yes', 'no', or 'examine'.")
                time.sleep(1.5)

    checkout()


# last part completely done myself :)
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    type_text(
        "Hi! You will now have 30 seconds to look at the list of ingredients. "
        "Try to remember as many as possible in order to buy all of them at the supermarket and bake a delicious cake!"
    )
    print()

    ready = input("Ready? Type 'yes' or 'no': ").strip().lower()

    if ready == "yes":
        run_memory_phase()
        game_loop()
    else:
        print("\nNo problem! take a deep breath and run the game whenever you're ready.")
