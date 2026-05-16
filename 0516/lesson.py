import random


def guess_number_game():
    print("歡迎來到猜數字遊戲！")
    print("我已經想好了一個 1 到 100 的整數，你可以開始猜了。")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess_text = input("請輸入你的猜測（1-100）：")
        attempts += 1

        if not guess_text.isdigit():
            print("請輸入有效的整數。")
            continue

        guess = int(guess_text)
        if guess < 1 or guess > 100:
            print("請輸入 1 到 100 之間的數字。")
            continue

        if guess < target:
            print("太小了，再試一次！")
        elif guess > target:
            print("太大了，再試一次！")
        else:
            print(f"恭喜你！答對了，答案就是 {target}。")
            print(f"你總共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    guess_number_game()
