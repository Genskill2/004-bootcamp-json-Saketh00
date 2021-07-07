# Add the functions in this file

import sys
import json

def load_journal(f_name):
    f=open(f_name,"r")
    string=f.read()
    f.close()
    data=json.loads(string)
    #if 'carrot' in data[0]['events']:
    #l=data[0]['events']
    #for i in range(0,len(l)):
    #    print(l[i])
    return data

def compute_phi(f_name, event):
    data=load_journal(f_name)
    z=0
    x=0
    c=0
    v=0
    a=0
    s=0
    d=0
    f=0
    for i in range(0,91):
        if event in data[i]['events'] and data[i]['squirrel']:
            z=z+1
        if event not in data[i]['events'] and not data[i]['squirrel']:
            x=x+1
        if event in data[i]['events'] and not data[i]['squirrel']:
            c=c+1
        if event not in data[i]['events'] and data[i]['squirrel']:
            v=v+1
        if event in data[i]['events']:
            a=a+1
        if event not in data[i]['events']:
            s=s+1
        if data[i]['squirrel']:
            d=d+1
        if not data[i]['squirrel']:
            f=f+1
    
    req=(z*x-c*v)/(a*s*d*f)**(0.5)
    return req

def compute_correlations(f_name):
    data=load_journal(f_name)
    d={}
    for i in range(0,91):
        l=data[i]['events']
        for j in range(0,len(l)):
            event=l[j]
            if event not in d.keys():
                value=compute_phi(f_name,event)
                d[event]=value
        #print(d)
        #print('carrot' in d.keys())
    #print(d)
    return d

def diagnose(f_name):
    dic=compute_correlations(f_name)
    p=-1
    n=1
    maxEvent=""
    minEvent=""
    for i in dic.keys():
        #print(dic[i])
        if dic[i]>p :
            maxEvent=i
            p=dic[i]
        if dic[i]<n :
            minEvent=i
            n=dic[i]
    #if(p> abs(n)):
    #    print(p)
    #else:
    #    print(n)
    return maxEvent,minEvent


#if __name__=="__main__":
#    p,n=diagnose(sys.argv[1])
#    print(p,n)

