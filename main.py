import sys
import json

arguments = sys.argv



with open(filename, "r") as source:
    data = json.load(source)
