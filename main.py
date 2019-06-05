from lab10_python import Message


def main():
    message1 = Message('Message1', "Jimmy", 25, "Amy", "Iphone", "21:30")
    message2 = Message('Message2', "Jimmy")
    message3 = Message('Message3', "Jimmy", 25, "Amy")
    message1.MessageInfo()
    message2.MessageInfo()
    message3.MessageInfo()


if __name__ == '__main__':
  main()
