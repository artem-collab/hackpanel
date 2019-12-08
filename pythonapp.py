
from modules.module import *
import os
def menu():
        print("01:exploit")
        print("02:ddos")
        print("03:spam")
        menu=input()
        if menu == '01':
                os.system('clear')
                print("01:metasploit")
                print("02:websploit")
                print("03:routersploit")
                print("04:darkfly")
                exploit=input()
                if exploit == '01' 
                        metasploit()
                elif exploit == '02':
                        websploit()
                elif exploit == '03':
                        route()
elif exploit == '04':
                        dark()
                else:
                        print('ошибка в написание"
        elif menu == '02':
                print("01:xerxes")
                print("02:routersploit")
print("03:goldeneye")
                dos=input()
                if dos == '01':
                        xer()
                elif dos == '02':
                        sdos()
                elif dos == '03':
                        gold()
                else:
                        print("ошибка в написание")
        elif menu == '03':
                os.system('clear')
                print("1:flood")
                flood=input()
                if flood == '01':
                        flood()
                else:
                        print("извините но в спа")
else:
                print("ошибка!!!")

if __name__ == '__main__':
        menu()
