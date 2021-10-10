class ConsoleColor :
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger :

    @staticmethod
    def log(context : str,  message : str, warning = False, fail = False) -> None :
        if warning :
            print(ConsoleColor.OKBLUE + f"[WARNING][{context}] -> {message}" + ConsoleColor.ENDC)
        elif fail :
            print(ConsoleColor.FAIL + f"[ERROR][{context}] -> {message}" + ConsoleColor.ENDC)
        else :
            print(ConsoleColor.OKGREEN + f"[{context}] -> {message}" + ConsoleColor.ENDC)