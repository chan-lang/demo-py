from chan import *
from typing import Optional, Any, Type as Chan


"""
The `main` function must be able to perform any side
effects that a program might want to perform. Therefore, we
pass to it the OS channel: the omnipotent power to do
whatever we wish.

When the `main` function calls other functions to delegate
some of its duties, it shares only a tiny bit of its great
power -- precisely as much as needed to perform the action.
Pure functions don't need any permissions at all! Just the
arguments, please!
"""
def main(os: Chan[OS]):
    name: str = some_or(get_name(os.args), "Anon")
    message: str = "Hello, " + name
    display(os.io.stdout, message)
    record(os.fs.write, message)


"""
Pure functions like `some_or` don't take any channels,
they only work with their explicit arguments.
"""
def some_or(value: Any, default: Any) -> Any:
    return default if value is None else value


"""
Impure function can only perform side-effects supported by
the channel you pass to it. This way, channels serve as a
natural permissions system.
"""
def get_name(args: Chan[Args]) -> Optional[str]:
    # Name may be passed as a command-line argument.
    return args.at(1)


"""
For example, this `display` function can only print to the
console through the `StdOut` chanel we gave it. It is very
easy to asses what a function is doing just by looking at
its signature.
"""
def display(stdout: Chan[StdOut], data: str):
    stdout.println(data)


def record(write: Chan[Write], data: str):
    write.to_file("message.txt", data)


"""
This initialisation logic is only necessary in Python. In a
true Permission-driven programming language, the `main`
function is assumed to have access to the OS channel.
"""
if __name__ == '__main__':
    main(OS)
