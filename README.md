# ZTE ZXHN H298N

## jazztel 1.5

```
$ binwalk -E -N zxhnh298n_hv15_fv114_jazzt15_firmware.bin

DECIMAL       HEXADECIMAL     ENTROPY
--------------------------------------------------------------------------------
0             0x0             Rising entropy edge (0.985458)
1826816       0x1BE000        Falling entropy edge (0.000000)
4194304       0x400000        Rising entropy edge (0.976179)
8803328       0x865400        Falling entropy edge (0.387252)

$ dd if=zxhnh298n_hv15_fv114_jazzt15_firmware.bin of=squash.img bs=4194560 skip=1
$ unsquashfs -d zxhnh298n_hv15_fv114_jazzt15_firmware firmware.bin
```
