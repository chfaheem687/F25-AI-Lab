from task2 import minimax,alphabeta
# Swap complete subtrees, preserving the game-tree structure and root value.
def swap_sibling_subtrees(values,level):
    # level 1 swaps the root's two halves; level 2 swaps quarter-pairs.
    n=len(values); block=n//(2**level)
    out=[]
    for i in range(0,n,2*block):out+=values[i+block:i+2*block]+values[i:i+block]
    return out
if __name__=='__main__':
    base=[3,5,2,9,3,5,2,9]
    for label,values in [('original',base),('root swapped',swap_sibling_subtrees(base,1)),('quarter swapped',swap_sibling_subtrees(base,2)),('leaf swapped',swap_sibling_subtrees(base,3))]:
        mm=minimax(values);ab=alphabeta(values)
        assert mm[0]==ab[0]==minimax(base)[0]
        print(label,values,'minimax',mm,'alpha-beta',ab)
