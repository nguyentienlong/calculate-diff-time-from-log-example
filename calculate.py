#!/usr/env/bash python
import io
from sys import argv
from datetime import datetime

def main(fname):
    with open(fname, 'rb') as fh:
        first = next(fh)
        offs = -100
        while True:
            fh.seek(offs, 2)
            lines = fh.readlines()
            if len(lines)>1:
                last = lines[-1]
                break
            offs *= 2

        first_date_time = datetime.strptime(first.decode().rstrip(), '%Y-%m-%d %H:%M:%S')
        last_date_time = datetime.strptime(last.decode().rstrip(), '%Y-%m-%d %H:%M:%S')
        print(last_date_time - first_date_time)

if __name__ == '__main__':
    try:
        fname = argv[1]
    except IndexError as e:
        raise e

    main(fname)
