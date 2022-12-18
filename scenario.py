hero = {
  'name': 'hero',
  'slots': 3
}

scenes = [ 
  { 'key': 'start',
    'title': 'Start',
    'story': 'Situation start... what to do?',
    'options': [
      {'key': 'c', 'next' : 'cave', 'story' : 'the dark and misty cave'},
      {'key': 'h', 'next' : 'hut', 'story' : 'the old wooden hut'},
      {'key': 't', 'next' : 'tree', 'story' : 'the thick old tree'},
    ]
  },
  { 'key': 'cave',
    'title': 'Cave',
    'story': 'Situation cave... wat te doen?',
    'options': [
      {'key': 'r', 'next' : 'river', 'story' : 'You choose to the river'},
      {'key': 'b', 'next' : 'bear-nest', 'story' : 'You choose to the bear nest'},
      {'key': 'l', 'next' : 'lava-chimney', 'story' : 'You choose to the lava chimney'},
    ]
  },
  { 'key': 'hut',
    'title': 'Hut',
    'story': 'Situation hut... wat te doen?',
    'options': [
      {'key': 'a', 'next' : 'attic', 'story' : 'You choose to the attic'},
      {'key': 'b', 'next' : 'bath room', 'story' : 'You choose to the bath room nest'},
      {'key': 'c', 'next' : 'cellar', 'story' : 'You choose to the cellar'},
    ]
  },
  { 'key': 'tree',
    'title': 'Tree',
    'story': 'Situation tree... what is there?',
    'options': [
      {'key': 'r', 'next' : 'e', 'story' : 'You choose to the river'},
      {'key': 'b', 'next' : 'bear-nest', 'story' : 'You choose to the bear nest'},
      {'key': 'l', 'next' : 'lava-chimney', 'story' : 'You choose to the lava chimney'},
    ]
  },
  { 'key': 'bear-nest',
    'title': 'Empty bears nest',
    'story': 'Situation bear... wat te doen?',
    'options': [
      {'key': 'a', 'next' : 'river', 'story' : 'You choose to the river'},
      {'key': 'b', 'next' : 'bear-nest', 'story' : 'You choose to the bear nest'},
      {'key': 'l', 'next' : 'lava-chimney', 'story' : 'You choose to the lava chimney'},
    ]
  },
  { 'key': 'attic',
    'title': 'Attic',
    'story': 'Situation attic... wat te doen?',
    'options': [
      {'key': 'a', 'next' : 'attic', 'story' : 'You choose to the attic'},
      {'key': 'b', 'next' : 'bath room', 'story' : 'You choose to the bath room nest'},
      {'key': 'c', 'next' : 'cellar', 'story' : 'You choose to the cellar'},
    ]
  },
  { 'key': 'river',
    'title': 'River',
    'story': 'Situation river... wat te doen?',
    'options': [
      {'key': 'a', 'next' : 'death', 'story' : 'You choose to the attic'},
      {'key': 'b', 'next' : 'death', 'story' : 'You choose to the bath room nest'},
      {'key': 'c', 'next' : 'death', 'story' : 'You choose to the cellar'},
    ]
  },
  { 'key': 'death',
    'title': 'Death',
    'story': 'You died, so sad!',
    'end': 'There\'s no more to explore!',
    'options': [
    ]
  },
]

items = [

]

dangers = [
  { 'key': 'bear',
    'name': 'Grizzly bear with giant claws',
    'story': '''Situatie bear... wat te doen?''',
    'options': [
      {'key': 'a', 'action' : 'attack', 'effects' : 'You choose to the river'},
      {'key': 'f', 'next' : 'freeze', 'story' : 'You choose to the bear nest'},
      {'key': 'r', 'next' : 'run', 'story' : 'You choose to the lava chimney'},
      {'key': 'h', 'next' : 'hide', 'story' : 'You choose to the lava chimney'},
    ]
  }
]