from heapq import heappush,heappop
G={'S':[('A',1),('B',4)],'A':[('C',2)],'B':[('G',5)],'C':[('G',3)],'G':[]}
H={'S':5,'A':4,'B':4,'C':2,'G':0}
def astar(graph,h,start='S',goal='G'):
    pq=[(h[start],0,start,[start])];best={start:0};processed=[];expansions=[]
    while pq:
        f,g,node,path=heappop(pq)
        if g!=best[node]:continue
        processed.append((node,g,h[node],f))
        if node==goal:return g,path,processed,expansions
        expansions.append(node)
        for nxt,w in graph.get(node,[]):
            ng=g+w
            if ng<best.get(nxt,float('inf')):
                best[nxt]=ng;heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))
    return None,None,processed,expansions
if __name__=='__main__':
    for label,h in [('A*',H),('UCS',{k:0 for k in H}),('Overestimate',{**H,'C':10})]:
        cost,path,processed,expanded=astar(G,h)
        print(label,'path',path,'cost',cost,'processed',processed,'expanded',expanded,'count',len(expanded))
    print('Heuristic consistency checks:')
    for u,edges in G.items():
        for v,w in edges:print(u,v,H[u],'<=' ,w+H[v],H[u]<=w+H[v])
