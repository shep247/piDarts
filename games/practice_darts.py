from boardreader.bed_map import BED_MAP
from boardreader.dart_reader import DartReader
from es.es_client import EsClient
import random

MODIFIERS = ['Little'] + ['Double'] * 2 + ['Big'] * 4 +  ['Triple'] * 4
BULL_MODIFIERS = ['Big'] * 3 + ['Double']
NUMBERS = range(1,15) * 2 + range(15,21) * 3 + [25] * 4

def get_dart_pins(modifier, number):
    return (k for k,v in BED_MAP.items() if v.get('modifier') == modifier and v.get('number') == number).next()

def get_random_aim():
    number = random.choice(NUMBERS)
    modifier = random.choice(BULL_MODIFIERS if number == 25 else MODIFIERS)
    return (modifier, number)

if __name__ == "__main__":
    reader = DartReader()
    es = EsClient()
    while (True):
        aim_pins = get_dart_pins(*get_random_aim())
        aim_dart = BED_MAP.get(aim_pins) 
        print "Aim For: " + str(aim_dart.get('modifier')) + " " + str(aim_dart.get('number'))

        hit_pins = reader.read_dart_pins()
        hit_dart = BED_MAP.get(hit_pins)
        print "  Bed Hit: " + str(hit_dart.get('modifier')) + " " + str(hit_dart.get('number'))
        was_hit = aim_pins == hit_pins
        print "HIT" if was_hit else "MISS"
        es.push_dart_to_es(aim_dart, hit_dart, was_hit, 'george', 'random_practice')
        print "---------------------------"
    
