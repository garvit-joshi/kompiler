# Copyright (c) 2021 Garvit Joshi <garvitjoshi9@gmail.com>


# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


VERSION_NO = "0.7.0"

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
