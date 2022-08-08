import argparse
from femaleMating.plot import Plot

parser = argparse.ArgumentParser(description='Plot CSV result')
parser.add_argument('-out', '--outputFilename', type=str)
parser.add_argument('-inf', '--fitfilenames', type=str, nargs='*')
parser.add_argument('-ing', '--gefilenames', type=str, nargs='*', required=False)
parser.add_argument('-t', '--female_type', type=int,)
args = parser.parse_args()

model = Plot(
    fitfilenames = args.fitfilenames,
    lastfilenames = args.gefilenames,
    output = args.outputFilename,
    type=args.female_type
)
