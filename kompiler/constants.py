VERSION_NO = "0.5.0"

VERSION = "Kompiler: v"+VERSION_NO

ABOUT = """
Kompiler: A package for auto compiling C++ files as soon as they are saved.\n
Source Code: https://github.com/garvit-joshi/kompiler/
pip: https://pypi.org/project/kompiler/
Made by Garvit Joshi https://github.com/garvit-joshi
"""

HELP = """
Usage: kompiler [File.cpp] [COMMAND...]
eg:
    ❯ kompiler hello.cpp
        Command used for compiling: g++ hello.cpp\n
    ❯ kompiler hello.cpp -std=c++11 -O2 -Wall hello.cpp -o hello
        Command used for compiling: g++ -std=c++11 -O2 -Wall hello.cpp -o hello\n
    ❯ kompiler 3.cpp -std=c++11 -O2 -Wall 3.cpp -o hello "&&" ./hello
        Command used for compiling: g++ -std=c++11 -O2 -Wall 3.cpp -o hello && ./hello\n
"""
