#!/usr/bin/env python3

import sys
import re

module_re = re.compile(r'\w+?(?=\.\w+)+')

def get_module(s):
    search = re.search(module_re,s)
    return search.group() if search else None

def main():
    instructions = sys.argv[1].split(';')
    modules = list(map(get_module,instructions))

    globs = {}
    for module in modules:
        globs[module] = __import__(module)

    instructions[-1] = 'print({})'.format(instructions[-1])
    src = ';'.join(instructions)
    cmd = compile(src,'cmd','exec')
    exec(cmd,globs)

if __name__ == '__main__':
    main()