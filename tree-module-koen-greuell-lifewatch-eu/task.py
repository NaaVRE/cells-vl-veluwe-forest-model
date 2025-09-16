
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--nitrogen_uptake_factor', action='store', type=float, required=True, dest='nitrogen_uptake_factor')

arg_parser.add_argument('--soil_nitrogen_compounds_concentration', action='store', type=float, required=True, dest='soil_nitrogen_compounds_concentration')

arg_parser.add_argument('--tree_mass', action='store', type=float, required=True, dest='tree_mass')


args = arg_parser.parse_args()
print(args)

id = args.id

nitrogen_uptake_factor = args.nitrogen_uptake_factor
soil_nitrogen_compounds_concentration = args.soil_nitrogen_compounds_concentration
tree_mass = args.tree_mass



delta_tree_mass: float = tree_mass + soil_nitrogen_compounds_concentration * nitrogen_uptake_factor

file_delta_tree_mass = open("/tmp/delta_tree_mass_" + id + ".json", "w")
file_delta_tree_mass.write(json.dumps(delta_tree_mass))
file_delta_tree_mass.close()
