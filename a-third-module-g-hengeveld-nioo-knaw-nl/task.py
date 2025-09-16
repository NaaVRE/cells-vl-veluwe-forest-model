
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--my_dataset31', action='store', type=str, required=True, dest='my_dataset31')

arg_parser.add_argument('--my_dataset310', action='store', type=int, required=True, dest='my_dataset310')

arg_parser.add_argument('--my_dataset32', action='store', type=int, required=True, dest='my_dataset32')

arg_parser.add_argument('--my_dataset33', action='store', type=str, required=True, dest='my_dataset33')

arg_parser.add_argument('--my_dataset34', action='store', type=int, required=True, dest='my_dataset34')

arg_parser.add_argument('--my_dataset35', action='store', type=str, required=True, dest='my_dataset35')

arg_parser.add_argument('--my_dataset36', action='store', type=int, required=True, dest='my_dataset36')

arg_parser.add_argument('--my_dataset37', action='store', type=str, required=True, dest='my_dataset37')

arg_parser.add_argument('--my_dataset38', action='store', type=int, required=True, dest='my_dataset38')

arg_parser.add_argument('--my_dataset39', action='store', type=str, required=True, dest='my_dataset39')


args = arg_parser.parse_args()
print(args)

id = args.id

my_dataset31 = args.my_dataset31.replace('"','')
my_dataset310 = args.my_dataset310
my_dataset32 = args.my_dataset32
my_dataset33 = args.my_dataset33.replace('"','')
my_dataset34 = args.my_dataset34
my_dataset35 = args.my_dataset35.replace('"','')
my_dataset36 = args.my_dataset36
my_dataset37 = args.my_dataset37.replace('"','')
my_dataset38 = args.my_dataset38
my_dataset39 = args.my_dataset39.replace('"','')





file_my_dataset310 = open("/tmp/my_dataset310_" + id + ".json", "w")
file_my_dataset310.write(json.dumps(my_dataset310))
file_my_dataset310.close()
