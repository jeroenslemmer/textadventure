QUESTION_TODO = 'what to do?'
def get_options(options):
  string = ''
  short = ''
  for index in range (len(options)):
    if string > '':
      if index == len(options):
        short += ' or '
      else:
        short += ', '
    string += f"{options[index]['key']}: {options[index]['story']}\n"
    short += f"{options[index]['key']}"
  return string, short

def get_keys(options):
  keys = []
  for option in options:
    keys.append(option['key'])
  return keys

def display_choice(prompt):
  print(prompt)
  print(QUESTION_TODO)

def display_short_choice(prompt):
  print(prompt)

def choose(prompt, short_prompt, keys):
  display_choice(prompt)
  answer = ''
  while not answer in keys:
    answer = input('? ')
    if not answer in keys:
      display_short_choice(short_prompt)
  return answer

def get_items_text(items):
  string = ''
  for index in range(len(items)):
    if string > '':
      if index == len(get_items_text):
        string += ' or '
      else:
        string += ', '
    string += items[index]
    
  return string

def display_scene(scene):
  print(scene['title'])
  print(scene['story'])
  print(get_items_text(scene['items']))
  if 'end' in scene:
    print(scene['end'])

def get_next(scene,key_stroke):
  for option in scene['options']:
    if option['key'] == key_stroke:
      return option['next']
  raise Exception(f"Undefined next scene for key stroke: {key_stroke}") 

def dispose_items(scene, hero):
  pass
def pick_items(scene, hero):
  pass

def play_scene(scene, hero):
  display_scene(scene)
  new_items = pick_items(scene, hero)
  long_choice, short_choice = get_options(scene['options'])
  answer = choose(long_choice, short_choice, get_keys(scene['options']))
  return get_next(scene, answer)

def get_scene(scenes, scene_key):
  for scene in scenes:
    if scene['key'] == scene_key:
      return scene
  raise Exception(f"Undefined scene for: {scene_key}") 

def game_ends(scene):
  if 'end' in scene and scene['end'] > '':
    return True
  else:
    return False

def game(scenes, hero, start_key):
  scene = get_scene(scenes,start_key)
  while not game_ends(scene):
    next = play_scene(scene, hero)
    scene = get_scene(scenes,next)
  display_scene(scene)