import random
import os
import sys
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
def message():
    clear()
    while True:
        print("█████████╗███████╗██╗░░██╗████████╗")
        print(" ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝")
        print(" ░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░")
        print(" ░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░")
        print(" ░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░")
        print(" ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░")
        print()            
        print("░██████╗███████╗░█████╗░██╗░░░██╗██████╗░███████╗")
        print("██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔════╝")
        print("╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝█████╗░░")
        print("░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██╔══╝░░")
        print("██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║███████╗")
        print("╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝")
        print("**********************")
        print(" 1. 🇪🇳🇨🇷🇾🇵🇹 🇲🇪🇸🇸🇦🇬🇪\n 2. 🇩🇪🇨🇷🇾🇵🇹 🇲​​​​​🇪​​​​​🇸​​​​​🇸​​​​​🇦​​​​​🇬​​​​​🇪​​​​​\n 3. 🇪🇽🇮🇹")
        print("**********************")
        try:
            user = int(input("Enter Here : "))
            if user == 1:
                def encrypt():
                    encode = input("Enter Your message : ")
                    print()
                    l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                    fake_message = ["/@encrypt85ut","#encsms15uyg","#.security63ygf","kjse000fd"]
                    enum = ["/A/","/B/","/C/","/D/","/E/","/F/","/G/","/H/","/I/","/J/"]
                    lcount = 0
                    message = []
                    encrypted = []
                    encrypt = []

                    if len(encode) >= 3:
                        for i in encode:
                            encrypt.append(i)
                        encrypt.append(encrypt[0])
                        encrypt.remove(encrypt[0])
                        # add 3 random alphabet in message list
                        while lcount<3:
                            x = random.randrange(0, 25)
                            message.append(l[x])
                            lcount += 1
                        # add modify message in message list
                        for j in encrypt:
                            message.append(j)
                        lcount = 0
                        # add 3 random alphabet after adding main modify message in message list 
                        while lcount<3:
                            x = random.randrange(0, 25)
                            message.append(l[x])
                            lcount += 1
                        message.reverse()
                        # show encrypted message on your screen
                        for k in message:
                            if k == " ":
                                vm = random.randrange(0, 2)
                                encrypted.append(fake_message[vm])
                            elif k =="0":
                                encrypted.append(enum[0])
                            elif k =="1":
                                encrypted.append(enum[1])
                            elif k =="2":
                                encrypted.append(enum[2])
                            elif k =="3":
                                encrypted.append(enum[3])
                            elif k =="4":
                                encrypted.append(enum[4])
                            elif k =="5":
                                encrypted.append(enum[5])
                            elif k =="6":
                                encrypted.append(enum[6])
                            elif k =="7":
                                encrypted.append(enum[7])
                            elif k =="8":
                                encrypted.append(enum[8])
                            elif k =="9":
                                encrypted.append(enum[9])
                            else:
                                encrypted.append(k)
                        for i in encrypted:
                            print(i, end="")
                    else:
                        for i in encode:
                            encrypted.append(i)
                        encrypted.reverse()
                        for i in encrypted:
                            print(i, end="")
                    print("")
                    wait = input("\n🇲🇪🇸🇸🇦🇬🇪 🇪🇳🇨🇷🇾🇵🇹🇪🇩 🇸🇺🇨🇨🇪🇸🇸🇫🇺🇾!\nPress any key to continue.")
                    clear()
                encrypt()
            elif user == 2:
                def decrypt():
                    x = 0
                    decrypted = ""
                    fake_message = ["/@encrypt85ut","#encsms15uyg","#.security63ygf","kjse000fd"]
                    enum = ["/A/","/B/","/C/","/D/","/E/","/F/","/G/","/H/","/I/","/J/"]
                    decode = input("Enter Encrypted message : ")
                    print()
                    if len(decode)>=3:
                        for fm in fake_message:
                            decoded = decode.find(fm)
                            if decoded != -1:
                                decode = decode.replace(fm, " ")
                            else:
                                continue 
                        decode = list(decode)
                        del decode[0:3]
                        decode.reverse()
                        del decode[0:3]
                        decode.insert(0, decode[-1])
                        decode.pop()
                        for convert in decode:
                            decrypted += convert
                        for dnum in enum:
                            decode = decrypted.find(dnum)
                            if decode != -1:
                                decrypted = decrypted.replace(enum[0], "0")
                                decrypted = decrypted.replace(enum[1], "1")
                                decrypted = decrypted.replace(enum[2], "2")
                                decrypted = decrypted.replace(enum[3], "3")
                                decrypted = decrypted.replace(enum[4], "4")
                                decrypted = decrypted.replace(enum[5], "5")
                                decrypted = decrypted.replace(enum[6], "6")
                                decrypted = decrypted.replace(enum[7], "7")
                                decrypted = decrypted.replace(enum[8], "8")
                                decrypted = decrypted.replace(enum[9], "9")
                            else:
                                continue
                        print(decrypted)
                    else:
                        decode = list(decode)
                        decode.reverse()
                        for i in decode:
                            print(i, end="")
                    wait = input("\n🇲🇪🇸🇸🇦🇬🇪 🇩🇪🇨🇷🇾🇵🇹🇪🇩 🇸🇺🇨🇨🇪🇸🇸🇫🇺🇾!\nPress any key to continue.")
                    clear()
                decrypt()
            elif user == 3:
                sys.exit()
            else:
                message()
        except ValueError:
            print("Invalid input")
            time.sleep(2)
            clear()
message()