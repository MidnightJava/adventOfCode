import collections
import time
from dataclasses import dataclass
from collections import defaultdict

start = time.perf_counter()
map = []
personen = []
nachbarn = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def pos2i(pos):
  return pos[0]*spalten+pos[1]


def addPos(pos1, pos2):
  return (pos1[0]+pos2[0], pos1[1]+pos2[1])


def sucheAttackFields(pos):
  attackFields = []
  for nachbar in nachbarn:
    target = addPos(pos, nachbar)
    if map[pos2i(target)] != '#':
      attackFields.append(target)
  return attackFields


def sucheFreieNachbarn(pos):
  freieNachbarn = []
  for nachbar in nachbarn:
    target = addPos(pos, nachbar)
    if map[pos2i(target)] == '.':
      freieNachbarn.append(target)
  return freieNachbarn


def attackEnemy(person):
  attackEnemies = []
  for pos in sucheAttackFields(person.pos):
    if pos in enemies:
      attackEnemies.append(enemies[pos])
  if attackEnemies:
    enemy = sorted(attackEnemies, key=lambda a: (a.hp, a.pos))[0]
    person.attackEnemy(enemy)
    return True
  return False


@dataclass
class Person():
  typ: str
  pos: tuple
  attack: int
  hp: int = 200

  def attackEnemy(self, enemy):
    enemy.hp -= self.attack
    if enemy.hp < 1:
      map[pos2i(enemy.pos)] = '.'

  def move(self, newPos):
    map[pos2i(self.pos)] = '.'
    map[pos2i(newPos)] = self.typ
    self.pos = newPos


with open('data/Day15') as f:
  for z, zeile in enumerate(f):
    zeile = zeile.strip()
    for sp, zeichen in enumerate(zeile):
      map.append(zeichen)
      if zeichen == 'G':
        personen.append(Person(zeichen, (z, sp), 3))
      elif zeichen == 'E':
        personen.append(Person(zeichen, (z, sp), 3))
spalten = len(zeile)


def bfs(person):
  visited, queue, gefundeneZiele = set(), collections.deque(), []
  root = person.pos
  queue.append((root, 0, []))
  visited.add(root)
  tiefe = 0
  while True:
    vertex, d, path = queue.popleft()
    if d > tiefe:
      tiefe += 1
      if gefundeneZiele:
        # zuerst nach zielfeld (zeile, spalte = y,x) und dann nach erstem Schritt zum Ziel (zeile, spalte = y,x) sortieren
        gefundeneZiele.sort(key=lambda x: (x[0], x[1]))
        return gefundeneZiele[0][1]
    for nachbar in sucheFreieNachbarn(vertex):
      if nachbar not in visited:
        visited.add(nachbar)
        queue.append((nachbar, tiefe+1, path+[vertex]))
        if nachbar in targets:
          path += [vertex]+[nachbar]
          gefundeneZiele.append([nachbar, path[1]])
    if not queue:
      return


beendet = False
runde = 0
hitmap = defaultdict(int)
while not beendet:
  runde += 1
  personen.sort(key=lambda a: a.pos)
  for person in personen:
    if person.hp < 1:
      continue
    targets = set()
    enemies = {}

    for enemy in personen:
      if person.typ == enemy.typ or enemy.hp < 1:
        continue
      targets.update(sucheFreieNachbarn(enemy.pos))
      enemies[enemy.pos] = enemy

    if not enemies:
      beendet = True
      runde -= 1
      break

    if not attackEnemy(person):
      pos = bfs(person)
      if pos:
        person.move(pos)
        attackEnemy(person)

    hitmap[runde]+= person.hp


summeHitPoints = sum([p.hp for p in personen if p.hp > 0])
print()
print('Vollendete Runden: ', runde)
print('Summe HitPoints  : ', summeHitPoints)
print('Lösung           : ', runde*summeHitPoints)
print('gefunden in        ', time.perf_counter()-start)
print(hitmap)
