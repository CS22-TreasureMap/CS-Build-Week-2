from utils import *

mappy = mapper()
mappy.accumulate=True   #set pick up items to false
mappy.import_text_map=True
mappy.create_starting_map()

# mappy.explore_random(150)

# Get coins
# mappy.wishing_well()
# mappy.dash_to_room(55)
# mappy.hint_to_ld8()
# mappy.go_to_room(483)
# mappy.dash_to_room()
# mappy.get_proof()

# mappy.go_to_room(461) # Linh's shrine
# mappy.room_check
# mappy.go_to_room(499) # Glasowyn's Grave

# Infinite $$
mappy.get_treasure()