from heapq import heappush,heappop
from task1 import bfs
# Controlled extension: A-C-G has 2 hops but cost 12; A-B-E-G costs 3.
WEIGHTED={'A':[('B',1),('C',6)],'B':[('D',4),('E',1)],'C':[('F',2),('G',6)],'D':[],'E':[('G',1)],'F':[],'G':[]}
def ucs(graph,start,goal):
    pq=[(0,start,[start])];best={start:0};trace=[]
    while pq:
        cost,node,path=heappop(pq)
        if cost!=best[node]:continue
        trace.append((node,cost))
        if node==goal:return cost,path,trace
        for nxt,w in graph.get(node,[]):
            if cost+w<best.get(nxt,float('inf')):
                best[nxt]=cost+w;heappush(pq,(cost+w,nxt,path+[nxt]))
    return None,None,trace
def path_cost(path):
    return sum(next(w for v,w in WEIGHTED[u] if v==v2) for u,v2 in zip(path,path[1:]))
if __name__=='__main__':
    cost,path,trace=ucs(WEIGHTED,'A','G')
    plain={u:[v for v,w in edges] for u,edges in WEIGHTED.items()}
    bp,btrace=bfs(plain,'A','G')
    print('UCS',path,cost,'verified',path_cost(path),'processed',trace)
    print('BFS',bp,'cost',path_cost(bp),'processed',[x[0] for x in btrace])
