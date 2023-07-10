
import argparse
import models 
import genome

parser = argparse.ArgumentParser(description='Start female mating simulation')
parser.add_argument('-fs', '--femaleSize', type=int, default=100, required=False)
parser.add_argument('-ml', '--matingLength', type=int)
parser.add_argument('-ms', '--maleSigma', type=float)
parser.add_argument('-fit', '--fitnessFunction', type=int, default=0, required=False)
parser.add_argument('-fn', '--filename', type=str)
parser.add_argument('-seed', '--seed', type = int, default=-1, required=False)
parser.add_argument('-fitbase', '--fitbase', type = float, default=0, required=False)
args = parser.parse_args()


models.start(args)


