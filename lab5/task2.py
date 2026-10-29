# Complete binary game tree; root is MAX and turns alternate.
def minimax(scores):
    count=0;depth=(len(scores)-1).bit_length()
    assert len(scores)==2**depth
    def visit(d,i,max_turn):
        nonlocal count
        if d==depth:count+=1;return scores[i]
        a=visit(d+1,2*i,not max_turn)
        b=visit(d+1,2*i+1,not max_turn)
        return max(a,b) if max_turn else min(a,b)
    value=visit(0,0,True)
    return value,count
def alphabeta(scores):
    count=0;depth=(len(scores)-1).bit_length()
    assert len(scores)==2**depth
    def visit(d,i,max_turn,alpha,beta):
        nonlocal count
        if d==depth:count+=1;return scores[i]
        val=float('-inf') if max_turn else float('inf')
        for child in (2*i,2*i+1):
            v=visit(d+1,child,not max_turn,alpha,beta)
            if max_turn:val=max(val,v);alpha=max(alpha,val)
            else:val=min(val,v);beta=min(beta,val)
            if alpha>=beta:break
        return val
    return visit(0,0,True,float('-inf'),float('inf')),count
if __name__=='__main__':
    scores=[3,5,2,9,3,5,2,9]
    print('scores',scores,'minimax',minimax(scores),'alpha-beta',alphabeta(scores))
    assert minimax(scores)[0]==alphabeta(scores)[0]
