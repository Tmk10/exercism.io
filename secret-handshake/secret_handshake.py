def handshake(code):
    result = []
    secret = {0: "wink", 1: "double blink", 2: "close your eyes", 3: "jump"}  # mapping gestures to positions in string
    position = list(enumerate(bin(code)[-1:1:-1]))  # cutting "0b" and enumerate bin numbers with place in string
    for flag in position:
        if flag[0] == 4 and flag[1] == "1":  # checking if list reverse is needed
            result.reverse()
            break
        else:
            # adding gesture to list if current flag is set to 1
            result.append(secret[flag[0]]) if flag[1] == "1" else None

    return result


def secret_code(actions):
    result = ["0", "0", "0", "0"]
    secret = {"wink": 0, "double blink": 1, "close your eyes": 2,
              "jump": 3, }  # mapping gestures to positions in string
    for item in actions:
        result[secret[item]] = "1"
    result.reverse()
    # checking order of flags, if bigger flag value appear before smaller, the list is reversed
    if len(actioons) > 1 and secret[actions[0]] > secret[actions[1]]:
        result.insert(0, "1")
    return int("".join(result), 2)










