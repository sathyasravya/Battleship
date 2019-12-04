import os
import sys
class ship:

    # Class Attribute
    # Initializer / Instance Attributes
    def __init__(self, m, matrix):
        self.m = m
        self.matrix = matrix
def main():
     filepath = 'inp.txt'
     with open(filepath) as fp:
         line = fp.readline()
         cnt = 1
         while line:
             #print("Line {}: {}".format(cnt, line.strip()))
             line = fp.readline()
             if(cnt ==1):
                 m = line
             if(cnt ==2):
                 s = line
             if(cnt ==3 ):

                 p1 = [][]
                 for i in range(len(m)):
                     for j in range(len(m)):
                         p1[i][j]='_'
                 li = []
                 li2 =[]
                 li = line.split(":")
                 for i in range(len(li)):
                     li2 = li[i].split(',')
                     p1[li2[0]][li2[1]]='B'

            if(cnt ==4 ):
                p2 = [][]
                for i in range(len(m)):
                    for j in range(len(m)):
                        p2[i][j]='_'
                li = line.split(":")
                for i in range(len(li)):
                    li2 = li[i].split(',')
                    p2[li2[0]][li2[1]]='B'
            if(cnt==5):
                tm = line
            if(cnt==6):
                #p2 = [][]
                li = line.split(":")
                for i in range(len(tm)):
                    li2 = li[i].split(',')
                    if(p2[li2[0]][li2[1]]=='B'):
                        p2[li2[0]][li2[1]]='X'
                    else:
                        p2[li2[0]][li2[1]]='O'
                li_m1 = li
            if(cnt==7):
                #p2 = [][]
                li = line.split(":")
                for i in range(len(tm)):
                    li2 = li[i].split(',')
                    if(p1[li2[0]][li2[1]]=='B'):
                        p1[li2[0]][li2[1]]='X'
                    else:
                        p1[li2[0]][li2[1]]='O'
                li_m2 = li
            feild1 = ship(m,p1,)
            feild2 = ship(m,p2)
        cnt += 1
    f.close()
    filepath = 'outp.txt'
    orig_stdout = sys.stdout
    f = open(filepath, 'w')
    sys.stdout = f
    print("Player1")
    for i in range(len(m)):
        for j in range(m):
            print(p1[i][j])
    print("Player2")
    for i in range(len(m)):
        for j in range(m):
            print(p2[i][j])
    sys.stdout = orig_stdout
    f.close()

if __name__== "__main__":
  main()
