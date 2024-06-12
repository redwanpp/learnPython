while True:
    user_input = input('> ')

    if user_input.lower() == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif user_input.lower() == 'start':
        print('Car started.....Ready to go!')
    elif user_input.lower() == 'stop':
        print('Car stopped.')
    elif user_input.lower() == 'quit':
        break
    else:
        print("I don't understand that....")