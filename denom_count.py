#!/usr/bin/env python
counts = []
denominations = raw_input("Enter denominations, separated by commas: ")
denominations = [int(d) for d in denominations.split(',')]
for denom in denominations:
    count = int(raw_input("$%s x " % denom)) or 0
    counts.append(count * denom)
    print "$%s x %s = %s" % (denom, count, denom * count)
print "TOTAL $%s" % sum(counts)
