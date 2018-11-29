def main():
  print('Welcome to squares of prime numbers!')

  num_file = open('number.txt', 'r')

  for square in num_file:
    total = int(square)

    squared = total**2

    print('Num =', total, '\t', 'Squared = ', squared)

  num_file.close()

main()
