import pi2go, time

speed = 40
turnspeed = 10
leftPrev = False
rightPrev = False


def followLine():
    left = pi2go.irLeftLine()
    right = pi2go.irRightLine()
    if left and right:
        pi2go.forward(speed)
    elif left and not right:
        pi2go.go(speed / 2 + turnspeed, speed / 2 - turnspeed)
    elif right and not left:
        pi2go.go(speed / 2 - turnspeed, speed / 2 + turnspeed)
    else:
        pi2go.forward(speed)


def wallDetected():
    if pi2go.irCentre():
        return True
    else:
        return False


def returnBack():
    while pi2go.irRightLine():
        pi2go.spinRight(speed)


# main program

pi2go.init()
try:
    pi2go.forward(speed)
    while True:
        if wallDetected():
            returnBack()
        else:
            followLine()

finally:
    pi2go.cleanup()
