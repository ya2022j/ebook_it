


import os

path = os.getcwd()
all = os.listdir(path)
for file in all:
    if file.endswith(".html"):
        name = os.path.splitext(file)[0]
        os.system("cd {0} && pandoc -f html -t markdown -o {1}.md {2}.html".format(path,os.path.splitext(name)[0],os.path.splitext(name)[0]))


