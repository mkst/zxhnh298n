# ZTE ZXHN H298N

## jazztel 1.5

```
$ binwalk -N zxhnh298n_hv15_fv114_jazzt15_firmware.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
276           0x114           LZMA compressed data, properties: 0x5D, dictionary size: 33554432 bytes, uncompressed size: 5947376 bytes
4194560       0x400100        Squashfs filesystem, little endian, version 4.0, compression:lzma, size: 4609744 bytes, 929 inodes, blocksize: 131072 bytes, created: 2013-10-18 10:07:32

$ dd if=zxhnh298n_hv15_fv114_jazzt15_firmware.bin of=squash.img bs=4194560 skip=1
$ unsquashfs -d zxhnh298n_hv15_fv114_jazzt15_firmware firmware.bin
```
