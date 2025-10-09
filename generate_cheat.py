from cwcheatio import CwCheatIO

file = CwCheatIO("ULJM05066.ini")
file.write(f"Event Quest Loader v1.1 [JPN]")
file.write(f"_L 0x210ee7f8 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
file.write(f"_L 0x210ee7fc 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
file.seek(0x08802000)
with open("build/EventLoaderJPN.bin", "rb") as bin:
    file.write(bin.read())
file.close()



file = CwCheatIO("ULUS10084.ini")
file.write(f"Event Quest Loader v1.1 [USA]")
file.write(f"_L 0xE0020005 0x01141182\n")
file.write(f"_L 0xE0010020 0x00238f9C\n")
file.write(f"_L 0x01141182 0x00000006\n")
file.write(f"_L 0x210ef140 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
file.write(f"_L 0x210ef144 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
file.seek(0x08802000)
with open("build/EventLoaderUSA.bin", "rb") as bin:
    file.write(bin.read())
file.close()



file = CwCheatIO("ULES00318.ini")
file.write(f"Event Quest Loader v1.1 [EUR]")
file.write(f"_L 0xE0020005 0x01142102\n")
file.write(f"_L 0xE0010020 0x00239C5C\n")
file.write(f"_L 0x01142102 0x00000006\n")
file.write(f"_L 0x210f0110 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
file.write(f"_L 0x210f0114 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
file.seek(0x08802000)
with open("build/EventLoaderEUR.bin", "rb") as bin:
    file.write(bin.read())
file.close()