#Last Update : Dec 30, 2017
#Linux
#Testing
#Colorless
import os
import sys
import time
import traceback
os.system('clear')
print"This portion of the script will install or update Netcat in your device.\n"
print"Please Proceed.\n"
os.system('sudo apt-get install netcat')
os.system('sleep 2')
os.system('clear')
print"Netcat is successfully installed/updated\n"
print"\nPlease wait.."
os.system('sleep 2')
#Lolomokalbo - GrandFather
banner='''
##        #####   ##       #####   ###    ###   #####
##      ##     ## ##     ##     ## ## #  # ## ##     ##
##      ##     ## ##     ##     ## ##  ##  ## ##     ##    K A L B O !
##      ##     ## ##     ##     ## ##      ## ##     ##
########  #####   #######  #####   ##      ##   #####
=======================================================================\n
'''
#Game!
haha="Putangina mag antay kayo ng konti.\n"
cl="clear"
s1="sleep 1"
ca=''
da=''
ea=''
fa=''
#lololol
def a():
    os.system(cl)
    print banner
    os.system('sleep 2')
    os.system('clear')
    print "This is just a testing tool for Netcat users.\n"
    os.system('sleep 2')
    os.system('clear')

def b():
    print banner
    print"Usage : python lolomokalbo.py [mode] v\n "
    pirnt"[Modes (isa lang)]:
    print"[+] 1 - Port Scanner\n"
    print"[+] 2 - Port Banners Grabber (Single)\n"
    print"[+] 3 - BackConnect \n"
    print"[+] 4 - Port Banners Grabber (Multiple)\n"
    print"[+] h - Help\n"
    print"[+] v - Verbose Mode [example : python lolomokalbo.py 1 v]\n"
    sys.exit()

def c():
    try:
        os.system(cl)
        os.system(s1)
        print banner
        print" Port Scanner PUTA\n"
        ca = raw_input("Target mo putangina ka (IP/Host): ")
        cb = raw_input("Anong ports na i-iiscan puta ka (From - To): ")
        cc = "nc -v -w2 -z "+ca+" "+cb
        print"=======================================================================\n"
        print'Puta nagsimula na! @ [',time.strftime("%X"),']\n'
        print haha
        if len(sys.argv)== 3:
            if sys.argv[2]=="v":
                cc = "nc -v -v -w2 -z "+ca+" "+cb
        os.system(cc)
    except KeyboardInterrupt:
        print "\n\n\n\nPutangina mo salamat sa pag gamit sa pipitsugin kong tool gago."
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

def d():
    try:
        os.system(cl)
        os.system(s1)
        print banner
        print "Port Banners Grabber putangina mo\n"
        da = raw_input("Target mo putangina ka (IP/Host): ")
        db = raw_input("Anong Port putangina mo: ")
        dc = "nc -v -n "+da+" "+db
        print"========================================================================\n"
        print'Puta nagsimula na! @ [',time.strftime("%X"),']\n'
        print haha
        if len(sys.argv)== 3:
            if sys.argv[2]=="v":
                dc = "nc -v -v -n "+da+" "+db
        os.system(dc)
    except KeyboardInterrupt:
        print "\n\n\n\nPutangina mo salamat sa pag gamit sa pipitsugin kong tool gago."
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

def e():
    try:
        os.system(cl)
        os.system(s1)
        print banner
        print"Back Connect para sa mga putanginang shell mo. Iroot mo gago\n"
        ea = raw_input("Port :")
        eb = "nc -l -n -v -p "+ea
        print"========================================================================\n"
        print'Puta nagsimula na! @ [',time.strftime("%X"),']\n'
        print haha
        if len(sys.argv)== 3:
            if sys.argv[2]=="v":
                eb = "nc -l -n -v -v -p"+ea
        os.system(eb)
    except KeyboardInterrupt:
        print "\n\n\n\nPutangina mo salamat sa pag gamit sa pipitsugin kong tool gago."
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

def f():
    try:
        os.system(cl)
        os.system(s1)
        print banner
        print "Ports Banners Grabber para sa pangmaramihang ports putangina ka\n"
        fa = raw_input("Target mo putangina ka (IP/Host): ")
        fb = raw_input("Mula at Hanggang saang port putangina mo (From - To): ")
        fc = "echo '' | nc -v -n -w1 "+fa+" "+fb
        print"========================================================================\n"
        print'Puta nagsimula na! @ [',time.strftime("%X"),']\n'
        print haha
        if len(sys.argv)== 3:
            if sys.argv[2]=="v":
                fc = "echo '' | nc -n -v -v -w1"+fa+" "+fb
        os.system(fc)
    except KeyboardInterrupt:
        print "\n\n\n\nPutangina mo salamat sa pag gamit sa pipitsugin kong tool gago."
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

#Jombag HAHA
if len(sys.argv) <2:
    a()
    b()
else:
    if sys.argv[1]=="h":
        b()
    elif sys.argv[1]=="1":
        c()
    elif sys.argv[1]=="2":
        d()
    elif sys.argv[1]=="3":
        e()
    elif sys.argv[1]=="4":
        f()
