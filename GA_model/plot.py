import argparse
from femaleMating.plot import Plot

parser = argparse.ArgumentParser(description='Plot CSV result')
parser.add_argument('-out', '--outputFilename', type=str)
parser.add_argument('-inf', '--fitfilenames', type=str, nargs='*')
parser.add_argument('-ing', '--gefilenames', type=str, nargs='*')
parser.add_argument('-t', '--female_type', type=int,)
parser.add_argument('-d', '--debug', type = bool, default=False, required=False)
args = parser.parse_args()

model = Plot(
    fitfilenames = args.fitfilenames,
    lastfilenames = args.gefilenames,
    output = args.outputFilename,
    type=args.female_type,
    debug = args.debug
)
