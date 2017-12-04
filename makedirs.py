import urllib.request
import os, sys, shutil
from bs4 import BeautifulSoup

if __name__ == '__main__':
	try:
		if len(sys.argv[1:]) == 1 and sys.argv[1] == "clean":
			for root, dirs, files in os.walk('./exercises/'):
				if len(files) == 1:
					for name in files:
						os.remove(os.path.join(root, name))
						os.rmdir(root)
		elif len(sys.argv[1:]) > 1:
			url = "https://projecteuler.net/problem="
			for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
				with urllib.request.urlopen(url+str(i)) as response:
					page = response.read()
					soup = BeautifulSoup(page, 'html.parser')
					problem_content = soup.findAll("div",{'class' : 'problem_content'})
					if not os.path.exists('./exercises/'+str(i)):
						os.makedirs('./exercises/'+str(i))
					htmlfile = open('./exercises/'+str(i)+'/'+str(i)+'.html', 'w')
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