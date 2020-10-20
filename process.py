import os
os.system('pidof simplescreenrecorder > process.txt')
with open('process.txt','r') as file:
    new  =  file.read()
    os.system(f'kill  {new}')

