#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    fields = line.split(",")

    # Expect 5 columns: Region, Days, Rainfall, Temp, Yield
    if len(fields) < 5:
        continue

    try:
        region = fields[0].strip()
        days = float(fields[1])
        rain = float(fields[2])
        temp = float(fields[3])
        yld  = float(fields[4])
    except:
        continue

    print(f"{region}\t{days},{rain},{temp},{yld},1")
