# coding: utf8

import collections
import itertools
import random
import sys


MAX_VALUE = 6
NUM_DIGITS = 4
NUM_TRIES = 6
NUM_TOTAL_POSSIBILITIES = MAX_VALUE ** NUM_DIGITS

_CODES = None
_COUNT = None
_POSSIBILITIES = None


HELP_HELPER = ("Veuillez entrer soit 'state' pour connaitre les possibilités "
               "restantes, soit 'help' pour connaitre le meilleur coup "
               "possible, soit 'win' pour indiquer que vous avez gagné, soit "
               "<code> <noirs> <blancs> pour mettre à jour.")

HELP_FREE_GAME = ("Veuillez entrer soit 'state' pour connaitre les "
                  "possibilités restantes, soit 'help' pour connaitre le "
                  "meilleur coup possible, soit <code> pour proposer une "
                  "réponse.")

WELCOME = 'Bienvenue !'


class Bot(object):
  def __init__(self):
    self.state = set(GetAllCodes())

  def Reset(self):
    self.__init__()

  def GetState(self):
    print 'Possibilités restantes: ' + str(sorted(list(self.state)))

  def HasWon(self):
    return not self.state

  def GetAdvice(self):
    min_max_possibilities = NUM_TOTAL_POSSIBILITIES
    min_codes = []
    for code in _CODES:
      max_possibilities = max(
          [len(possibilities.intersection(self.state))
           for possibilities in GetPossibilities(code).values()])
      if max_possibilities < min_max_possibilities:
        min_max_possibilities = max_possibilities
        min_codes = [code]
      if max_possibilities == min_max_possibilities:
        min_codes.append(code)
    intersection = self.state.intersection(min_codes)
    best_guess = min(min_codes)
    if intersection:
      best_guess = min(intersection)
      print 'Meilleur coup: ' + best_guess

  def Update(self, code, black, white):
    self.state = self.state.intersection(GetPossibilities(code)[(black, white)])


def Helper():
  print WELCOME
  print HELP_HELPER
  bot = Bot()
  while True:
    user_input = raw_input()
    if user_input == 'state':
      bot.GetState()
    elif user_input == 'help':
      bot.GetAdvice()
    elif user_input == 'win':
      print 'Hourra ! Beaucoup trop facile !'
      bot.Reset()
    else:
      try:
        code, black, white = user_input.split(' ')
        bot.Update(code, int(black), int(white))
      except:
        print HELP_HELPER


class Game(object):
  def __init__(self):
    self.bot = Bot()
    self.remaining_tries = NUM_TRIES
    self.code = self.GenerateCode()

  def Reset(self):
    self.__init__()

  def GenerateCode(self):
    return GetAllCodes()[random.randint(0, NUM_TOTAL_POSSIBILITIES - 1)]


def FreeGame():
  game = Game()
  print WELCOME
  print HELP_FREE_GAME
  while True:
    user_input = raw_input()
    if user_input == 'state':
      game.bot.GetState()
    elif user_input == 'help':
      game.bot.GetAdvice()
    else:
      try:
        black, white = ComputeProximity(user_input, game.code)
        game.bot.Update(user_input, int(black), int(white))
        game.remaining_tries -= 1
        if black == NUM_DIGITS:
          print 'Tu as gagné! Il te restait {} essai(s).'.format(
              str(game.remaining_tries))
          game.Reset()
          continue
        print 'Noirs: {} Blancs: {} Essais restants: {}'.format(
            str(black), str(white), str(game.remaining_tries))
        if not game.remaining_tries:
          print 'Tu as perdu... Le code était: ' + game.code
          game.Reset()
      except:
        print HELP_FREE_GAME


def GetCount(code):
  global _COUNT
  if not _COUNT:
    _COUNT = {}
    for code_iterator in GetAllCodes():
      _COUNT[code_iterator] = [0] * MAX_VALUE
      for digit in code_iterator:
        _COUNT[code_iterator][int(digit) - 1] += 1
  return _COUNT[code]


def GetAllCodes():
  global _CODES
  if not _CODES:
    digits = [str(i) for i in xrange(1, MAX_VALUE + 1)]
    _CODES = sorted([''.join(list_digits) for list_digits in
                    itertools.product(*([digits] * NUM_DIGITS))])
  return _CODES


def ComputeProximity(n, m):
  black = len([0 for d1, d2 in zip(n, m) if d1 == d2])
  count_n = GetCount(n)
  count_m = GetCount(m)
  black_and_white = sum([min(c1, c2) for c1, c2 in zip(count_n, count_m)])
  return black, black_and_white - black


def GetPossibilities(code):
  global _POSSIBILITIES
  if not _POSSIBILITIES:
    _POSSIBILITIES = collections.defaultdict(
        lambda: collections.defaultdict(set))
    for n in GetAllCodes():
      for m in GetAllCodes():
        if n < m:
          proximity = ComputeProximity(n, m)
          _POSSIBILITIES[n][proximity].add(m)
          _POSSIBILITIES[m][proximity].add(n)
  return _POSSIBILITIES[code]


def main():
  try:
    game_mode = sys.argv[1].upper()
  except:
    FreeGame()
    return
  if game_mode == 'HELP':
    Helper()
  else:
    FreeGame()

if __name__ == '__main__':
  main()
