from task3 import StatefulClassroomAgent
agent=StatefulClassroomAgent()
expected=[('COOL',True),('COOL',False),('IDLE',True),('IDLE',False),('WARM',True),('ECO',True)]
inputs=[(29,True),(29,True),(20,True),(26,True),(19,True),(29,False)]
for percept,want in zip(inputs,expected):
    prev,target,send=agent.step(*percept)
    assert (target,send)==want
    print(percept,prev,target,send,'PASS')
