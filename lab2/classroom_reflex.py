class ClassroomAgent:
    def act(self,temp,occupied):
        if not occupied: return 'ECO'
        if temp>26: return 'COOL'
        if temp<20: return 'WARM'
        return 'IDLE'
if __name__=='__main__':
    a=ClassroomAgent()
    for p in [(29,True),(29,True),(20,True),(26,True),(19,True),(29,False)]: print(p,a.act(*p))
