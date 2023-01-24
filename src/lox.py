import sys
from scanner import Scanner
from token import Token


class Lox:
    @staticmethod
    def main():
        print(sys.argv)
        if len(sys.argv) != 2:
            print(f"Usage: ./lox [script]")
            sys.exit(64)  # see `sysexits.h`
        elif sys.argv[1] != "":
            Lox.runFile(sys.argv[1])
        else:
            Lox.runPrompt()

    @staticmethod
    def runFile(file_path: str) -> None:
        with open(file_path, "r") as file:
            Lox.run(file)

    @staticmethod
    def runPrompt() -> None:
        while True:
            try:
                line: str = input("> ")
                Lox.run(line)
            except (KeyboardInterrupt, EOFError):
                break

    @staticmethod
    def run(source: str) -> None:
        scanner = Scanner(source)
        tokens = scanner.scanTokens()

        for token in tokens:
            print(token)


if __name__ == "__main__":
    Lox.main()
