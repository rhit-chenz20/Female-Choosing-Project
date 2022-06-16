# from femaleMating.server import server
# server.launch()

import argparse
from femaleMating.model import FemaleMatingModel
from femaleMating.plot import Plot

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('fSize', type=int)
parser.add_argument('mLength', type=int)
parser.add_argument('mMu', type=float)
parser.add_argument('mSigma', type=float)
parser.add_argument('muSigma', type=float)
parser.add_argument('maxGen', type=int)
parser.add_argument('range', type=float)
parser.add_argument('selection', type=str)
parser.add_argument('filename', type=str)
parser.add_argument('plot50', type=bool)
parser.add_argument('plotT', type=bool)
args = parser.parse_args()

# model = FemaleMatingModel(
#     femaleSize = args.fSize,
#     matingLength = args.mLength,
#     maleMu = args.mMu,
#     maleSigma = args.mSigma,
#     mutationSigma = args.muSigma,
#     generations = args.maxGen,
#     startingRange = args.range,
#     # selection = "top50",
#     # selection = "tournament",
#     selection = args.selection,
#     filename = args.filename
# )

# plot = Plot(args.plot50, args.plotT)
plot = Plot(True, False)
