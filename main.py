import os
import random


class BuilderBrute:
    def __init__(self):
        self.name_file = input("name file: ") + ".txt"
        if input("use default letters? (y/n): ") == "y":
            self.letters = "1234567890qwertyuiopasdfghjklzxcvbnm-_QWERTYUIOPASDFGHJKLZXCVBNM"
        else:
            self.letters = input("input new letters: ")
        self.words = str(self.get_words()).split()
        self.rejected = 0

    def create_txt(self) -> None:
        with open(self.name_file, "w"):
            pass

    def get_word(self, now: int, now2: int) -> str:
        length = random.randint(now, now2)
        return ''.join(random.choices(self.letters, k=length))

    def get_words(self) -> list[str]:
        try:
            with open(self.name_file, "r") as txt:
                return txt.read().split()
        except:
            self.create_txt()
            return []

    def write(self, word: str) -> None:
        with open(self.name_file, "a") as txt:
            txt.write(word + "\n")

    def clear(self) -> None:
        with open(self.name_file, "w"):
            pass

    def checker(self) -> None:
        with open(self.name_file, "r") as txt:
            if input("word: ") in txt.read().split():
                print("Found!")
            else:
                print("Not Found")

    def main(self, now: int, now2) -> None:
        while True:
            word = self.get_word(now, now2)
            if word in self.words or word[0] in ("-", "_"):
                print("rejected")
                self.rejected += 1
                os.system("title rejected: " + str(self.rejected))
            else:
                self.write(word)
                self.words.append(word)
                print(word)


if __name__ == '__main__':
    builder = BuilderBrute()
    if input("use checker db? (y/n): ") == "y":
        builder.checker()
        input("...")
    else:

        builder.main(int(input("min: ")), int(input("max: ")))
