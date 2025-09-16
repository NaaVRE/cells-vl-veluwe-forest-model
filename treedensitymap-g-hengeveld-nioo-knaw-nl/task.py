
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--DBH', action='store', type=str, required=True, dest='DBH')

arg_parser.add_argument('--Species', action='store', type=str, required=True, dest='Species')

arg_parser.add_argument('--TreeDensity', action='store', type=str, required=True, dest='TreeDensity')


args = arg_parser.parse_args()
print(args)

id = args.id

DBH = json.loads(args.DBH)
Species = json.loads(args.Species)
TreeDensity = json.loads(args.TreeDensity)





