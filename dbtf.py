import os, sys, requests
site = sys.argv[1]
try:
	wl = sys.argv[2]
	wordlist = open(wl, 'r')
	print(f'\033[1;33mWordList carregada - {wl}')
except Exception as e:
	wordlist = open('common.txt', 'r')
	print(f'\033[1;33mWordList carregada - diretorios.txt')
print('''
$$$$$$$\  $$$$$$$\ $$$$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\\__$$  __|$$  _____|
$$ |  $$ |$$ |  $$ |  $$ |   $$ |      
$$ |  $$ |$$$$$$$\ |  $$ |   $$$$$\    
$$ |  $$ |$$  __$$\   $$ |   $$  __|   
$$ |  $$ |$$ |  $$ |  $$ |   $$ |      
$$$$$$$  |$$$$$$$  |  $$ |   $$ |      
\_______/ \_______/   \__|   \__|      
                                       
                        Directory Brute Forcer - DBTF               





''')
hits = open('hits.txt', 'a')
for lines in wordlist:
	attemps = lines.strip('\n')
	site_req = str(site + '/' + attemps)
	try:
		r = requests.get('https://' + site_req)
		erro_ = range(400, 499)
		sucesso_ = range(200, 299)
		redirect = range(300, 399)
		erro_site = range(500, 599)
		informativa = range(100, 199)
		if r.status_code in erro_:
			print(f'\033[1;31mDiretório não accesível para o site "{site}" | Código de retorno - "{r.status_code}" | Diretório testado - "{site_req}"')
		elif r.status_code in sucesso_:
			print(f'\033[1;32mDiretório encontrado para o site "{site}" | Código de retorno - "{r.status_code}" | Diretório testado - "{site_req}"')
			hits.write(site_req + '\n')
		elif r.status_code in redirect:
			print(f'\033[1;33mRedirect para o site "{site}" | Código de retorno - "{r.status_code}" | Diretório testado - "{site_req}"')
		elif r.status_code in erro_site:
			print(f'\033[1;91mErro interno para o site "{site}" | Código de retorno - "{r.status_code}" | Diretório testado - "{site_req}"')
		else:
			print(f'\033[1;33mErro não computado para o site "{site}" | Código de retorno - "{r.status_code}" | Diretório testado - "{site_req}"')

	except Exception as e:
		print(e)