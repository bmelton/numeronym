def numeronym(input):
    f = input[0]
    l = input[-1]
    output = "%s%d%s" % (f, len(input[1:-1]), l)
    return output.lower()
