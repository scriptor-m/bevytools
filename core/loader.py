import itertools
import threading
import time
import sys


done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


class Loader:
    def __init__(self) -> None:
        global done
        done = False
    
    def start(self):
        self.t = threading.Thread(target=animate)
        self.t.start()
    
    def stop(self):
        global done
        done = True

    