import os
import sys
class battleground:
    # Class Attribute, Initializer / Instance Attributes
    def __init__(self, m, matrix,destroy,name):
        self.m = m
        self.name = name
        self.matrix = matrix
        sel.destroy = destroy
    def kill_targets(self):
        for i in range(len(tm)):
            li2 = destroy[i].split(',')
            if(matrix[li2[0]][li2[1]]=='B'):
                matrix[li2[0]][li2[1]]='X'
            else:
                matrix[li2[0]][li2[1]]='O'
    def print_matrix(self):
        print(self.name)
        for i in range(len(m)):
            for j in range(m):
                print(matrix[i][j])
def main():
     filepath = 'inp.txt'
     with open(filepath) as fp:
         line = fp.readline()
         cnt = 1
         while line:
             line = fp.readline()
             if(cnt ==1):
                 m = int(line)
             if(cnt ==2):
                 s = int(line)
             if(cnt ==3 ):
                 p1 = []
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
                 p2 = []
                 for i in range(len(m)):
                     for j in range(len(m)):
                         p2[i][j]='_'
                 li = line.split(":")
                 for i in range(len(li)):
                     li2 = li[i].split(',')
                     p2[li2[0]][li2[1]]='B'
             if(cnt==5):
                 tm = int(line)
             if(cnt==6):
                 li = line.split(":")
                 li_m1 = li
             if(cnt==7):
                 li = line.split(":")
                 li_m2 = li

         cnt += 1
    feild1 = battleground(m,p1,li_m2,'Player1')
    feild2 = battleground(m,p2,li_m1,'Player2')
    filepath = 'outp.txt'
    orig_stdout = sys.stdout
    f = open(filepath, 'w')
    sys.stdout = f
    feild1.print_matrix()
    feild2.print_matrix()
    sys.stdout = orig_stdout
    f.close()
    f.close()
if __name__== "__main__":
  main()
