from classroom_reflex import ClassroomAgent
class StatefulClassroomAgent(ClassroomAgent):
    def __init__(self): self.previous_mode=None
    def step(self,temp,occupied):
        previous=self.previous_mode
        target=self.act(temp,occupied)
        send=target!=previous
        self.previous_mode=target
        return previous,target,send
if __name__=='__main__':
    agent=StatefulClassroomAgent()
    for temp,occupied in [(29,True),(29,True),(20,True),(26,True),(19,True),(29,False),(29,False)]:
        prev,target,send=agent.step(temp,occupied)
        print(f'previous={prev} percept=({temp},{occupied}) target={target} command={send}')
