import time;
import sys;
import colorama;
from colorama import Back, Fore, Style
colorama.init();


def centerWord(string, blankS):
	if(len(string) == 20):
		for bl in range(6):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(6):
		    print(blankS, end="")
	if(len(string) == 19):
		for bl in range(7):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(6):
		    print(blankS, end="")	
	if(len(string) == 18):
		for bl in range(8):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(6):
		    print(blankS, end="")		    	    
	if(len(string) == 17):
		for bl in range(8):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(7):
		    print(blankS, end="")
	if(len(string) == 16):
		for bl in range(8):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(8):
		    print(blankS, end="")
	if(len(string) == 15):
		for bl in range(9):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(8):
		    print(blankS, end="")
	if(len(string) == 14):
		for bl in range(9):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(9):
		    print(blankS, end="")
	if(len(string) == 13):
		for bl in range(10):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(9):
		    print(blankS, end="")	
	if(len(string) == 12):
		for bl in range(10):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(10):
		    print(blankS, end="")
	if(len(string) == 11):
		for bl in range(11):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(10):
		    print(blankS, end="")
	if(len(string) == 10):
		for bl in range(11):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(11):
		    print(blankS, end="")
	if(len(string) == 9):
		for bl in range(12):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(11):
		    print(blankS, end="")	
	if(len(string) == 8):
		for bl in range(12):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(12):
		    print(blankS, end="")
	if(len(string) == 7):
		for bl in range(13):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(12):
		    print(blankS, end="")
	if(len(string) == 6):
		for bl in range(13):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(13):
		    print(blankS, end="")	
	if(len(string) == 5):
		for bl in range(14):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(13):
		    print(blankS, end="")	
	if(len(string) == 4):
		for bl in range(14):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(14):
		    print(blankS, end="")	
	if(len(string) == 3):
		for bl in range(15):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(14):
		    print(blankS, end="")
	if(len(string) == 2):
		for bl in range(15):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(15):
		    print(blankS, end="")	
	if(len(string) == 1):
		for bl in range(16):
			print(blankS,end="")
		print(Fore.RESET+string+Fore.LIGHTRED_EX, end="")
		for bl in range(15):
		    print(blankS, end="")	

def drawHeart(sign, blankS, name):	
    print("\n")
    for bl in range(7):
	    print(Fore.LIGHTRED_EX+ " ", end="")
    for h in range(9):
	    print(sign, end="");
    for bl in range(6):
	    print(blankS,end="")
    for h in range(9):
	    print(sign, end="");	
    print(" ");
    for bl in range(4):
        print(" ",end="")	
    for h in range(3):
        print(sign,end="")   
    for bl in range(9):
        print(blankS, end="")  
    for h in range(1):
        print(sign, end="") 
    for bl in range(4):
        print(blankS,end="")
    for h in range(1):
        print(sign, end="")
    for bl in range(9):
        print(blankS, end="") 
    for h in range(3):
        print(sign,end="")
    print("")
    for bl in range(2):
        print(" ",end="")
    for h in range(2):
        print(sign,end="")
    for bl in range(13):
        print(blankS,end="") 
    for h in range(1):
        print(sign,end="") 
    for bl in range(2):
        print(blankS,end="") 
    for h in range(1):
        print(sign,end="") 
    for bl in range(13):
        print(blankS,end="") 
    for h in range(2):
        print(sign,end="")            
    print("")
    for h in range(2):
        print(sign,end="") 
    for bl in range(16):
        print(blankS,end="") 
    for h in range(2):
        print(sign,end="")  
    for bl in range(16):
        print(blankS,end="") 
    for h in range(2):
        print(sign,end="") 
    print("")
    for h in range(2):
        print(sign,end="")
    for bl in range(34):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="") 
    print("")
    for h in range(2):
        print(sign,end="")
    for bl in range(34):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="") 
    print("")
    for h in range(2):
        print(sign,end="")
    for bl in range(34):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="") 
    print("")
    for h in range(2):
        print(sign,end="")
    for bl in range(34):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="") 
    #============================
    print("")
    for bl in range(1):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    if name == "":
        for bl in range(32):
            print(" ",end="")  
    else:
        centerWord(name, blankS)                            

    for h in range(2):
        print(sign,end="")  
    #=====================
    print("")
    for bl in range(2):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(30):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="")
    print("")
    for bl in range(3):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(28):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="")
    print("")
    for bl in range(5):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(24):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="")
    print("")
    for bl in range(7):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(20):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="") 
    print("")
    for bl in range(9):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(16):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="")  
    print("")
    for bl in range(11):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(12):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="")
    print("")
    for bl in range(13):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(8):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="") 
    print("")
    for bl in range(15):
        print(" ",end="")
    for h in range(2):
        print(sign,end="") 
    for bl in range(4):
        print(blankS,end="")
    for h in range(2):
        print(sign,end="")
    print("")
    for bl in range(17):
        print(" ",end="")
    for h in range(4):
        print(sign,end="") 
    print("\n") 
    mess =  "You are a very special person to me, ";
    for i in mess:
    	print(Fore.LIGHTCYAN_EX +i,end="");
    	time.sleep(0.1);
    for i in name:
    	print(Fore.RESET +i,end="");
    	time.sleep(0.1);    	
    print("\n") 

kitu = input("Kí tự cho trái tim: ");
while len(kitu) > 1:
    kitu = input("Kí tự cho trái tim (Không quá 1 kí tự): ");
if(len(kitu) ==0):
    kitu = "o"       	

kituBlank = input("Kí tự chỗ trống của trái tim: ");
while len(kituBlank) > 1 or kitu == kituBlank:
    kituBlank = input("Kí tự chỗ trống của trái tim (Không quá 1 kí tự hoặc không được giống kí tự cho trái tim): ");
if(len(kituBlank) == 0):
    kituBlank = " " 
ten = "" 
while len(ten) == 0 or len(ten) > 20:
	ten = input("Tên (Không được bỏ trống hay quá 20 kí tự): ");   	
drawHeart(kitu, kituBlank,ten);	
                                                                                                                                        