import os
import subprocess
# instruction list from https://www.felixcloutier.com/x86/

def print_sbin():
	print "[+] hello! this is the sbin folder"
	print "You can choose one file to find instruction statistics"
	print "----------------------------------------------------------------"
	os.system("ls /sbin")
	print "----------------------------------------------------------------"

def wanted_binary(filename):
	ret = subprocess.check_output(["objdump","-d", filename])
	return ret

print_sbin()
filename = raw_input("Wanted File: ")

want = wanted_binary("/sbin/" + filename)

wantlen = want.count('\n')
print "[+] objdump line: " + str(wantlen)
dic = {}

# splited = want.split(" ")

print "[+] Wait a Second... I'm finding all instruction~~"
print "[-] If instruction line is more than 20000, you have to wait more than 20s.."

for i in range(wantlen):
	line = want.split('\n')[i]
	# print line

	if line == '':
		continue
	if  line.count('\t') == 1 or line.count('\t') == 0: 
		continue
	ins = line.split('\t')[2].split()[0]

	if dic.get(ins)==None:
		dic[ins]=1	# dictionary insert
	else:
		dic[ins] = dic[ins] + 1

print dic
