import argparse
from femaleMating.plot import Plot

parser = argparse.ArgumentParser(description='Plot CSV result')
parser.add_argument('-out', '--outputFilename', type=str)
parser.add_argument('-in', '--filenames', type=str, nargs='*')
args = parser.parse_args()

model = Plot(
    filenames = args.filenames,
    output = args.outputFilename
)
