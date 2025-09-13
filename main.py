import random
import json
import time
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

with open('queries.json', 'r') as f:
    data = json.load(f)

def click():
    mouse.click(Button.left, 1)

def scroll_down_up():
    steps = random.randint(1, 6)
    for _ in range(steps):
        mouse.scroll(0, -1)
        time.sleep(0.1)
    time.sleep(0.5)
    for _ in range(steps):
        mouse.scroll(0, 1)
        time.sleep(0.1)

def key_presses(num_lines):
    for i, line in enumerate(data["query"]):
        if i >= num_lines:
            break
        for char in line:
            keyboard.press(char)
            keyboard.release(char)
            ran = random.randint(1,10)
            ran =  ran/3
            time.sleep(ran)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        scroll_down_up()
        click()

        delay_between = random.uniform(4, 8)  

def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input.lstrip("-").isdigit():
                print("Not an integer. Try again.")
                continue
            return int(user_input)
        except ValueError:
            print("ValueError occurred. Exiting.")
            return None

def run_bot(num_queries):
    time.sleep(5)
    key_presses(num_queries)

if __name__ == "__main__":
    num_queries = get_integer_input("Enter how many queries to type: ")
    if num_queries is None or num_queries <= 0:
        print("Invalid number of queries. Exiting.")
        exit()

    run_bot(num_queries)
