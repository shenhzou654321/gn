#!/usr/bin/env python
# Recursively formats a all *.gn, *.gni files found in a directory.
# Usage: gn-format-recursive.py <folder path> [<gn binary path>]
import sys
import os
import subprocess

GN_EXTENSIONS = ('.gn', '.gni')

def main(path, binary='gn'):
  for path, dirs, filenames in os.walk(path):
    for filename in filenames:
      if os.path.splitext(filename)[1] not in GN_EXTENSIONS:
        continue

      subprocess.check_call([binary, 'format', '--in-place', path])

if __name__ == '__main__':
  main(*sys.argv[1:])
