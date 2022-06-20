import argparse
from femaleMating.plot import Plot

parser = argparse.ArgumentParser(description='Plot CSV result')
parser.add_argument('outputFilename', type=str)
args = parser.parse_args()

model = Plot(
    filename = args.outputFilename,
)
