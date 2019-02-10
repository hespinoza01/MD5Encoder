class console(object):
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def error(*args):
        argsv = ["{}".format(arg) for arg in args][1:]
        print("{0}{2}{1}".format(console.FAIL, console.ENDC, " ".join(argsv)))

    @classmethod
    def success(*args):
        argsv = ["{}".format(arg) for arg in args][1:]
        print("{0}{2}{1}".format(console.OKGREEN, console.ENDC, " ".join(argsv)))

    @classmethod
    def warning(*args):
        argsv = ["{}".format(arg) for arg in args][1:]
        print("{0}{2}{1}".format(console.WARNING, console.ENDC, " ".join(argsv)))