max = int(input("Enter max number: "))

def onlyOdd(max):
  oddList = []
  for i in range(1, max):
    if (i % 2) == 1:
      oddList.append(i)

  return oddList


def main():
  print("Odd numbers: ", onlyOdd(max))

main()