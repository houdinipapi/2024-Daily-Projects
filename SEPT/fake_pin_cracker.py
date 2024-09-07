import time
import random


def fake_pin_cracker(correct_pin):
    print("Starting the fake pin cracking process...\n")

    for attempt in range(1000, 10000):  # Loop through all possible 4 digit pins
        print(f"Trying PIN: {attempt}")
        time.sleep(0.01)  # Simulate time delay for each attempt

        if attempt == correct_pin:
            print(f"\nPIN cracked! The correct PIN is: {attempt}")
            break
        else:
            print("\nFailed to crack the PIN.")  # Just in case t loops through all without matching


# Simulate a random 4-digit correct pin
correct_pin = random.randint(1000, 9999)
fake_pin_cracker(correct_pin)