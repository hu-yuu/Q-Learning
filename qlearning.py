import numpy as np
from env import Environment
import random 
from operator import itemgetter
from tabulate import tabulate
import matplotlib.pyplot as plt
import time
from envgr import Wall, Room, Room1, drw
import math

class Qlearning:
    def __init__(self, gamma, startX, startY, env:Environment):
        self.gamma = gamma
        self.env = env

        self.boundX, self.boundY = env.get_shape()
        self.q_table = np.zeros((self.boundX**2, self.boundY**2))
        self.set_loc(startX, startY)

    def set_loc(self, x, y):
        self.cur_X = x
        self.cur_Y = y

    
    def choose_way(self):
        cur_around = self.env.get_around(self.cur_X, self.cur_Y)

        cur_state = self.boundX * self.cur_X + self.cur_Y

        q_scores = []
        for i in cur_around:
            q_scores.append({
                'cur_state':cur_state,
                'next_state':i['state'],
                'q_score':self.q_table[cur_state, i['state']],
                'x':i['x'],
                'y':i['y']
            })

        q_scores = sorted(q_scores, key=itemgetter('q_score'), reverse=True)

        ctdup = 0

        nextLoc = 0
    
        if len(q_scores) >0:
            maxval = q_scores[0]['q_score']
        else:
            return -997, 'empty'

        if len(q_scores) >1:
            for i in q_scores[1:]:
                if i['q_score'] == maxval:
                    ctdup +=1
            rnd = random.randint(0, ctdup)
            nextLoc = q_scores[rnd]
        else:
            nextLoc == maxval

        print(nextLoc)
            
        try:
            maxnum_around = self.env.get_around(nextLoc['x'], nextLoc['y'])
        except:
            return -997, nextLoc
        mxnex = []
        for i in maxnum_around:
            dct = {'state': i['state'], 'score':self.q_table[nextLoc['next_state'] ,i['state']]}
            mxnex.append(dct)
        mxnex1 = sorted(mxnex, key=itemgetter('score'), reverse=True)[0]
        
                
        
        score = env.env[nextLoc['x'], nextLoc['y']] + (self.gamma * mxnex1['score'])

        

        self.update_Q(cur_state, nextLoc['next_state'], score)
        
        if nextLoc['x'] == env.endX and nextLoc['y'] == env.endY:
            return -999, nextLoc, score
        elif env.env[nextLoc['x'], nextLoc['y']] == env.bpoint:
            return -998, nextLoc, score
  
        
        self.set_loc(nextLoc['x'], nextLoc['y'])

        return 1, nextLoc, score

    def update_Q(self, x, y, score):
        self.q_table[x, y] = score

    def get_shortes_path(self, x, y):
        
        nl = env.x*x + y
        fnl = env.x*env.endX + env.endY
        locs = [nl]
        for i in range(len(self.q_table)):
            nl = np.argmax(self.q_table[nl])
            locs.append(nl)

            if np.max(self.q_table[nl]) == 100:
                locs.append(fnl)
                return locs

    #Fully Random pick if point != -100
    def choose_way2(self):
        cur_around = self.env.get_around(self.cur_X, self.cur_Y)

        cur_state = self.boundX * self.cur_X + self.cur_Y

        q_scores = []
        for i in cur_around:
            q_scores.append({
                'cur_state':cur_state,
                'next_state':i['state'],
                'q_score':self.q_table[cur_state, i['state']],
                'x':i['x'],
                'y':i['y']
            })

        q_scores = sorted(q_scores, key=itemgetter('q_score'), reverse=True)

        ctdup = 0

        nextLoc = 0
    
        if len(q_scores) >=1:
            q_scores = [ind for ind in q_scores if ind['q_score'] != -100]
            rnd = random.randint(0, len(q_scores)-1)
            nextLoc = q_scores[rnd]
        else:
            return -997, 'empty'

        print(nextLoc)
            
        try:
            maxnum_around = self.env.get_around(nextLoc['x'], nextLoc['y'])
        except:
            return -997, nextLoc
        mxnex = []
        for i in maxnum_around:
            dct = {'state': i['state'], 'score':self.q_table[nextLoc['next_state'] ,i['state']]}
            mxnex.append(dct)
        mxnex1 = sorted(mxnex, key=itemgetter('score'), reverse=True)[0]
        
                
        
        score = env.env[nextLoc['x'], nextLoc['y']] + (self.gamma * mxnex1['score'])

        self.update_Q(cur_state, nextLoc['next_state'], score)
        
        if nextLoc['x'] == env.endX and nextLoc['y'] == env.endY:
            return -999, nextLoc, score
        elif env.env[nextLoc['x'], nextLoc['y']] == env.bpoint:
            return -998, nextLoc, score
  
        
        self.set_loc(nextLoc['x'], nextLoc['y'])

        return 1, nextLoc, score

        
def plot_results( steps, cost):

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    
    ax1.plot(np.arange(len(steps)), steps, 'b')
    ax1.set_xlabel('Episode')
    ax1.set_ylabel('Steps')
    ax1.set_title('Episode via steps')

    
    ax2.plot(np.arange(len(cost)), cost, 'r')
    ax2.set_xlabel('Episode')
    ax2.set_ylabel('Cost')
    ax2.set_title('Episode via cost')

    plt.tight_layout()  

    
    plt.figure()
    plt.plot(np.arange(len(steps)), steps, 'b')
    plt.title('Episode via steps')
    plt.xlabel('Episode')
    plt.ylabel('Steps')

    
    plt.figure()
    plt.plot(np.arange(len(cost)), cost, 'r')
    plt.title('Episode via cost')
    plt.xlabel('Episode')
    plt.ylabel('Cost')

    plt.show()


if __name__ == "__main__":
    
    
    env = Environment(20, 20, 20, -100, 0)

    drw(env.env, [])

    st2 = int(input("Bitiş X: "))
    ed2 = int(input("Bitiş Y: "))
    env.set_end(st2, ed2)
    env.to_txt()


    
    st = int(input("Başlangıç X: "))
    ed = int(input("Başlangıç Y: "))
    drw(env.env, [])
    


    qler = Qlearning(0.8, st, ed, env)


    start = time.time()
    episodeCT = 0


    costList = []
    stepList = []

    while True:
        print('####### EPISODE {} #######'.format(episodeCT))
        qler.set_loc(st,ed)
        countStep = 0
        costCt = 0
        while True:
            flag, nn, sc = qler.choose_way()
            costCt += sc
            countStep +=1

            if flag == -999: 
                print('find max')
                break
            elif flag == -998:
                print('hit the wall')
                break
            elif flag == -997:
                print('no way to go:', nn)
                break
        costList.append(costCt)
        stepList.append(countStep)

        print(countStep)
        episodeCT +=1
        if qler.get_shortes_path(st, ed) != None: break


    print(time.time()-start)
    print(qler.get_shortes_path(st, ed))
    kisaYol = []
    for ind in qler.get_shortes_path(st, ed):
        sX = math.floor(ind/env.x)
        sY = ind%env.x
        kisaYol.append((sX, sY))

    drw(env.env, kisaYol)
    plot_results(stepList, costList)
    





