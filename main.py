import time

ttt = input("choose and write one of these 'countdown' or 'stopwatch' : ")


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        hour, mins = divmod(mins, 60)
        tformat = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)

        print(tformat)

        time.sleep(1)
        t -= 1

        if t == 0:
            t = False
            print("Time is up")

            from win10toast import ToastNotifier
            ToastNotifier().show_toast(title="Time is up!", msg="You can stop studying.",
                               duration=20, threaded=True)



def stopwatch(s):

    while s:


        mins, secs = divmod(s, 60)
        hour, mins = divmod(mins, 60)
        sformat = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)

        print(sformat)
        time.sleep(1)
        s += 1

        if s == stop_w:

            print("Time is up")

            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title="Time is full!", msg="You can rest",
                                       duration=20, threaded=True)

            s = False


if ttt == "countdown" or ttt == "Countdown":

    seconds = input("enter an integer for countdown: ")
    seconds = int(seconds)
    countdown(seconds)

if ttt == "stopwatch":

    stop_w = int(input("enter an integer for stopwatch: "))
    stopwatch(1)











