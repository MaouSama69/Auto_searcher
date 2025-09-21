from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController
import random
import json
import time

keyboard = KeyboardController()
mouse = MouseController()

def load_queries(file_path="queries.json"):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        if "query" not in data or not isinstance(data["query"], list):
            raise KeyError("queries.json is empty!!!")
        return data["query"]
    except Exception as e:
        print(f"Error loading queries!!! {e}")
        exit(1)

def click():
    mouse.click(Button.left, 1)

def scroll_down_up():
    scrolls = random.randint(1, 5)
    for x in range(scrolls):
        mouse.scroll(0, -1)
        time.sleep(0.05)
    time.sleep(0.3)
    for x in range(scrolls):
        mouse.scroll(0, 1)
        time.sleep(0.05)

def key_presses(queries, num_lines):
    random.shuffle(queries)

    for i, line in enumerate(queries[:num_lines]):
        for char in line:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(random.uniform(0.1, 0.2))

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        scroll_down_up()
        click()

        time.sleep(random.uniform(0.5, 1.0))

        keyboard.press(Key.ctrl)
        keyboard.press('a')
        keyboard.release('a')
        keyboard.release(Key.ctrl)

        keyboard.press(Key.delete)
        keyboard.release(Key.delete)

        time.sleep(random.uniform(1, 2))

def rrun_number(num):
    while True:
        user_input = input(num)
        if not user_input.isdigit():
            print("Not a valid positive integer, Try again!!!")
            continue
        value = int(user_input)
        if value <= 0:
            print("Number must be greater than 0!!!")
            continue
        return value

def run_bot(num_qreis):
    print("Bot will start in 5 seconds. Place your cursor in the search bar...")
    time.sleep(5)
    queries = load_queries()
    key_presses(queries, num_qreis)

if __name__ == "__main__":
    queries_n = rrun_number("Enter how many queries to type: ")
    run_bot(queries_n)
