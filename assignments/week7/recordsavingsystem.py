# added the record saving system to my game from week 6
# I'm a bit unsure about the order of all my things, it seems so messy but it work haha
# did some stuff such as the timestamp, sorting and leaderboard UI with help of gemini
# added a (NEW!) after the newly added stuff for the record saving system to make it easier to find the relevant parts for you so watch out :)

import csv
from datetime import datetime
import os
import sys
import time

# leaderboard csv & debug (NEW!)
FILENAME = "leaderboard.csv"
DEBUG = True  # set to true to skip/ false to play the game normally!
# ----------------------------------

# ingredients list
ingredients = [
    "Flour",
    "Milk",
    "Sugar",
    "Eggs",
    "Baking Soda",
    "Butter",
]


# animated typing effect
def type_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# the 30-second memory countdown
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

    print("\n" * 100)
    os.system("cls" if os.name == "nt" else "clear")

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
player_money = 20


# record saving system (NEW!)
def save_and_update_leaderboard(player_name, score):
    records = []

    # try block for opening/reading the file safely
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # skip CSV header
                for row in reader:
                    if row:
                        records.append([row[0], row[1], int(row[2])])
        except (IOError, ValueError, IndexError) as e:
            print(f"\n[Notice] Could not load past leaderboard data safely ({e}). Starting fresh.")
            records = []

    # get standard timestamp string
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # append current game record
    records.append([player_name, timestamp, score])

    # sort records (highest score first)
    records.sort(key=lambda x: x[2], reverse=True)

    # try block for writing the updated list back to the csv file
    try:
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Timestamp", "Score"])
            writer.writerows(records)
    except IOError as e:
        print(f"\n[Error] Unable to save your score to the file: {e}")

    # display clean leaderboard UI
    print("\n" + "=" * 20 + " LEADERBOARD " + "=" * 20)
    print(f"{'Rank':<6}{'Name':<15}{'Timestamp':<22}{'Score':<10}")
    print("-" * 53)
    for rank, record in enumerate(records, start=1):
        print(f"{rank:<6}{record[0]:<15}{record[1]:<22}{record[2]:<10}")
    print("=" * 53)

# old functions
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

    # calculate final score based on cart performance (NEW!)
    final_score = (len(correct_items) * 100) - (len(wrong_items) * 50)
    print(f"\nYour Final Score: {final_score} points")

    # ask for name and pass data to our assignment system (NEW!)
    # these were done completely by myself with no help of AI
    player_name = input("\nEnter your name for the Leaderboard: ").strip()
    if not player_name:
        player_name = "Anonymous Player"

    save_and_update_leaderboard(player_name, final_score)
    print("\nThanks for playing!")


def examine(item_name):
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
    if target_item["name"] in ingredients:
        print(" -> It looks fresh, high quality, and perfect for baking a cake!")
    elif target_item["name"] == "Toilet Paper":
        print(" -> It's soft and quilted... but definitely doesn't belong in a mixing bowl.")
    else:
        print(" -> It looks like a great item, but you try to remember if a cake recipe actually calls for this...")


def game_loop():
    global player_money

    for item in items_in_room:
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print(f"WALLET: €{player_money} remaining")
            show_cart()
            print("\n" + "=" * 32)
            print(f"\nYou see: {item['name']} (Price: €{item['price']})")
            print("Options: Type 'yes' to buy, 'no' to skip, or 'examine' to inspect it.")

            choice = input(f"Do you want to buy {item['name']}?: ").strip().lower()

            if choice == "examine":
                examine(item["name"])
                input("\nPress Enter to return to choices...")
                continue

            elif choice == "yes" or choice == "y":
                if player_money >= item["price"]:
                    cart.append(item)
                    player_money -= item["price"]
                    print(f" Added {item['name']} to your cart.")
                    time.sleep(1)
                    break
                else:
                    print(f"You can't afford that! You only have €{player_money} left.")
                    time.sleep(1.5)
                    break

            elif choice == "no" or choice == "n":
                print(f"Skipped {item['name']}.")
                time.sleep(0.5)
                break

            else:
                print("Invalid choice. Please type 'yes', 'no', or 'examine'.")
                time.sleep(1.5)

    checkout()


# main operational block (FIRST PART NEW!)
def start_game():
    if DEBUG:
        print("[DEBUG MODE ACTIVE] Skipping main gameplay loops.")
        test_name = input("Enter your name for debug testing: ").strip()
        if not test_name:
            test_name = "Tester"
        save_and_update_leaderboard(test_name, 999)
        return

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


if __name__ == "__main__":
    start_game()
