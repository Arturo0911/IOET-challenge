#!/usr/bin/python

import sys
import re
from pprint import pprint
from typing import (
    List,
    Any)

FILE_NAME = "Acme-offers.txt"

"""
>>> run this snipet if you make 
>>> the files to test the script

file_content =>

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

def make_files_content():
    pass


['MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00']
['MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
['MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2



RENE
['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']

ASTRID
['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']

ANDRES
['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']


schedule form:

{'ANDRES': ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00'],
 'ASTRID': ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00'],
 'RENE': ['MO10:00-12:00',
          'TU10:00-12:00',
          'TH01:00-03:00',
          'SA14:00-18:00',
          'SU20:00-21:00']}



"""


def match_keys(value_1: List[str], value_2: List[str]) -> int:
    
    schedule_match = [value for value in value_1 if value in value_2]
    return len(schedule_match)


def challenge_solution() -> None:

    with open(FILE_NAME, "r") as f:
        file = f.readlines()
    file = [x.strip("\n") for x in file]

    
    # schedule = dict()
    
    # for x in file:
    #     name = re.search(r'\w{4,}', x)
    #     content = re.findall(r'\=(.*)', x)
    #     schedule[name.group()] = content[0].split(",")

    schedule = {re.search(r'\w{3,}', x).group():re.findall(r'\=(.*)', x)[0].split(",") for x in file }

    try:
        for pos, (key,value) in enumerate(schedule.items()):
        
            for new_key, new_value in schedule.items():
                if key != new_key:
                    # print(f"{key}-{new_key}:{match_keys(value, new_value)}")
                    print("\n\n\n")
                else:
                    break
    except Exception as e:
        print(str(e))

    pprint(schedule)

def main():
    challenge_solution()

if __name__ == "__main__":
    main()
