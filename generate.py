import os
import shutil
import subprocess
from tools.cwcheatio import CwCheatIO

VERSION = "v1.1"

original_file_dir = "files"
asm_src_dir = "source"
build_dir = "build"
armips = os.path.join("tools", "armips.exe")


def setASMOffset(asm, offset):
    asm_path = os.path.join(asm_src_dir, asm+".asm")
    
    with open(asm_path, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
        
    for i, line in enumerate(lines):
        if ".createfile" in line:
            lines[i] = f'.createfile "./{build_dir}/{asm}.bin", {hex(offset)}\n'
        
    with open(asm_path, "w", encoding="utf-8") as fp:
        fp.writelines(lines)
 
def buildASM(asm, offset):
    print("Compiling ASM...")
    
    
    setASMOffset(asm, offset)
    
    subprocess.run(
        [armips, os.path.join(asm_src_dir, asm+".asm")],
        check=True
    )
 
def writeHook(name, data_bin_offset, data_bin):
    path = os.path.join(build_dir, name, "DATA.BIN")
    shutil.copyfile(os.path.join(original_file_dir, data_bin), path)
    print("Writing to DATA.BIN...")
    with open(path, "r+b") as fp:
        fp.seek(data_bin_offset)
        fp.write(0x0A23035B.to_bytes(4, byteorder="little"))
        fp.seek(data_bin_offset+4)
        fp.write(0x00000000.to_bytes(4, byteorder="little"))
    
def writeEBOOT(name, asm, eboot_bin):
    path = os.path.join(build_dir, name, "EBOOT.BIN")
    shutil.copyfile(os.path.join(original_file_dir, eboot_bin), path)
    print("Writing to EBOOT.BIN...")
    with open(os.path.join(build_dir, asm+".bin"), "rb") as src:
        data = src.read()
    with open(path, "r+b") as fp:
        fp.seek(0xBDB00)
        fp.write(data)
        
def generateCheat(name, v):
    print("Generating cheat file...")
    asm = os.path.join(v)
    path = os.path.join(build_dir, v+".bin")
    if v == "EventLoaderJPN":
        file = CwCheatIO(os.path.join(build_dir, name, "ULJM05066.ini"))
        file.write(f"Event Quest Loader {VERSION} [JPN]")
        file.write(f"_L 0x210ee7f8 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
        file.write(f"_L 0x210ee7fc 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
        file.seek(0x08802000)
        with open(path, "rb") as bin:
            file.write(bin.read())
        file.close()
    elif v == "EventLoaderUSA":
        file = CwCheatIO(os.path.join(build_dir, name, "ULUS10084.ini"))
        file.write(f"Event Quest Loader {VERSION} [USA]")
        file.write(f"_L 0xE0020005 0x01141182\n")
        file.write(f"_L 0xE0010020 0x00238f9C\n")
        file.write(f"_L 0x01141182 0x00000006\n")
        file.write(f"_L 0x210ef140 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
        file.write(f"_L 0x210ef144 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
        file.seek(0x08802000)
        with open(path, "rb") as bin:
            file.write(bin.read())
        file.close()
    elif v == "EventLoaderEUR":
        file = CwCheatIO(os.path.join(build_dir, name, "ULES00318.ini"))
        file.write(f"Event Quest Loader {VERSION} [EUR]")
        file.write(f"_L 0xE0020005 0x01142102\n")
        file.write(f"_L 0xE0010020 0x00239C5C\n")
        file.write(f"_L 0x01142102 0x00000006\n")
        file.write(f"_L 0x210f0110 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
        file.write(f"_L 0x210f0114 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
        file.seek(0x08802000)
        with open(path, "rb") as bin:
            file.write(bin.read())
        file.close()
    
def generate(name, v, off, db, eb):
    path = os.path.join(build_dir, name)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)
    buildASM(v, 0x088C0D6C)
    writeHook(name, off, db)
    writeEBOOT(name, v, eb)
    buildASM(v, 0x08802000)
    generateCheat(name, v)
    print("\nDone!")
        
if __name__ == "__main__":
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)
    generate("JPN", "EventLoaderJPN", 0x1A6AA0F8, "DATA_JPN.BIN", "EBOOT_JPN.BIN")
    generate("JPN_Enhanced", "EventLoaderJPN", 0x1A6AA0F8, "DATA_JPN_ENHANCED.BIN", "EBOOT_JPN_ENHANCED.BIN")
