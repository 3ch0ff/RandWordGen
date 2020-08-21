from lib.generate import rand_generator
import os
import random

try:
    import pyfiglet
    print("pyfiglet library >> \033[0;92mOK\033[0;97m\n")
except ImportError:
    print("pyfiglet library >> \033[0;91mNOT FIND\033[0;97m\n")
    os.system("python3 -m pip install -u pip && python3 -m pip install pyfiglet")

os.system("clear")


def banner(word):
    b__ = pyfiglet.figlet_format(str(word), font="slant")
    color = random.randint(1, 7)
    print("\033[0;9{0}m{1}\033[0;97m".format(color, b__))


def main():
    try:
        print("*******************************************************************")
        banner("RandWordGen")
        print("*******************************************************************")
        print("\t\t\tdeveloped by 3ch0ff")
        types = "rand"
        exstensions = input("\ninsert wordlist extension\n [ txt, dict, dicc ]\n>>>--: ")
        var = True
        while var is True:
            if exstensions == "txt" or exstensions == "dict" or exstensions == "dicc":
                var = False
            else:
                print("\033[0;91mError\033[0;97m -> insert valid wordlist extension")
                exstensions = input("insert wordlist extension\n [ txt, dict, dicc ]\n>>>--: ")
        wordlist_name = input("\ninsert wordlist name\n>>>--: ")
        passwd_lenghts = input("\ninsert password lenght\n [ 2, 3, etc ]\n>>>--: ")
        while passwd_lenghts < "2":
            print("\033[0;91mError\033[0;97m -> 0 and 1 isn't supported lenghts")
            passwd_lenghts = input("\ninsert password lenght\n [ 2, 3, etc ]\n>>>--: ")
        if types == "rand":
            file = wordlist_name + "." + exstensions
            wordlist_lenghts = input("\ninsert wordlist lenght\n [ 100, 1000, etc ]\n>>>--: ")
            while wordlist_lenghts < "1":
                print("\033[0;91mError\033[0;97m -> 0 isn't supported lenght")
                wordlist_lenghts = input("\ninsert wordlist lenght\n [ 100, 1000, etc ]\n>>>--: ")
            dicts = input(
                "insert which dictionary you want\n [ \n 1 : numeric ,\n 2 : alpha-numeric,\n 3 : all,\n 4 : alphabet ,\n 5 : lowercase-alphabet ]\n>>>--: ")
            var = True
            while var is True:
                if dicts == "numeric" or dicts == "alphabet" or dicts == "alpha-numeric" or dicts == "all" or dicts == "lowercase-alphabet" or dicts == "1" or dicts == "2" or dicts == "3" or dicts == "4" or dicts == "5" :
                    var = False
                else:
                    print("insert valid dict")
                    dicts = input(
                        "insert which dictionary you want\n [ \n 1 : numeric ,\n 2 : alpha-numeric,\n 3 : all,\n 4 : alphabet ,\n 5 : lowercase-alphabet ]\n>>>--: ")
            if dicts == "numeric" or dicts == "1":
                print("#------------ start generate wordlist ------------#")
                rand_generator.pass_numb_gen(passwd_lenghts, wordlist_lenghts, file)
                print("{} : \033[0;92mDONE\033[0;97m".format(file))
                print("#------------ end generate wordlist ------------#")
            elif dicts == "alpha-numeric" or dicts == "2":
                print("#------------ start generate wordlist ------------#")
                rand_generator.pass_nosign_gen(passwd_lenghts, wordlist_lenghts, file)
                print("{} : \033[0;92mDONE\033[0;97m".format(file))
                print("#------------ end generate wordlist ------------#")
            elif dicts == "all" or dicts == "3":
                print("#------------ start generate wordlist ------------#")
                rand_generator.pass_all_gen(passwd_lenghts, wordlist_lenghts, file)
                print("{} : \033[0;92mDONE\033[0;97m".format(file))
                print("#------------ end generate wordlist ------------#")
            elif dicts == "alphabet" or dicts == "4":
                print("#------------ start generate wordlist ------------#")
                rand_generator.pass_onlyletter_gen(passwd_lenghts, wordlist_lenghts, file)
                print("{} : \033[0;92mDONE\033[0;97m".format(file))
                print("#------------ end generate wordlist ------------#")
            elif dicts == "lowercase-alphabet" or dicts == "5":
                print("#------------ start generate wordlist ------------#")
                rand_generator.pass_onlymin_gen(passwd_lenghts, wordlist_lenghts, file)
                print("{} : \033[0;92mDONE\033[0;97m".format(file))
                print("#------------ end generate wordlist ------------#")
            else:
                pass
    except KeyboardInterrupt:
        os.system("clear")
        print("Goodbye!")
main()
