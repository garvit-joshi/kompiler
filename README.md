# Kompiler
A package for auto compiling C++ files as soon as they are saved.

```
Usage: kompiler [File.cpp] [COMMAND...]
eg:
    ❯ kompiler hello.cpp
        Command used for compiling: g++ hello.cpp
    ❯ kompiler hello.cpp -std=c++11 -O2 -Wall hello.cpp -o hello
        Command used for compiling: g++ -std=c++11 -O2 -Wall hello.cpp -o hello
    ❯ kompiler 3.cpp -std=c++11 -O2 -Wall 3.cpp -o hello "&&" ./hello
        Command used for compiling: g++ -std=c++11 -O2 -Wall 3.cpp -o hello && ./hello
```