def prime(number):
  if number == 1 or number == 0:
    return False
  elif number == 2:
    return True
  elif number > 2:
    for divisor in range(2, number):
      if number % divisor == 0:
        return False
      elif number % divisor != 0 and divisor == number-1:
        return True
        
prime(265)        
