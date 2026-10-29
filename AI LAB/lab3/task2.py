from task1 import GRAPH
# Path-local cycle detection preserves alternate routes.
def dls(graph,start,goal,limit):
    def visit(node,path,depth):
        if node==goal:return 'FOUND',path
        if depth==limit:
            return ('CUTOFF',None) if any(n not in path for n in graph.get(node,[])) else ('FAILURE',None)
        cutoff=False
        for nxt in graph.get(node,[]):
            if nxt in path:continue
            status,answer=visit(nxt,path+[nxt],depth+1)
            if status=='FOUND':return status,answer
            if status=='CUTOFF':cutoff=True
        return ('CUTOFF' if cutoff else 'FAILURE'),None
    return visit(start,[start],0)
def iddfs(graph,start,goal,max_depth):
    tried=[]
    for limit in range(max_depth+1):
        status,path=dls(graph,start,goal,limit);tried.append((limit,status))
        if status=='FOUND':return status,path,tried
        if status=='FAILURE':return status,None,tried
    return 'CUTOFF',None,tried
if __name__=='__main__':
    for limit in [1,2,3,4]:
        print('DLS',limit,dls(GRAPH,'A','G',limit))
        print('IDDFS max',limit,iddfs(GRAPH,'A','G',limit))
