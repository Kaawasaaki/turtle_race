def number_of_racers:
  racers = 0
  while True:
    racers = input("Enter number of racers '2-10' : ")
    if racers.isdigit():
      racers = int(racers)
  else:
    print("Enter a valid number")
    continue()
