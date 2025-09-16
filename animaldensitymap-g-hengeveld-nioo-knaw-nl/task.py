
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--Abundance', action='store', type=str, required=True, dest='Abundance')

arg_parser.add_argument('--Animal', action='store', type=str, required=True, dest='Animal')


args = arg_parser.parse_args()
print(args)

id = args.id

Abundance = json.loads(args.Abundance)
Animal = json.loads(args.Animal)





