import os
import random
from time import time

class BuilderBrute:
    def __init__(self):
        self.name_file = ""
        self.letters = ""
        self.rejected = 0
        self.accepted = 0
        self.start_time = time()
        self.words_set = set()
        self.buffer_size = 150
        self.buffer = []

    def create_txt(self) -> None:
        with open(self.name_file, "w"):
            pass

    def get_word(self, now: int, now2: int) -> str:
        length = random.randint(now, now2)
        return ''.join(random.choices(self.letters, k=length))

    def get_words(self) -> set[str]:
        try:
            with open(self.name_file, "r") as txt:
                return set(txt.read().split())
        except FileNotFoundError:
            self.create_txt()
            return set()

    def write_buffer(self) -> None:
        with open(self.name_file, "a") as txt:
            txt.write("\n".join(self.buffer) + "\n")
        self.buffer.clear()

    def write(self, word: str) -> None:
        self.buffer.append(word)
        if len(self.buffer) >= self.buffer_size:
            self.write_buffer()

    def clear(self) -> None:
        with open(self.name_file, "w"):
            pass
        self.words_set.clear()

    def checker(self) -> None:
        with open(self.name_file, "r") as txt:
            if input("word: ") in txt.read().split():
                print("Found!")
            else:
                print("Not Found")

    def main(self, now: int, now2: int) -> None:
        self.words_set = self.get_words()
        while True:
            word = self.get_word(now, now2)
            if word in self.words_set or word[0] in ("-", "_"):
                self.rejected += 1
            else:
                self.write(word)
                self.words_set.add(word)
                print(word, end=", ", flush=True)
                self.accepted += 1

            elapsed_time = time() - self.start_time
            accepted_per_second = self.accepted / elapsed_time if elapsed_time > 0 else 0
            rejected_per_second = self.rejected / elapsed_time if elapsed_time > 0 else 0

            os.system(
                f"title rejected: {self.rejected}    "
                f"accepted: {self.accepted}    "
                f"rejected/s: {rejected_per_second:.2f}    "
                f"accepted/s: {accepted_per_second:.2f}"
            )

if __name__ == '__main__':
    builder = BuilderBrute()
    builder.name_file = input("name file: ") + ".txt"
    if input("use checker db? (y/n): ") == "y":
        builder.checker()
        input("...")
    else:
        if input("use default letters? (y/n): ") == "y":
            builder.letters = "1234567890qwertyuiopasdfghjklzxcvbnm-_QWERTYUIOPASDFGHJKLZXCVBNM"
        else:
            builder.letters = input("input new letters: ")
        builder.main(int(input("min: ")), int(input("max: ")))
