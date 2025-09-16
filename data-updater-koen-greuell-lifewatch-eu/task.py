
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--delta_tree_mass', action='store', type=float, required=True, dest='delta_tree_mass')

arg_parser.add_argument('--intial_tree_mass', action='store', type=float, required=True, dest='intial_tree_mass')


args = arg_parser.parse_args()
print(args)

id = args.id

delta_tree_mass = args.delta_tree_mass
intial_tree_mass = args.intial_tree_mass



tree_mass = intial_tree_mass

tree_mass = tree_mass + delta_tree_mass

file_tree_mass = open("/tmp/tree_mass_" + id + ".json", "w")
file_tree_mass.write(json.dumps(tree_mass))
file_tree_mass.close()
