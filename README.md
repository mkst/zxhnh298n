# ZTE ZXHN H298N

## jazztel 1.5

```
$ binwalk -N firmware/zxhnh298n_hv15_fv114_jazzt15_firmware.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
276           0x114           LZMA compressed data, properties: 0x5D, dictionary size: 33554432 bytes, uncompressed size: 5947376 bytes
4194560       0x400100        Squashfs filesystem, little endian, version 4.0, compression:lzma, size: 4609744 bytes, 929 inodes, blocksize: 131072 bytes, created: 2013-10-18 10:07:32

$ dd if=firmware/zxhnh298n_hv15_fv114_jazzt15_firmware.bin of=squash.img bs=4194560 skip=1
$ unsquashfs -d zxhnh298n_hv15_fv114_jazzt15_firmware squash.img

$ dd if=firmware/zxhnh298n_hv15_fv114_jazzt15_firmware.bin of=header.dmp bs=276 count=1
$ xxd header.dmp
00000000: 9999 9999 4444 4444 5555 5555 aaaa aaaa  ....DDDDUUUU....
00000010: 0000 0000 0000 0000 0000 0000 0000 0230  ...............0
00000020: 0000 0003 5631 2e31 2e34 5f4a 415a 5a00  ....V1.1.4_JAZZ.
00000030: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000040: 0001 0000 0000 0000 003f ffec 0000 0100  .........?......
00000050: 287d 10d6 0046 6000 0040 0000 e93a 94b6  (}...F`..@...:..
00000060: 0140 0000 0040 0000 0180 0000 0060 0000  .@...@.......`..
00000070: 03c0 0000 0040 0000 0400 0000 0060 0000  .....@.......`..
00000080: 5448 4953 2049 5320 4832 3938 4e20 5645  THIS IS H298N VE
00000090: 5253 494f 4e00 0000 0000 0000 0000 0009  RSION...........
000000a0: 0500 0000 0000 0000 0000 0000 0000 0000  ................
000000b0: 0000 0009 0000 0000 3423 c258 3230 3133  ........4#.X2013
000000c0: 3130 3138 3138 3037 3434 0000 0000 0000  1018180744......
000000d0: 0000 0000 ffff ffff 0000 0000 0000 0000  ................
000000e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000100: 3333 3333 6666 6666 9999 9999 cccc cccc  3333ffff........
00000110: 0000 0000                                ....

