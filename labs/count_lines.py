import sys

if 1 == len(sys.argv):
    print('Usage: %s <filename>' % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1]) as fp:
    count = 0
    for line in fp:
        count = 1 + count

print('%d' % count)
