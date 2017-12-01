import urllib.request
import os, sys, shutil
from bs4 import BeautifulSoup

if __name__ == '__main__':
	try:
		if sys.argv[1] == "clean":
			for root, dirs, files in os.walk('./exercises/'):
				if len(files) <= 1:
					for name in files:
						print('file: ' + os.path.join(root, name))
						#os.remove(os.path.join(root, name))
					for name in dirs:
						print('dir: ' + os.path.join(root, name))
						#os.rmdir(os.path.join(root, name))
		elif sys.argv[1] and sys.argv[2]:
			url = "https://projecteuler.net/problem="
			for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
				with urllib.request.urlopen(url+str(i)) as response:
					page = response.read()
					soup = BeautifulSoup(page, 'html.parser')
					problem_content = soup.findAll("div",{'class' : 'problem_content'})
					if not os.path.exists('./'+str(i)):
						os.makedirs('./'+str(i))
					htmlfile = open('./'+str(i)+'/'+str(i)+'.html', 'w')
					htmlfile.write(str(problem_content).split('[')[1].split(']')[0])
					htmlfile.close()
		
		else:
			print("Makedirs will create all the subdirectories for Project Euler problems N to M")
			print("To perform this use the arguments python ./makedirs N M")
			print("To clean up unchanged directories use the argument python ./makedirs clean")
	except urllib.error.HTTPError as e:
		if e.code == 404:
			exit()
	except UnicodeEncodeError:
		pass
	except IndexError:
		pass