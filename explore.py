from utils import *

mappy = mapper()
mappy.accumulate=True   #set pick up items to false
mappy.import_text_map=True
mappy.create_starting_map()

# mappy.explore_random(150)
# mappy.dash_to_room(461) # Linh's shrine
# mappy.dash_to_room(499) # Glasowyn's Grave


# Infinite $$
# mappy.get_treasure()

# All the coins
mappy.auto_coins()