$ dd if=firmware/zxhnh298n_hv15_fv114_jazzt15_firmware.bin of=lzma.dmp bs=276 skip=1 && truncate -s 4194284 lzma.dmp
$ 7za x lzma.dmp
$ binwalk -N lzma
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
148401        0x243B1         Cisco IOS microcode, for "0B"
2610081       0x27D3A1        Cisco IOS microcode, for ",f"
4030496       0x3D8020        Linux kernel version "2.6.30.9 (xia@njzd) (gcc version 4.4.6 (Realtek RSDK-1.5.6p2) ) #2 Fri Oct 18 18:07:21 CST 2013"
4083856       0x3E5090        CRC32 polynomial table, little endian
4294313       0x4186A9        Unix path: /tmp/CN_VoIP/cvsroot/VoIP-rtl865x/linux-2.4.18/rtk_voip/voip_dsp/dsp_r1/t38/mdm_src/r2x_baud.c,v 1.3 2008-01-15 06:33:22 kennyli
4296377       0x418EB9        Unix path: /tmp/CN_VoIP/cvsroot/VoIP-rtl865x/linux-2.4.18/rtk_voip/voip_dsp/dsp_r1/t38/mdm_src/r2x_scm.c,v 1.3 2008-01-15 06:33:23 kennylin
4302169       0x41A559        Unix path: /tmp/CN_VoIP/cvsroot/VoIP-rtl865x/linux-2.4.18/rtk_voip/voip_dsp/dsp_r1/t38/mdm_src/r17_cor.c,v 1.3 2008-01-15 06:33:22 kennylin
4303305       0x41A9C9        Unix path: /tmp/CN_VoIP/cvsroot/VoIP-rtl865x/linux-2.4.18/rtk_voip/voip_dsp/dsp_r1/t38/mdm_src/r21_cor.c,v 1.3 2008-01-15 06:33:22 kennylin
4303497       0x41AA89        Unix path: /tmp/CN_VoIP/cvsroot/VoIP-rtl865x/linux-2.4.18/rtk_voip/voip_dsp/dsp_r1/t38/mdm_src/t21_cor.c,v 1.3 2008-01-15 06:33:23 kennylin
4304057       0x41ACB9        Unix path: /tmp/CN_VoIP/cvsroot/VoIP-rtl865x/linux-2.4.18/rtk_voip/voip_dsp/dsp_r1/t38/mdm_src/mdm_fltr.c,v 1.3 2008-01-15 06:33:22 kennyli
4307625       0x41BAA9        MySQL MISAM index file Version 6
4307644       0x41BABC        MySQL ISAM compressed data file Version 6
4717671       0x47FC67        Unix path: /100_half/10_full/100_full/1000_full/auto"
4727175       0x482187        Unix path: /net/rtl819x/rtl865x/../AsicDriver/rtl865x_asicBasic.c
4730892       0x48300C        Unix path: /trap/normal/clean_L2/clean_L3)
4843860       0x49E954        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/core/request_sock.c
4844320       0x49EB20        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/core/datagram.c
4845144       0x49EE58        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/core/dev.c
4846296       0x49F2D8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/include/linux/CSPCommon.h
4848660       0x49FC14        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/core/fib_rules.c
4848968       0x49FD48        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/sched/sch_generic.c
4849356       0x49FECC        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/sched/act_api.c
4849620       0x49FFD4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/sched/act_police.c
4849732       0x4A0044        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/sched/sch_wfq.c
4850116       0x4A01C4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/sched/cls_u32.c
4850376       0x4A02C8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netlink/af_netlink.c
4854196       0x4A11B4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netfilter/nf_conntrack_h323_main.c
4854628       0x4A1364        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netfilter/nf_conntrack_ftp.c
4854928       0x4A1490        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netfilter/nf_conntrack_pt.c
4856036       0x4A18E4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netfilter/nf_conntrack_pptp.c
4856280       0x4A19D8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netfilter/nf_conntrack_sip.c
4857668       0x4A1F44        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netfilter/nf_conntrack_tftp.c
4858068       0x4A20D4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/netfilter/nf_conntrack_rtsp.c
4860556       0x4A2A8C        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/route.c
4861048       0x4A2C78        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/ip_input.c
4861484       0x4A2E2C        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/ip_output.c
4861636       0x4A2EC4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/inet_hashtables.c
4862504       0x4A3228        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/tcp.c
4862900       0x4A33B4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/tcp_input.c
4863680       0x4A36C0        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/tcp_timer.c
4864356       0x4A3964        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/tcp_ipv4.c
4865304       0x4A3D18        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/icmp.c
4865604       0x4A3E44        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/devinet.c
4866236       0x4A40BC        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/af_inet.c
4867132       0x4A443C        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/igmp.c
4868504       0x4A4998        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/fib_frontend.c
4868866       0x4A4B02        Unix path: /proc/net/arpdefend/interval fail!
4868934       0x4A4B46        Unix path: /proc/net/arpdefend/agetime fail!
4872292       0x4A5864        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/netfilter/nf_nat_helper.c
4873040       0x4A5B50        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/netfilter/nf_nat_rtsp.c
4875728       0x4A65D0        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/netfilter/nf_nat_sip.c
4877012       0x4A6AD4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/netfilter/ipt_psd.c
4877528       0x4A6CD8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/netfilter/ipt_logext.c
4878520       0x4A70B8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv4/netinfo.c
4878774       0x4A71B6        Unix path: /proc/net/netinfo/wlan_sta_disconnect fail!
4878902       0x4A7236        Unix path: /proc/net/netinfo/size fail!
4878954       0x4A726A        Unix path: /proc/net/netinfo/max_size fail!
4880732       0x4A795C        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/unix/af_unix.c
4880948       0x4A7A34        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/af_inet6.c
4881168       0x4A7B10        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/ip6_output.c
4882784       0x4A8160        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/ip6_fib.c
4883756       0x4A852C        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/ndisc.c
4884980       0x4A89F4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/reassembly.c
4885388       0x4A8B8C        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/tcp_ipv6.c
4886739       0x4A90D3        Neighborly text, "NeighborSolicitsts"
4886763       0x4A90EB        Neighborly text, "NeighborAdvertisementsmp6OutDestUnreachs"
4886964       0x4A91B4        Neighborly text, "NeighborSolicitsirects"
4886992       0x4A91D0        Neighborly text, "NeighborAdvertisementssponses"
4887412       0x4A9374        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/inet6_connection_sock.c
4888848       0x4A9910        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/netfilter/nf_conntrack_reasm.c
4889800       0x4A9CC8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ipv6/inet6_hashtables.c
4889988       0x4A9D84        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/packet/af_packet.c
4890676       0x4AA034        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/bridge/br_if.c
4891235       0x4AA263        Neighborly text, "neighbor %.2x%.2x.%.2x:%.2x:%.2x:%.2x:%.2x:%.2x lost on port %d(%s)(%s)"
4891496       0x4AA368        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/bridge/br_hook.c
4895560       0x4AB348        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ppp/ppp_generic.c
4897108       0x4AB954        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/ppp/pppoe.c
4898360       0x4ABE38        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../drivers/source/ledkey_mod.c
4900756       0x4AC794        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../drivers/source/ver_info.c
4901576       0x4ACAC8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../drivers/source/csp_ifinfo.c
4901956       0x4ACC44        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../drivers/source/sweth_core.c
4925672       0x4B28E8        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../common/source/oss_logctl.c
4926728       0x4B2D08        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../common/source/monitor.c
4927584       0x4B3060        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../common/source/cspmirror.c
4932216       0x4B4278        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../common/source/oss_logfile.c
4937708       0x4B57EC        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../common/source/oss_logstdio.c
4939168       0x4B5DA0        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/wb_main.c
4939912       0x4B6088        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/wb_config.c
4945156       0x4B7504        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/br_mc_mac.c
4945692       0x4B771C        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/br_mld.c
4948172       0x4B80CC        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/br_mld_mac.c
4948616       0x4B8288        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/qos.c
4953270       0x4B94B6        Unix path: /proc/net/fastforward/bridge_learn_power fail!
4953378       0x4B9522        Unix path: /proc/net/fastforward/route_learn_power fail!
4953428       0x4B9554        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/ff_api.c
4953818       0x4B96DA        Unix path: /proc/net/mcfastforward/mcff_l2_learn_power fail!
4953914       0x4B973A        Unix path: /proc/net/mcfastforward/mcff_l3_learn_power fail!
4953968       0x4B9770        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/mc_fast_api.c
4954648       0x4B9A18        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/rtl_ff_api.c
4959748       0x4BAE04        Unix path: /home/xia/Builds/H298N_V1.1_Dev/csp/cspkernel/linux/net/../../protocol/source/ffe_core.c
4960194       0x4BAFC2        Unix path: /proc/net/fastforward/route_entry_clear fail!
4960278       0x4BB016        Unix path: /proc/net/fastforward/ffe_status fail!
4960342       0x4BB056        Unix path: /proc/net/fastforward/max_size fail!
4960410       0x4BB09A        Unix path: /proc/net/fastforward/fap_pps fail!
4960932       0x4BB2A4        Unix path: /home/xia/Builds/H298N_V1.1_Dev/chip_h298n_8676/product/h298nv1.1.4_JAZZTEL/scripts/../code/cspkernel/source/conf_ifinfo.c
4961568       0x4BB520        Unix path: /home/xia/Builds/H298N_V1.1_Dev/chip_h298n_8676/product/h298nv1.1.4_JAZZTEL/scripts/../code/cspkernel/source/mtd_adapter.c
5305081       0x50F2F9        Unix path: /tmp/CN_VoIP/cvsroot/VoIP-rtl865x/linux-2.4.18/rtk_voip/voip_dsp/dsp_r1/t38/mdm_src/r2x_dcd.c,v 1.3 2008-01-15 06:33:22 kennylin
5538797       0x5483ED        LZMA compressed data, properties: 0x90, dictionary size: 16777216 bytes, uncompressed size: 49665 bytes
5548547       0x54AA03        LZMA compressed data, properties: 0x64, dictionary size: 16777216 bytes, uncompressed size: 57345 bytes
5549197       0x54AC8D        LZMA compressed data, properties: 0x64, dictionary size: 16777216 bytes, uncompressed size: 57345 bytes
5699891       0x56F933        LZMA compressed data, properties: 0xC0, dictionary size: 16777216 bytes, uncompressed size: 1660800 bytes
5704938       0x570CEA        LZMA compressed data, properties: 0xD0, dictionary size: 65536 bytes, uncompressed size: 65792 bytes
```
