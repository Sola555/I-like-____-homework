#make a list of things you like
#print I like ____
#join two lists together


list = []

while True:
  add = str(input("What is something that you like(type stop to stop)? : "))

  if add == 'stop':
    for likes in list:    
      print ("I like {}".format(likes))
    break
  else:
    list.append(str(add))

