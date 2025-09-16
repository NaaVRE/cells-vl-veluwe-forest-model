
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--intial_stored_tree_mass', action='store', type=float, required=True, dest='intial_stored_tree_mass')

arg_parser.add_argument('--tree_mass_changes', action='store', type=float, required=True, dest='tree_mass_changes')


args = arg_parser.parse_args()
print(args)

id = args.id

intial_stored_tree_mass = args.intial_stored_tree_mass
tree_mass_changes = args.tree_mass_changes



stored_tree_mass = intial_stored_tree_mass

stored_tree_mass = stored_tree_mass + tree_mass_changes

file_stored_tree_mass = open("/tmp/stored_tree_mass_" + id + ".json", "w")
file_stored_tree_mass.write(json.dumps(stored_tree_mass))
file_stored_tree_mass.close()
