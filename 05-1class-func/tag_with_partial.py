from tag import tag
from functools import partial

# tag -> callable, img -> name
picture = partial(tag, 'img', cls='pic-frame')
# src='wumpus.jpeg' -> attrs
print(picture(src='wumpus.jpeg'))
