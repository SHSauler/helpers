#!/usr/bin/env python3

import sys
from time import sleep

def progress_bar(progress, total, bar_length=75, padding=".", fill="#" ):

    progress_percent = int((progress / total) * 100)
    num_progress_fill = int((bar_length * progress_percent) / 100)
    progress_fill = num_progress_fill * fill
    remaining_fill = (bar_length - num_progress_fill) * padding
    
    sys.stdout.write("\r [{0}{1}] {2}%".format(progress_fill, 
                                               remaining_fill, 
                                               progress_percent))
    sys.stdout.flush()

for i in range(100):
    progress_bar(i, 100)
    sleep(0.3)

