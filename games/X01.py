from boardreader.bed_map import BED_MAP
from boardreader.dart_reader import DartReader
from es.es_client import EsClient
import random

class X01:
    def __init__(self, points):
        self.TOTAL_POINTS = points

    def play_game(self):
        reader = DartReader()
        points_left = self.TOTAL_POINTS
        points_left_last_round = self.TOTAL_POINTS
        round_count = 0
        keep_playing = True;
        darts_thrown = 0
        while (keep_playing):
            last_round = points_left
            round_count += 1
            print "Round: %s" % round_count
            for x in range(1,4):
               print "Dart " + str(x)
               print "  Points Left: %s" % points_left
               hit_pins = reader.read_dart_pins()
               hit_dart = BED_MAP.get(hit_pins)
               print "  Hit: " + str(hit_dart.get('modifier')) + " " + str(hit_dart.get('number'))
               points = hit_dart.get('points')
               darts_thrown += 1
            
               if(points > points_left):
                   points_left = points_left_last_round
                   break
               elif(points == points_left):
                   print "WINNER WINNER CHICKEN DINNER"
                   keep_playing = False
                   break
    

               points_left = points_left - points
               print "--------"

            points_left_last_round = points_left

        ppd = self.TOTAL_POINTS/darts_thrown
        ppr = ppd * 3

        print "Points per dart = %s" % ppd
        print "Points per round = %s" % ppr
