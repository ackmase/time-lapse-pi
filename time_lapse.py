import datetime
import os
import sys
import time


DEFAULT_INTERVAL_IN_SECONDS = 30
DEFAULT_DIRECTORY = '/home/pi/time_lapse/pictures'
SECONDS_IN_AN_HOUR = 3600


def SnapPicture(directory=DEFAULT_DIRECTORY):
  """Snap a picture and save it in the directory using the current timestamp as filename.
  
  Args:
    directory: string, Directory to save image to. Note that the directory must exist."""
  now = str(datetime.datetime.now()).replace(' ', '-').replace('.', '-')
  file_path = os.path.join(directory, '%s.jpg' % now)
  response = os.popen('fswebcam -r 1280x720 --no-banner %s' % file_path)

  
def main():
  if len(sys.argv) != 3:
    print 'usage: python time_lapse.py interval_in_seconds /path/to/picture/directory'
  else:
    interval = float(sys.argv[1])
    directory = sys.argv[2]
    for unused_index in range(int(SECONDS_IN_AN_HOUR / interval)):
      SnapPicture(directory=directory)
      time.sleep(interval)


if __name__ == '__main__':
  main()
