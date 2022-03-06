import os
import string
safechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '.-'+' '
arr = os.listdir()

for file in sorted(arr):
    splitfile = os.path.splitext(file)
    if(splitfile[1]) == ".scl":
        scl = open(file, encoding="ISO-8859-1")
        lines = scl.readlines()
        if( lines[1].rstrip() == '!'):
            newname = ''.join([c for c in lines[2].rstrip().replace('\\', ' over ') if c in safechars])+'.scl'
            if(newname == ''):
                continue
        elif(lines[2].rstrip() == '!'):
           newname = ''.join([c for c in lines[1].rstrip().replace('\\', ' over ') if c in safechars])+'.scl'
           if (newname == ''):
               continue
        else:
            continue
        print(splitfile[0] + ' ' + newname)
        os.rename(file, newname)
