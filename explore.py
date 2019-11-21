from utils import *

mappy = mapper()
mappy.accumulate=False   #set pick up items to false
mappy.import_text_map=True
mappy.create_starting_map()
mappy.transmogriphier()
mappy.transmogrify()
# mappy.equip_gear()
# mappy.unequip_gear('body')
# print(mappy.action(what='balance'))
# mappy.auto_coins()
# mappy.wishing_well()
# mappy.hint_to_ld8()
# mappy.dash_to_room(461)

# print(mappy.action(what='pray'))
# print(mappy.action(what='status'))
# mappy.go_to_room(482)
# mappy.get_proof()

# mappy.explore_random(150)
# mappy.get_treasure()
