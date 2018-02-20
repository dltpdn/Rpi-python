class MyWith:
    def __init__(self):
        self.name = 'MyWith'
   
    def __enter__(self):
        print('entered.')
        return self
    
    def __exit__(self, ext, exv, trb):
        print('exit')


with MyWith() as my:
    print("my.name :" , my.name)
###############################################3

file_name = "file.txt"
try:
    with open(file_name) as file :
        lines = file.read()
        words = lines.splitlines()
        print(words)
except IOError:
    print('Can not open the file.')
