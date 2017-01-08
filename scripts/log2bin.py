from sys import argv, stdout

# mark@carbon:~/Documents$ head bootloader.log 
# <RTL867X>d 0x80000000 3209000
# 0x80000000: 10 00 00 FF 00 00 00 00 10 00 01 05 00 00 00 00 ................
# 0x80000010: 00 00 00 00 00 00 00 00 10 00 FF F9 00 00 00 00 ................
# 0x80000020: 10 00 FF F7 00 00 00 00 10 00 FF F5 00 00 00 00 ................

cols_per_line = 16

if len(argv) != 2:
  print "usage:\n  python", argv[0], "<log_file>"
  exit()

with open (argv[1]) as log:
  for line in log:
    if line.startswith("0x"):
      l = line.split(" ")
      h = ""
      for i in range (1, 1 + cols_per_line):
        h += chr(int(l[i], 16))
      stdout.write(h)
