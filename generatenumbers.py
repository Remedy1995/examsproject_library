import random
import string

class MySample:
    @staticmethod
    def Generate():
        n = random.random()
        number=n*10000   
        number1=("%.1f" % number).replace(".", "")
        letter=random.choice(string.ascii_uppercase)
        final= str(letter)+number1
        # print(final)
        return final
    # Generate()
    @staticmethod
    def GenerateBookID():
        n = random.random()
        number=n*10000   
        number1=("%.1f" % number).replace(".", "")
        letter="BK"
        return letter+number1

        