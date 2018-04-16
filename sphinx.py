import json

speach = {
    "01": ['You heard me before, yet you hear me again, Then I die, ’till you call me again.', 'echo']
    "02": ['Die without me, Never thank me. Walk right through me, never feel me. Always watching, never speaking. Always lurking, never seen.', 'air']
    "03": ['When young, I am sweet in the sun. When middle-aged, I make you gay. When old, I am valued more than ever.', 'wine']
    "04": ['Ripped from my mother’s womb, Beaten and burned, I become a blood thirsty killer. What am I?', 'iron']
    "05": ['Half-way up the hill, I see thee at last, lying beneath me with thy sounds and sights — A city in the twilight, dim and vast, with smoking roofs, soft bells, and gleaming lights.', 'past']
    "06": ['If you break me I do not stop working, If you touch me I may be snared, If you lose me Nothing will matter.', 'heart']
    "07": ['Welcome stranger. You may seat or stay or just lose your way']
    "08": ['Try to solve, don`t mistake or i cut your head away']

with open("text.json", "w") as textfile:
    json.dump(speach, textfile)
