# from femaleMating.server import server
# server.launch()

import argparse
from femaleMating.model import FemaleMatingModel

parser = argparse.ArgumentParser(description='Start female mating simulation')
parser.add_argument('fSize', type=int)
parser.add_argument('mLength', type=int)
parser.add_argument('mMu', type=float)
parser.add_argument('mSigma', type=float)
parser.add_argument('muSigma', type=float)
parser.add_argument('maxGen', type=int)
parser.add_argument('range', type=float)
parser.add_argument('selection', type=int)
parser.add_argument('fitness', type=int)
parser.add_argument('filename', type=str)
args = parser.parse_args()

model = FemaleMatingModel(
    femaleSize = args.fSize,
    matingLength = args.mLength,
    maleMu = args.mMu,
    maleSigma = args.mSigma,
    mutationSigma = args.muSigma,
    generations = args.maxGen,
    startingRange = args.range,
    selection = args.selection,
    fitness=args.fitness,
    filename = args.filename
)

# for running without mesa
for x in range(model.maxGen):
    model.step()
