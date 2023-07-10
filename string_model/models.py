import genome
from model import FemaleMatingModel
import dataProcess

models = []

def start(args):
    for g in genome.generate_genome(args.matingLength):
        model = FemaleMatingModel(
            args=args,
            genome = g
        )

        model.det_fitness()
        models.append(model)
    dataProcess.cal_data(models, args.filename)
    