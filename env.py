import numpy as np
import random 
from tabulate import tabulate
from operator import itemgetter

class Environment:
    def __init__(self, x, y, barrier_rate, bpoint, wpoint):
        self.env = np.zeros((x, y))
        self.x = x
        self.y = y
        self.bpoint = bpoint
        for x1 in range(x):
            for y1 in range(y):
                rand = random.randint(0, 100)
                if rand <= barrier_rate:
                    self.env[x1, y1] = bpoint
                else:
                    self.env[x1, y1] = wpoint


        countB = 0
        for i in range(20):
            for y in range(20):
                if self.env[i, y] == -100:
                    countB += 1
        print(countB, "BURASI BARİYER SAYISI")
                

    def set_end(self, x, y):
        self.endX = x
        self.endY = y
        self.env[x, y] = 100

    def get_shape(self):
        return self.x, self.y

    def to_txt(self):
        with open("env.txt",'w', encoding = 'utf-8') as f:
            f.write('')

        for i in range(self.env.shape[0]):
            for y in range(self.env.shape[1]):
                with open("env.txt",'a', encoding = 'utf-8') as f:
                    if self.env[i, y]==0:
                        f.write('({})({}){}\n'.format(i, y, 'Y'))
                    elif self.env[i, y]==-100:
                        f.write('({})({}){}\n'.format(i, y, 'E'))
                    else:
                        f.write('({})({}){}\n'.format(i, y, 'B'))

    def get_around(self, x, y):
        around_loc = []
        for x1 in range(x-1, x+2):
            if x1<= self.env.shape[0]-1 and x1 >=0:
                for y1 in range(y-1, y+2):
                    if y1<=self.env.shape[1]-1 and y1 >=0 : #and self.env[x1, y1] != self.bpoint
                        if x1!=x or y1!=y:
                            around_loc.append({'x':x1,
                                            'y':y1,
                                            'state': (self.x) * x1 + y1,
                                            'score':self.env[x1, y1]})
        random.shuffle(around_loc)
        return around_loc
                        


if __name__ == '__main__':
    env = Environment(5, 5, 30, -10, -1)
    env.set_end(4, 4)
    m = tabulate(env.env, tablefmt="fancy_grid")
    print(m)
    for i in env.get_around(0, 0):
        print(i)