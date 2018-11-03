from elasticsearch import Elasticsearch
from datetime import datetime
from pytz import timezone
import ConfigParser

class EsClient:
    def __init__(self):
        cp = ConfigParser.ConfigParser(open('/home/pi/projects/piDarts/creds/esConfig.cfg'))
        self.es = Elasticsearch(cp.get('DEFAULT', 'esUrl'))
        self.timezone = timezone('US/Arizona')

    def push_dart_to_es(self, aim_dart, hit_dart, hit, player, game):
        body = {'aim_modifier': aim_dart.get('modifier'),
                'hit_modifier': hit_dart.get('modifier'),
                'aim_number': aim_dart.get('number'),
                'hit_number': hit_dart.get('number'),
                'aim_points': aim_dart.get('points'),
                'hit_points': hit_dart.get('points'),
                'player': player,
                'game': game,
                'hit': hit,
                'date_thrown': datetime.now(self.timezone)}
        self.es.index(index='rpdarts', doc_type='dart', body=body)

    def push_color_to_es(self, color, button):
        colors = {7:"red", 11:"green", 15:"blue", 0:"off"}
        button_text = {1:"change_button", 2:"display_button"}
        body = {'color': colors.get(color),
                'button': button_text.get(button),
                'date_clicked': datetime.now(self.timezone)}
        self.es.index(index='raspberrypi', doc_type='rgb', body= body)

