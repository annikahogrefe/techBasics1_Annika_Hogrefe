import sys
import time

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#introduction with name input
type_text("welcome to \"grocery shopping with your mum simulator\"")
time.sleep(1)
name = input("what's your name?")
lives = 2
time.sleep(1)
type_text(f"\"hello {name}, this is your mum.\"")
time.sleep(2)

#game over check function
def check_game_over():
    global lives
    if lives <= 0:
        print("\nGAME OVER — your mum is disappointed 😢")
        exit()

# first decision
while True:
    decision1 = input("\"would you like to come grocery shopping with me?\"").lower()

    time.sleep(2)
    if decision1 == "yes":
        type_text("\"great let's go!\"")
        break
    elif decision1 == "no":
        type_text("\"you can't sit in your room all day! c'mon!\"")
        lives -= 1
        break
    else:
        print("user input invalid, please enter yes or no")
check_game_over()
time.sleep(5)

# second decision
while True:
    decision2 = input ("\"how would you like to get there?\" it's a sunny day and the next grocery store is 2km away. you could walk or drive").lower()

    time.sleep(2)
    if decision2 == "walk":
        type_text("\"good choice\"")
        break
    elif decision2 == "drive" :
        type_text("\"ugh... that's so unnecessary and bad for the environment\"")
        lives -= 1
        break
    else:
        print("user input invalid, please enter walk or drive")
check_game_over()
time.sleep(5)

#third decision
type_text(f"\"here we are, {name}, can you get a shopping cart please?\"")
time.sleep(3)
while True:
    decision3 = input ("there are two lines of shopping carts. a short one and a long one. which one do you take your shopping cart from?").lower()
    time.sleep(2)

    if decision3 in ["short", "short one"]:
        type_text ("weird... why not balance it out?")
        lives -= 1
        break
    elif decision3 in ["long", "long one"]:
        type_text ("perfect")
        break
    else:
        print("user input invalid, please enter short or long")
check_game_over()
time.sleep(5)

#fourth decision
type_text("you and your mum enter the grocery store. first up is the aisle with dairy products.")
time.sleep(3)

while True:
    decision4 = input(f"\"how many containers of milk do you think we need, {name}?\" ")

    try:
        decision4 = int(decision4)
    except ValueError:
        print("please enter a valid number")
        continue

    if 0 < decision4 < 5:
        type_text("\"alright!\"")
        break
    elif decision4 >= 5:
        type_text("\"that is too many!\"")
        lives -= 1
        break
    else:
        print("please enter a realistic number")
check_game_over()
time.sleep(5)

#fifth decision
type_text("after getting milk you move on to the next aisle")
time.sleep(2)
while True:
    decision5 = input("\"where do you wanna go next? vegetables or candy?\"").lower()
    time.sleep(2)
    if decision5 == "vegetables":
        decision6 = input("\"oh there is my friend Karen, do you mind if I go talk to her?\"").lower()

        if decision6 == "no":
            type_text("\"thanks! this might take a while...\"")
            time.sleep(20)
        elif decision6 == "yes":
            time.sleep(2)
            type_text("\"fine..., we’ll keep moving then 😢.\"")
            lives -= 1
        else:
            print("please answer yes or no")
            continue

        break

    elif decision5 == "candy":
        time.sleep(2)
        print("\"ooo sweet stuff!\"")
        break

    else:
        print("user input invalid, please enter vegetables or candy")
check_game_over()
time.sleep(5)
#ending
type_text(f"""
you and your mum are waiting in line for checkout.
\"Thanks for coming shopping with me, {name}\"
    """)

time.sleep(7)
type_text("""
\"wait, I think I forgot something...\"
your mum leaves you at the checkout with a full shopping cart and no money.
    """)


#check lives
print(f"""
lives left: {lives}/2
""")

if lives == 2:
    print("perfect shopping trip!")
elif lives == 1:
    print("not bad, but mum is slightly annoyed")
else:
    print("that went terribly...")

#ai use:
# I used chatgpt for debugging (if I got error messages I didn't understand, mostly forgetting a {}, : or , lol) and helping me with the live system and typing effect. please contact me of you want to see the conversation! rest was all done by myself :)
