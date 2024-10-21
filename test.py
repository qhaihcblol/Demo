import time

def countdown():
    value = 100
    while value > 0:
        print(f"Current value: {value}")
        value -= 1
        time.sleep(5)  # Dừng 15 giây trước khi tiếp tục
    print("Countdown finished!")

countdown()
