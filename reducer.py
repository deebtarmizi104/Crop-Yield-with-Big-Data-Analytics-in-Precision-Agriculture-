#!/usr/bin/env python3
import sys

current_region = None
sum_days = sum_rain = sum_temp = sum_yld = 0.0
count = 0

def emit(region, count, sd, sr, st, sy):
    if count == 0:
        return
    print(f"{region}\t{sd/count:.6f}\t{sr/count:.6f}\t{st/count:.6f}\t{sy/count:.6f}")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    region, values = line.split("\t", 1)

    try:
        days, rain, temp, yld, c = values.split(",")
        days = float(days); rain = float(rain); temp = float(temp); yld = float(yld); c = int(float(c))
    except:
        continue

    if current_region is None:
        current_region = region

    if region != current_region:
        emit(current_region, count, sum_days, sum_rain, sum_temp, sum_yld)
        current_region = region
        sum_days = sum_rain = sum_temp = sum_yld = 0.0
        count = 0

    sum_days += days
    sum_rain += rain
    sum_temp += temp
    sum_yld  += yld
    count += c

if current_region is not None:
    emit(current_region, count, sum_days, sum_rain, sum_temp, sum_yld)
