# from femaleMating.server import server
# server.launch()

from femaleMating.model import FemaleMatingModel
model = FemaleMatingModel(10,4,2,3,10,1,10,2)

for i in range(10):
    model.step()