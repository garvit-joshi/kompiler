from os import system, path
from time import sleep, ctime
from sys import argv


if __name__ == "__main__":
    args_len = len(argv)
    if args_len == 1:
        print("Please give a file name to watch")
        exit()
    elif args_len == 2:
        command = "g++ " + argv[1]
    else:
        command = "g++ " + (" ".join(argv[1:]))
    try:
        timer = ctime(path.getmtime(argv[1]))
    except FileNotFoundError:
        print("File:", argv[1],"Not Found" )
        exit()
    last_timer = 0
    while True:
        if last_timer == 0:
            last_timer = timer
            timer = ctime(path.getmtime(argv[1]))
        if timer != last_timer:
            system("clear")
            system(command)
        last_timer = timer
        timer = ctime(path.getmtime(argv[1]))
        sleep(1)
