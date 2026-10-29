from collections import deque
GRAPH={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':['G'],'F':[],'G':[]}
def bfs(graph,start,goal):
    q=deque([(start,[start])]); seen={start}; trace=[]
    while q:
        node,path=q.popleft(); trace.append((node,list(q),path))
        if node==goal: return path,trace
        for nxt in graph.get(node,[]):
            if nxt not in seen: seen.add(nxt);q.append((nxt,path+[nxt]))
    return None,trace
def dfs(graph,start,goal):
    stack=[(start,[start])];seen=set();trace=[]
    while stack:
        node,path=stack.pop()
        if node in seen:continue
        seen.add(node);trace.append((node,list(reversed(stack)),path))
        if node==goal:return path,trace
        for nxt in reversed(graph.get(node,[])):
            if nxt not in seen:stack.append((nxt,path+[nxt]))
    return None,trace
if __name__=='__main__':
    for name,fn in [('BFS',bfs),('DFS',dfs)]:
        path,trace=fn(GRAPH,'A','G');print(name,'path',path,'visit',[r[0] for r in trace])
        for node,frontier,p in trace:print(' processed',node,'frontier',frontier,'path',p)
