#!/usr/bin/python3

import sys
import json

def main():
    for arg in sys.argv[1:]:
        with open(arg, 'r') as f:
            js = json.loads(f.read())
        with open(arg + '.txt', 'w') as f:
            last_time = None
            line_started = False
            for ev in js['events']:
                time_ms = ev['tStartMs']
                time_s, time_ms = divmod(time_ms, 1000)
                time_m, time_s = divmod(time_s, 60)
                time_h, time_m = divmod(time_m, 60)
                if 'segs' not in ev: continue
                for seg in ev['segs']:
                    text = seg['utf8']
                    if text == '\n':
                        f.write('\n')
                        line_started = False
                        continue
                    if not line_started:
                        f.write(f'{time_h}:{time_m:02}:{time_s:02} ::')
                        line_started = True
                    f.write(' ' + text.strip())
            f.write('\n')

if __name__ == '__main__':
    main()
