from os import system
g='\033[1;92m'
w='\033[1;97m'
index = 1
list = [g + 'python3','python2','github','clang','clang++','perl','ruby','kali linux','ubuntu','debian','Kali nethunter','black box','arch linux','nano','micro','import all']
for all in list:
	print (f'{index} . {all}')
	print ('')
	index += 1

i = 1
while i < 17:
	type = input ('Number Next Back : ')
	if type == '1':
		system('pkg install python -y')
	if type == '2':
		system('pkg install python2 -y')
	if type == '3':
		system('pkg install git -y')
	if type == '4':
		system('pkg install clang -y')
	if type == '5':
		system('pkg install clang++ -y')
	if type == '6':
		system('pkg install perl -y')

	if type == '7':
		system('pkg install ruby -y')
	if type == '8':
		system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
	if type == '9':
		system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh')
	if type == '10':
		system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh')
	if type == '11':
		system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh')
	if type == '12':
		system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh')
	if type == '13':
		system('pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh')
	if type == '14':
		system('pkg install nano')
	if type == '15':
		system('pkg install micro')
	if type == '16':
		system('pkg install python2 -y && pkg install python -y &&  pkg install git -y && pkg install ruby -y && pkg install nano -y && pkg install micro -y && pkg install clang && pkg install clang++'+w)
	if type == 'Next':
		pass
	if type == 'Back':
		break
		system('clear')
		system('exit()')
