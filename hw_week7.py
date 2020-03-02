import random

def hw_week7(secret_number):
  if int(secret_number) == 16:
    print(f'Good job! You guessed my number !')
  elif int(secret_number) > 16:
    print('Your guess is too high.\nTake a guess.')
  else:
    print('Your guess is too low.\nTake a guess.')


if __name__ == '__main__':
    hw_week7(random.randint(1, 100))
