#if user types help, brings up all the command options
#if the user types anythings besides our 4 commands, prints "I don't understand..."
#if user types "start", the car is started
#if user types "stop" the car is stopped
#if the user types quit, program terminates

user_input = input(">")
started = False
stopped = True

while user_input.lower() != "quit":
  if user_input.lower() == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
  elif user_input.lower() == "start":
    if started:
      print("The car is started already!!!")
    else:
      print("Car started...Ready to go!")
      started = True
      stopped = False
  elif user_input.lower() == "stop":
    if stopped:
      print("The car is already stopped!!!")
    else:
      print("Car stopped.")
      stopped = True
      started = False
  elif user_input.lower() == "quit":
    exit()
  else:
    print("I don't understand that...")
  user_input = input(">")
