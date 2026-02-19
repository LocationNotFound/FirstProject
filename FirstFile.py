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
    result += 1
  print(result)


