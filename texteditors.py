# Test editor install #
from os import system
import time
index = 1
r='\033[1;91m'
g='\033[1;92m'
y='\033[1;93m'
p='\033[1;95m'
c='\033[1;96m'
b='\033[1;94m'
w='\033[1;97m'

text_editor_list = [g + 'Emacs Text Editor','Joe Text Editor','Jupp Text Editor','Micro Text Editor','Nano Text Editor','Sed Text Editor','Vim Text Editor','Neovim Text Editor','Zile Text Editor'+w]
for i in text_editor_list:
	print (f'{g}{index} . {i}{w}')
	index = index + 1
print ('')

i = 1
while i < 10:

	select = input(g + 'Enter Number You want to install  : '+w)

	if select == '1':
		system('pkg install emacs')
	if select == '2':
		system('pkg install joe')
	if select == '3':
		system('pkg install jupp')
	if select == '4':
		system('pkg install micro')
	if select == '5':
		system('pkg install micro')
	if select == '6':
		system('pkg install nano')
	if select == '7':
		system('pkg install vim')
	if select == '8':
		system('pkg install neo vim')
	if select== '9':
		system('pkg install zile')
	else:
		print (r+'Error '+w)
		time.sleep(0.3)

	print ('')
	time.sleep(0.3)
	back = input (g+'back or next :'+w)

	if back == 'back':
		break
	if back == 'next':
		pass
	else:
		print (r + 'Error' + w)

