import time

def countdown():
    value = 100
    while value > 0:
        print(f"Current value: {value}")
        value -= 1
        time.sleep(3)
    print("Countdown finished!")

countdown()
