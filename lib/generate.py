import random
from tqdm import tqdm
import os

def chngedir():
    try:
        os.mkdir("./output")
    except FileExistsError:
        pass
    os.chdir("./output")

pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
         '9', '0', '!', '@', '#', '$', '%', '^', '&', '*',
         '(', ')']

pass2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
         '9', '0']

pass3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']

pass4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z']

pin1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

password = ""

def blockgen(block):
    bck = ""
    for b in range(0, block):
        bck = bck + "9"
    print("block generate")
    return bck


class rand_generator():
    def pass_all_gen(lenghts, passnumber, filename):
        chngedir()
        f1 = open(str(filename), "w")
        f1.close()
        file = open(filename, "w")
        for i in tqdm(range(int(passnumber))):
            password = ""
            for x in range(0, int(lenghts)):
                password = password + random.choice(pass1)
            file.write(password + "\n")
        file.close()
    def pass_numb_gen(lenghts, passnumber, filename):
        chngedir()
        f1 = open(str(filename), "w")
        f1.close()
        file = open(filename, "w")
        for i in tqdm(range(int(passnumber))):
            password = ""
            for x in range(0, int(lenghts)):
                password = password + random.choice(pin1)
            file.write(password + "\n")
        file.close()
    def pass_onlyletter_gen(lenghts, passnumber, filename):
        chngedir()
        f1 = open(str(filename), "w")
        f1.close()
        file = open(filename, "w")
        for i in tqdm(range(int(passnumber))):
            password = ""
            for x in range(0, int(lenghts)):
                password = password + random.choice(pass4)
            file.write(password + "\n")
        file.close()
    def pass_onlymin_gen(lenghts, passnumber, filename):
        chngedir()
        f1 = open(str(filename), "w")
        f1.close()
        file = open(filename, "w")
        for i in tqdm(range(int(passnumber))):
            password = ""
            for x in range(0, int(passnumber)):
                password = password + random.choice(pass3)
            file.write(password + "\n")
        file.close()
    def pass_nosign_gen(lenghts, passnumber, filename):
        chngedir()
        f1 = open(str(filename), "w")
        f1.close()
        file = open(filename, "w")
        for i in tqdm(range(int(passnumber))):
            password = ""
            for x in range(0, int(lenghts)):
                password = password + random.choice(pass2)
            file.write(password + "\n")
        file.close()
