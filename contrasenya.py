import re

class Password:
    def llegeix_password() -> str:
        correcte = 0
        while not (correcte):
            print("Entra Password: ")
            password = input()
            if (len(password) >= 8) and (re.search("[a-z]", password)) and (re.search("[0-9]", password)):
                correcte = 1
        return correcte
