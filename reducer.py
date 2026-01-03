#!/usr/bin/env python3
import sys

current_key = None
sum_days = sum_rain = sum_temp = sum_yld = 0.0
count = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    key, values = line.split("\t", 1)

    try:
        days, rain, temp, yld, c = map(float, values.split(","))
    except:
        continue

    if current_key is None:
        current_key = key

    if key != current_key:
        # output result for previous key
        print(f"{current_key}\t{count},{sum_days},{sum_rain},{sum_temp},{sum_yld}")
        current_key = key
        sum_days = sum_rain = sum_temp = sum_yld = 0.0
        count = 0.0

    sum_days += days
    sum_rain += rain
    sum_temp += temp
    sum_yld  += yld
    count += c

# last key
if current_key is not None:
    print(f"{current_key}\t{count},{sum_days},{sum_rain},{sum_temp},{sum_yld}")
