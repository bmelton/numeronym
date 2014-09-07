class Numeronym:
    def __init__(self, short=None, lower=None):
        # Default variables
        allow_short             = False
        return_lower            = True
        
        self.allow_short        = allow_short
        if short:
            self.allow_short    = short
        
        self.return_lower       = return_lower
        if lower:
            self.return_lower   = lower
        
        print self.allow_short
        print self.return_lower
        
    def encode(self, input):
        print "Lower: %s" % (self.return_lower)
        if len(input) < 4:
            if self.allow_short == True:
                f = input[0]
                output = "%s%d" % (f, len(input[1:]))
                if self.return_lower == True:
                    output = output.lower()

                return output
            else:
                raise Exception("Input string must be at least four characters in length")

        f = input[0]
        l = input[-1]

        output = "%s%d%s" % (f, len(input[1:-1]), l)

        if self.return_lower == True:
            output = output.lower()

        return output
