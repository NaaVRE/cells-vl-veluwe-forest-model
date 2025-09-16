
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--my_dataset3', action='store', type=int, required=True, dest='my_dataset3')

arg_parser.add_argument('--my_dataset4', action='store', type=str, required=True, dest='my_dataset4')


args = arg_parser.parse_args()
print(args)

id = args.id

my_dataset3 = args.my_dataset3
my_dataset4 = args.my_dataset4.replace('"','')





file_my_output1 = open("/tmp/my_output1_" + id + ".json", "w")
file_my_output1.write(json.dumps(my_output1))
file_my_output1.close()
