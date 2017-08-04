import regex
import random

dicere = regex.compile('(\d*)d(\d+)([-+]\d+)?')
repeatre = regex.compile('(\d+)m(.*)')

def roll(string):
    string.replace(" ", "")
    match = repeatre.search(string)
    repeats = 1
    if match:
        print(string, match, match[0], match[1], match[2])
        repeats = int(match[1])
        string = match[2]
    results = []
    match = dicere.search(string)
    if match:
        print(string, match, match[0], match[1], match[2], match[3])
        for x in range(repeats):
            result = dice(match[1], match[2], match[3])
            results.append(result)
        output = "**Dice Roll:** " + match.group(0)
        for result in results:
            output = output + "\n" + result
        return output
    else:
        return "Couldn't interpret that roll"

def dice(count, faces, add):
    if count is None or count == "":
        count = 1
    else:
        count = int(count)
    faces = int(faces)
    results = []
    total = 0
    if add is not None:
        total = total + int(add)
    for x in range(count):
        result = random.randint(1, faces)
        results.append(result)
        total = total + result
    string = ""
    if count > 0:
        for x in range(count):
            if x != 0:
                string = string + ", "
            string = string + str(results[x])
    string = "**d" + str(faces) + " Results:** " + string + " (Total = " + str(total) + ")"
    return string