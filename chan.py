import sys
from typing import List, Optional


class StdIn:
    readln = input


class StdOut:
    println = print


class IO:
    stdin = StdIn
    stdout = StdOut


class Read:
    @staticmethod
    def from_file(filepath: str) -> str:
        with open(filepath) as file:
            return file.read()

class Write:
    @staticmethod
    def to_file(filepath: str, data: str):
        with open(filepath, 'w') as file:
            file.write(data)


class FileSystem:
    read = Read
    write = Write


class Args:
    all: List[str] = sys.argv

    @staticmethod
    def at(idx: int) -> Optional[str]:
        return Args.all[idx] if 0 <= idx < len(Args.all) else None


class OS:
    io = IO
    fs = FileSystem
    args = Args
