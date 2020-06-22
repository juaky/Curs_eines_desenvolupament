import re

class Password:
    def llegeix_password() -> str:
        correcte = 0
        while not (correcte):
            print("Entra Password: ")
            password = input()
            if (len(password) >= 10) and \
                    (re.search("[a-z]", password)) and \
                    (re.search("[0-9]+", password)) and \
                    (re.search("[A-Z]", password)) and \
                    (re.search("[_@$]", password)):
                correcte = 1
        return correcte
