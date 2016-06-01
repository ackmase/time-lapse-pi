"""Ad hoc tool for cloning files.

Assumes that filenames are of the form: 2016-05-31-06:32:01-442061.???. The minutes are
incremented by 2.
"""

import os
import sys

def main():
  assert len(sys.argv) == 2, 'Usage: clone-files.py /path/to/directory/'
  
  directory = sys.argv[1]
  results = os.popen('ls %s' % directory)
  old_filenames = [row.strip('\n') for row in results]
  
  for old_filename in old_filenames:
    old_minutes = int(old_filename[14:16])
    new_minutes = old_minutes + 2
    new_filename = '%s%02d%s' % (old_filename[:14],
                                 new_minutes,
                                 old_filename[16:])
    os.popen('cp %s %s' % (old_filename, new_filename))


if __name__ == '__main__':
  main()
