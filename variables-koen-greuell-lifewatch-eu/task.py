
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_nitrogen_uptake_factor', action='store', type=float, required=True, dest='param_nitrogen_uptake_factor')
arg_parser.add_argument('--param_soil_nitrogen_compounds_concentration', action='store', type=float, required=True, dest='param_soil_nitrogen_compounds_concentration')

args = arg_parser.parse_args()
print(args)

id = args.id


param_nitrogen_uptake_factor = args.param_nitrogen_uptake_factor
param_soil_nitrogen_compounds_concentration = args.param_soil_nitrogen_compounds_concentration


nitrogen_uptake_factor = param_nitrogen_uptake_factor
soil_nitrogen_compounds_concentration = param_soil_nitrogen_compounds_concentration

file_nitrogen_uptake_factor = open("/tmp/nitrogen_uptake_factor_" + id + ".json", "w")
file_nitrogen_uptake_factor.write(json.dumps(nitrogen_uptake_factor))
file_nitrogen_uptake_factor.close()
file_soil_nitrogen_compounds_concentration = open("/tmp/soil_nitrogen_compounds_concentration_" + id + ".json", "w")
file_soil_nitrogen_compounds_concentration.write(json.dumps(soil_nitrogen_compounds_concentration))
file_soil_nitrogen_compounds_concentration.close()
