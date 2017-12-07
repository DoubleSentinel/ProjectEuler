import urllib.request
import os
import sys
import shutil
from bs4 import BeautifulSoup


def main():
	try:
		if len(sys.argv[1:]) == 1 and sys.argv[1] == "clean":
			for root, dirs, files in os.walk('./exercises/'):
				if len(files) == 1:
					for name in files:
						os.remove(os.path.join(root, name))
						os.rmdir(root)
                        
		elif len(sys.argv[1:]) == 2:
			url = "https://projecteuler.net/problem={}"
            
            low = int(sys.argv[1])
            high = int(sys.argv[2])
            
			for i in range(low, high + 1):
				with urllib.request.urlopen(url.format(i)) as response:
					page = response.read()
					soup = BeautifulSoup(page, 'html.parser')
					problem_content = soup.findAll("div", {'class': 'problem_content'})
					
                    folder = './exercises/{}'.format(i)
                    if not os.path.exists(folder):
						os.makedirs(folder)
					
                    htmlfile = open('{}/{}.html'.format(folder, i), 'w')
					htmlfile.write(str(problem_content).split('[')[1].split(']')[0])
					htmlfile.close()
		
		else:
			print("Makedirs will create all the subdirectories for Project Euler problems N to M")
			print("To perform this use the arguments python ./makedirs N M")
			print("To clean up unchanged directories use the argument python ./makedirs clean")
	except urllib.error.HTTPError:
		print('rekt by http')
	except UnicodeEncodeError:
		print('rekt by unicode')
	except:
		print('rekt by existence')
        
        
if __name__ == '__main__':
    main()
