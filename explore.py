from utils import *

mappy = mapper()
mappy.accumulate=False   #set pick up items to false
mappy.import_text_map=True
mappy.create_starting_map()
mappy.explore_random(500)