import random
from difflib import get_close_matches
from datetime import datetime
import sys 
list_of_greetings = ['Hello',
                        'Hi there',
                        'Greetings',
                        'Good morning',
                        'Good afternoon',
                        'Good evening',
                        'Hey',
                        'Howdy',
                        'What\'s up',
                        'How\'s it going',
                        'Salutations',
                        'Welcome',
                        'Hiya',
                        'What\'s new',
                        'Long time no see',
                        'Nice to see you',
                        'How have you been',
                        'It\'s great to see you',
                        'Cheers',
                        'How\'s everything?'  
                                            ]

list_status_checkers = ['How are you',
                        'What\'s up',
                        'How are things',
                        'How are you doing',
                        'How\'s it going',
                        'How\'s everything',
                                            ]

list_of_goodbyes = [
                      'goodbye',
                      'bye'
                      'see you later',
                      'take care',
                      'farewell',
                      'catch you later',
                      'have a great day',
                      'until next time',
                      'so long',
                      'later',
                      'peace out',
                      'adios',
                      'see you soon',
                      'goodbye for now',
                      'stay safe',
                      'wish you well'
                  ]

list_of_time_requests = [
                      'what time is it',
                      'tell me the time',
                      'what’s the time',
                      'give me the time',
                      'how late is it',
                      'can you tell me the time',
                      'what’s the current time',
                      'what time do you have',
                      'show me the time',
                      'what hour is it',
                      'is it time yet',
                      'how much time has passed',
                      'what time should I be there',
                      'what time does it say',
                      'do you have the time',
                      'do you know the time?'
                  ]



class Chatabot:
  def __init__(self, name: str, version: int) -> None:
    self.name = name
    self.version = version


  def greeting(self, ) -> None:
    random_greeting = random.choice(list_of_greetings)
    print(f'{self.name}: {random_greeting}')


  def status_checker(self, ) -> None:
    random_status_checker = random.choice(list_status_checkers)
    print(f'{self.name}: I\'m very well. {random_status_checker}')

  
  def goodbye(self, ) -> None:
    print(f'{self.name}: Farewell!')


  def get_time(self, ) -> None:
    now = datetime.now()
    print(f'{self.name}: {now:%H:%M:%S}')


def is_greeted(user_input) :
  user_input = user_input.strip().capitalize()
  if get_close_matches(user_input, list_of_greetings, n=1, cutoff=0.6) :
    return True
  else :
    return False  


def is_status_checked(user_input) :
  user_input = user_input.strip().lower()
  if get_close_matches(user_input, list_status_checkers, n=1, cutoff=0.6) :
    return True
  else :
    return False


def is_asking_time(user_input: str) -> bool:
  user_input = user_input.strip().lower()
  if get_close_matches(user_input, list_of_time_requests, n=1, cutoff=0.6) :
    return True
  else :
    return False


def is_going(user_input) :
  user_input = user_input.strip().lower()
  if get_close_matches(user_input, list_of_goodbyes, n=1, cutoff=0.6) :
    return True
  else :
    return False


def km_to_mi(kilometers: float) -> float:
        return round(kilometers * 0.621371, 2)



def mi_to_km(miles: float) -> float:
        return round(miles * 1.60934, 2)


def c_to_f(celsius: float) -> float:
        return round((celsius * 9/5) + 32, 2)


def f_to_c(farenheit: float) -> float:
        return round((farenheit - 32) * 5/9, 2)


def ounces_to_gr(ounces: float) -> float:
  return round(ounces * 28.3495, 2)


def gr_to_ounces(grams: float) -> float:
  return round(grams * 0.03527396, 2)


def input_checker(user_input: str) -> float:
  try:
    float_input: float = float(user_input)
    return float_input
  except ValueError:
    print('Enter a valid number tho...')
    return None
  except TypeError:
    print('Enter a valid number tho...')
    return None


def number_finder(user_input: str) -> float:
  words = user_input.split()
  found_numbers: list = []
  for word in words :
    try:
      number = float(word)
      found_numbers.append(number)
    except ValueError :
      continue
    return found_numbers[0]


def find_conversion(user_input: str) -> str | None:
  conversions: list = ['kilometers to miles', 'km to mi', 'km to miles', 'kilometers to mi',
                      'miles to kilometers', 'mi to km', 'miles to km', 'mi to kilometers',
                      'celsius to farenheit', 'c to f', 'celsius to f', 'c to farenheit',
                      'farenheit to celsius', 'f to celsius', 'farenheit to c', 'f to c',
                      'ounces to grams', 'oz to grams', 'oz to gr', 'ounces to grams',
                      'grams to ounces', 'gr to oz', 'grams to oz', 'gr to ounces',]

  matches: list = get_close_matches(user_input, conversions, n=1, cutoff=0.6)
  return matches[0] if matches else None


def main() -> None:
  bot = Chatabot('ChataBot', 1)

  while True :
    user_input: str = input('You: ').lower()

    if is_greeted(user_input) and is_status_checked(user_input):
      bot.greeting()
      bot.status_checker()
      continue
    elif is_greeted(user_input):
      bot.greeting()
      continue
    elif is_status_checked(user_input):
      bot.status_checker()
    elif is_going(user_input):
      bot.goodbye()
      break
    elif is_asking_time(user_input):
      bot.get_time()
      continue
  

    numbers: float = number_finder(user_input)
    float_input: float = input_checker(numbers)
    conversion: str = find_conversion(user_input)


    if conversion in ['kilometers to miles', 'km to mi', 'km to miles', 'kilometers to mi'] :
      if float_input :
                print(f'{float_input} km is {km_to_mi(float_input)} miles.')
                continue

    elif conversion in ['miles to kilometers', 'mi to km', 'miles to km', 'mi to kilometers'] :
            if float_input is not None :
                print(f'{float_input} miles is {mi_to_km(float_input)} km')
                continue

    elif conversion in ['celsius to farenheit', 'c to f', 'celsius to f', 'c to farenheit'] :
            if float_input is not None :
                print(f'{float_input} celsius is {c_to_f(float_input)} f')
                continue

    elif conversion in ['farenheit to celsius', 'f to celsius', 'farenheit to c', 'f to c'] :
            if float_input is not None :
                print(f'{float_input} farenheit is {f_to_c(float_input)} c')
                continue

    elif conversion in ['ounces to grams', 'oz to grams', 'oz to gr', 'ounces to grams'] :
            if float_input is not None :
                print(f'{float_input} ounces is {ounces_to_gr(float_input)} gr')
                continue

    elif conversion in ['grams to ounces', 'gr to oz', 'grams to oz', 'gr to ounces'] :
            if float_input is not None :
                print(f'{float_input} grams is {gr_to_ounces(float_input)} ounces')
                continue

    else:
      print(f'{bot.name}: Sorry, I didn\'t get that.')
      continue

if __name__ == '__main__':
  main()