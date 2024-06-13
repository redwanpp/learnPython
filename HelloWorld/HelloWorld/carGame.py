started = False
while True:
    user_input = input('> ')

    if user_input.lower() == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif user_input.lower() == 'start':
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car started.....Ready to go!')
    elif user_input.lower() == 'stop':
        if not started:
            print('car already stopped')
        else:
            started = False
            print('Car stopped.')
    elif user_input.lower() == 'quit':
        break
    else:
        print("I don't understand that....")