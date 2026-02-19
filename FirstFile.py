from typing import final

@final
class RandomClass:
  pass

#Apparently, this should result in error
#class RandomClasses(RandomClass):
  #pass


def sum(*args):
  result = 0
  for i in args:
    result += i
  print(result)


def muk(*args):
  result = 1
  for i in args:
    result * i
  print(result)


