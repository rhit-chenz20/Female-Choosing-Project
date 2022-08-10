# from femaleMating.server import server
# server.launch()

import argparse
from femaleMating.model import FemaleMatingModel

parser = argparse.ArgumentParser(description='Start female mating simulation')
parser.add_argument('-fs', '--femaleSize', type=int, default=100, required=False)
parser.add_argument('-ml', '--matingLength', type=int)
parser.add_argument('-ms', '--maleSigma', type=float)
parser.add_argument('-mul', '--mutationLamda', type=float, default=0.05, required=False)
parser.add_argument('-max', '--maxGen', type=int, default=200, required=False)
parser.add_argument('-fsigma', '--femaleSigma', type=float)
parser.add_argument('-fmu', '--femaleMu', type=float)
parser.add_argument('-sel', '--selection', type=int, default=0, required=False)
parser.add_argument('-fit', '--fitnessFunction', type=int, default=0, required=False)
parser.add_argument('-fn', '--filename', type=str)
parser.add_argument('-ft', '--femaleType', type = int, default=0, required=False)
parser.add_argument('-memol', '--memoryLength', type = int, default=0, required=False)
parser.add_argument('-c', '--flatCost', type = float, default=0, required=False)
parser.add_argument('-base', '--fitbase', type = float, default=0.5, required=False)
parser.add_argument('-per', '--topPercent', type = float, default=0.5, required=False)
parser.add_argument('-d', '--debug', type = bool, default=False, required=False)
args = parser.parse_args()

model = FemaleMatingModel(
    args=args
    # femaleSize = args.femaleSize,
    # matingLength = args.matingLength,
    # maleSigma = args.maleSigma,
    # mutationSigma = args.mutationLamda,
    # generations = args.maxGen,
    # femaleSigma =  args.femaleSigma,
    # femaleMu = args.femaleMu,
    # selection = args.selection,
    # fitness=args.fitnessFunction,
    # filename = args.filename,
    # femaleType = args.femaleType,
    # memoryLength= args.memoryLength,
    # flatcost=args.flatCost,
    # fitbase = args.fitbase,
    # topPercent= args.topPercent,
)

model.start()

# for running without mesa
# for x in range(model.maxGen):
#     model.step()
