import sys
from scanner import Scanner
from token import Token
import aux


class Lox:
    hadError: bool = False

    @staticmethod
    def main():
        if len(sys.argv) > 2:
            print(f"Usage: ./lox [script]")
            sys.exit(64)  # see `sysexits.h`
        elif len(sys.argv) == 2:
            Lox.runFile(sys.argv[1])
        else:
            Lox.runPrompt()

    @staticmethod
    def runFile(file_path: str) -> None:
        with open(file_path, "r") as file:
            Lox.run(file)
        if Lox.hadError:
            sys.exit(65)

    @staticmethod
    def runPrompt() -> None:
        while True:
            try:
                line: str = input("> ")
                Lox.run(line)
                Lox.hadError = False
            except (KeyboardInterrupt, EOFError):
                break

    @staticmethod
    def run(source: str) -> None:
        scanner = Scanner(source)
        tokens = scanner.scanTokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str) -> None:
        Lox.report(line, "", message)

    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        aux.print_to_stderr(f"[line {line}] Error{where}: {message}")
