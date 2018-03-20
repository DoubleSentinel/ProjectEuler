from time import time
import sys
import os


def run(ex, verbose=False):
    print('\nCompiling {}'.format(ex))
    output = os.system('stack build')
    
    if verbose:
        print(output)

    print('\nStarting {}'.format(ex))
    start = time()
    os.system('stack exec rofl.exe')
    print('Time for {}: {}\n'.format(ex, time() - start))


def main():
    try:
        ex = sys.argv[1]
    except:
        print('Please give an exercise number')
        sys.exit(-1)
    
    folder = '../exercises/E{}'.format(ex)
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    exercisefile = '{}/Q.hs'.format(folder, ex)
    mainfile = 'app/Main.hs'
    maintemplatefile = 'templates/Main.hs'
    exercisetemplatefile = 'templates/E.hs'
    
    with open(maintemplatefile, 'r') as file:
        maintemplate = ''.join(file.readlines()).format(ex)
        
    with open(mainfile, 'w') as file:
        file.writelines(maintemplate)
    
    if os.path.isfile(exercisefile):
        run(ex)
        sys.exit(0)
        
    print('Creating exercice {}'. format(ex))
    
    with open(exercisetemplatefile, 'r') as file:
        exercisetemplate = ''.join(file.readlines()).format(ex)
    
    with open(exercisefile, 'w') as file:
        file.writelines(exercisetemplate)
    
    os.system('start notepad++ {}'.format(exercisefile))
    # os.system('start chrome {}'.format('https://projecteuler.net/problem={}'.format(ex)))
    
    sys.exit(0)


if __name__ == '__main__':
    main()
