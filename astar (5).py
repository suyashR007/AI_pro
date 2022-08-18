# -*- coding: utf-8 -*-
"""

@author: afaan

PROGRAM:- A*
"""

edges={}
weights={}
heuristic={}
f={}
g={}
open=[]
closed=[]

def fsort(openlist):
    for p in range(len(openlist)):
        for i in range(len(openlist)-1):
            current=openlist[i]
            next=openlist[i+1]
            if f[current[0]]>f[next[0]]:
                temp=openlist[i+1]
                openlist[i+1]=openlist[i]
                openlist[i]=temp
    return openlist

def findparent(node):
    for s in closed:
        if s[0]==node:
            return s[1]
    return None

def ReconstructPath(st):
    node=st[0]
    parent=st[1]
    path=[node]
    while parent is not None:
        # print(node)
        node = parent
        parent = findparent(node)
        path.append(node)
    path.reverse()
    return path

def removenode(li,node):
    for s in li:
        if s[0]==node:
            li.remove(s)
    return li

def checkifpresent(li,node):
    for s in li:
        if s[0]==node:
            return True
    return False

def propagateImprovement(node):
    neighbours=edges[node]
    for n in neighbours:
        if checkifpresent(open,n):
            edge=n+node
            new_g=g[node]+weights[edge]
            if new_g<g[n]:
                g[n]=new_g
                f[n]=g[n]+heuristic[n]
                open=removenode(open,n)
                open.append([n,node,g[n],heuristic[n]])
        if checkifpresent(closed,n):
            edge=n+node
            new_g=g[node]+weights[edge]
            if new_g<g[n]:
                g[n]=new_g
                f[n]=g[n]+heuristic[n]
                closed=removenode(closed,n)
                closed.append([n,node,g[n],heuristic[n]])
                propagateImprovement(n)


n=int(input('Enter number of nodes: '))
print('Enter Node Names:')
nodes=[]

for i in range(n):
    nodes.append(input(f'Node {i+1}: ').upper())
    heuristic[nodes[i]]=float(input('Enter Heuristic Value: '))
    print('')
    edges[nodes[i]]=[]

s=d='start'
count=0
print('Enter Edges: ')
print('Note: Enter edge as end,end to stop entering more edges\nEnter Node names in Capital Letters')
print('')
while s.lower()!='end' and d.lower()!='end':
    print('Edge ',count+1,':')
    s=input('Enter source node: ')
    d=input('Enter destination node: ')
    if s!='end' and d!='end':
        c=float(input('Enter cost of edge: '))
        edges[s].append(d)
        edges[d].append(s)
        weights[s+d]=weights[d+s]=c
    print('')
    count+=1

print(edges)
print(heuristic)
print(weights)
print('')


start=input('Enter Start Node: ')
goal=input('Enter Goal Node: ')
f[start]=heuristic[start]
g[start]=0
state=[start,None,0,heuristic[start]] #state=[current_node,parent,cost,heuristic]
open.append(state)

while len(open)!=0:
    current_state=open.pop(0)
    # print(current_state)
    closed.append(current_state)
    if current_state[0]==goal:
        print('Solution Found!')
        print('Path: ',ReconstructPath(current_state))
        print('Total Cost: ',current_state[2])
        break
    neighbours=edges[current_state[0]]
    for neighbour in neighbours:
        if checkifpresent(open,neighbour)==False and checkifpresent(closed,neighbour)==False:
            edge=neighbour+current_state[0]
            open.append([neighbour,current_state[0],current_state[2]+weights[edge],
                         heuristic[neighbour]])
            g[neighbour]=current_state[2]+weights[edge]
            f[neighbour]=g[neighbour]+heuristic[neighbour]
        elif checkifpresent(open,neighbour):
            edge=neighbour+current_state[0]
            new_g=current_state[2]+weights[edge]
            if new_g<g[neighbour]:
                g[neighbour]=new_g
                f[neighbour]=g[neighbour]+heuristic[neighbour]
                open=removenode(open,neighbour)
                open.append([neighbour,current_state[0],g[neighbour],heuristic[neighbour]])
        elif checkifpresent(closed,neighbour):
            edge=neighbour+current_state[0]
            new_g=current_state[2]+weights[edge]
            if new_g<g[neighbour]:
                g[neighbour]=new_g
                f[neighbour]=g[neighbour]+heuristic[neighbour]
                closed=removenode(closed,neighbour)
                closed.append([neighbour,current_state[0],g[neighbour],heuristic[neighbour]])      
                propagateImprovement(neighbour)   

    open=fsort(open)   

    





