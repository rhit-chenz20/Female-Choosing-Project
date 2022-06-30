import agent

female = agent.FemaleGenome([0,1,0,1,1,0,0,0,1], memoryLength=3)
for x in range(len(female.genome)):
    female.setCurrentMale(x)
    female.step()