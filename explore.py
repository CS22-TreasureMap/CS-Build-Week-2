from utils import *

mappy = mapper()
mappy.accumulate=False   #set pick up items to false
mappy.import_text_map=True
mappy.create_starting_map()

# mappy.explore_random(150)
# mappy.get_treasure()
mappy.get_coins()
# mappy.hint_to_ld8() #Translate the hint using ld8
# mappy.go_to_room(476)
# mappy.get_proof()

#461 shrine
# mappy.action('pray')
# mappy.dash_to_room(476)