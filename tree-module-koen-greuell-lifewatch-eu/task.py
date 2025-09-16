
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--nitrogen_uptake_factor', action='store', type=float, required=True, dest='nitrogen_uptake_factor')

arg_parser.add_argument('--soil_nitrogen_compounds_concentration', action='store', type=float, required=True, dest='soil_nitrogen_compounds_concentration')

arg_parser.add_argument('--stored_tree_mass', action='store', type=float, required=True, dest='stored_tree_mass')


args = arg_parser.parse_args()
print(args)

id = args.id

nitrogen_uptake_factor = args.nitrogen_uptake_factor
soil_nitrogen_compounds_concentration = args.soil_nitrogen_compounds_concentration
stored_tree_mass = args.stored_tree_mass



tree_mass_changes: float = stored_tree_mass + soil_nitrogen_compounds_concentration * nitrogen_uptake_factor

file_tree_mass_changes = open("/tmp/tree_mass_changes_" + id + ".json", "w")
file_tree_mass_changes.write(json.dumps(tree_mass_changes))
file_tree_mass_changes.close()
