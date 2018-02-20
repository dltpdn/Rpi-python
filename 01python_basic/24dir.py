import os
import os.path
import glob

cwd = os.getcwd()
print(cwd)
os.chdir('./animal')
print(os.getcwd())
os.chdir('..')
#os.mkdir('temp')
for x in os.walk('.'):
    print(x)

print(os.path.abspath('.'))
print(os.path.basename(cwd))
print(os.path.dirname(cwd))
print(os.path.split(cwd))

print(os.path.exists('./animal'))
print(os.path.join('a', 'b', 'abc.txt'))

print(glob.glob('./*.txt'))