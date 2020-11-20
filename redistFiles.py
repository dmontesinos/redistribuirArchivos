import shutil
import os
import time

def redist(c, path):
    files = []

    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            files.append(f)


    for f in files:
        obj = os.path.splitext(f)
        if (obj[1] == '.gif'):
            shutil.move('Origin/' + f, 'Dest1/file-'+str(c)+".gif")
            c += 1

        elif (obj[1] == '.mp4'):
            shutil.move('Origin/' + f, 'Dest2/file-'+str(c)+".mp4")
            c += 1

        else:
            print("El fichero " + f + " no puede ser movido.")


if __name__ == '__main__':
    con = 0
    path = r"Origin"
    while(True):
        time.sleep(1)
        redist(con, path)
