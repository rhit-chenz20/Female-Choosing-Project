# from femaleMating.server import server
# server.launch()

from femaleMating.model import FemaleMatingModel
model = FemaleMatingModel(
    femaleSize = 10,
    matingLength = 5,
    maleMu = 5,
    maleSigma = 1,
    mutationSigma = 1,
    generations = 1000,
    startingRange = 4)

for i in range(1000):
    model.step()