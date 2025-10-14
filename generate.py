import os
import shutil
import subprocess
from tools.cwcheatio import CwCheatIO

original_file_dir = "files"
asm_src_dir = "source"
build_dir = "build"
armips = os.path.join("tools", "armips.exe")
umd_replace = os.path.join("tools", "UMD-replace.exe")
xdelta = os.path.join("tools", "xdelta.exe")

def writefp(fp, offset, value):
    fp.seek(offset)
    fp.write(value.to_bytes(4, byteorder="little"))

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
 
def writeHook(name, v, data_bin):
    path = os.path.join(build_dir, name, "DATA.BIN")
    shutil.copyfile(os.path.join(original_file_dir, data_bin), path)
    print("Writing to DATA.BIN...")
    with open(path, "r+b") as fp:
        if(v == "EventLoaderJPN"):
            offset = 0x195BB900
            writefp(fp, 0x10EE7f8+offset, 0x0A230857)
            writefp(fp, 0x10EE7fC+offset, 0x00000000)
        elif(v == "EventLoaderUSA"):
            offset = 0x19155880
            
            writefp(fp, 0x10EE7F4+offset, 0x24460002)
            
            writefp(fp, 0x11331D0+offset, 0x00280198)
            writefp(fp, 0x11331E8+offset, 0x00100100)
            writefp(fp, 0x11331F4+offset, 0x00080110)
            writefp(fp, 0x1133200+offset, 0x00090118)
            writefp(fp, 0x113320C+offset, 0x00190118)
            writefp(fp, 0x1133218+offset, 0x00190198)
            writefp(fp, 0x1133224+offset, 0x00C40118)
            writefp(fp, 0x1133230+offset, 0x00200100)
            writefp(fp, 0x113323C+offset, 0x00180110)
            writefp(fp, 0x1133248+offset, 0x00190118)
            writefp(fp, 0x1133254+offset, 0x00290118)
            writefp(fp, 0x1133260+offset, 0x00290198)
            writefp(fp, 0x113326C+offset, 0x008C0118)
            
            writefp(fp, 0x10F2414+offset, 0x0E23089f)
            writefp(fp, 0x10F2418+offset, 0x00000000)
            
            writefp(fp, 0x10ef140+offset, 0x0A230857)
            writefp(fp, 0x10ef144+offset, 0x00000000)
        elif(v == "EventLoaderEUR"):
            offset = 0x19781300
            
            writefp(fp, 0x10EF7C4+offset, 0x24460002)
            
            writefp(fp, 0x11341A8+offset, 0x00280198)
            writefp(fp, 0x11341C0+offset, 0x00100100)
            writefp(fp, 0x11341CC+offset, 0x00080110)
            writefp(fp, 0x11341D8+offset, 0x00090118)
            writefp(fp, 0x11341E4+offset, 0x00190118)
            writefp(fp, 0x11341F0+offset, 0x00190198)
            writefp(fp, 0x11341FC+offset, 0x00C40118)
            writefp(fp, 0x1134208+offset, 0x00200100)
            writefp(fp, 0x1134214+offset, 0x00180110)
            writefp(fp, 0x1134220+offset, 0x00190118)
            writefp(fp, 0x113422C+offset, 0x00290118)
            writefp(fp, 0x1134238+offset, 0x00290198)
            writefp(fp, 0x1134244+offset, 0x008C0118)
            
            writefp(fp, 0x10F33E4+offset, 0x0E23089f)
            writefp(fp, 0x10F33E8+offset, 0x00000000)
            
            writefp(fp, 0x10f0110+offset, 0x0A230857)
            writefp(fp, 0x10f0114+offset, 0x00000000)
    
def writeEBOOT(name, asm, eboot_bin):
    path = os.path.join(build_dir, name, "EBOOT.BIN")
    shutil.copyfile(os.path.join(original_file_dir, eboot_bin), path)
    print("Writing to EBOOT.BIN...")
    with open(os.path.join(build_dir, asm+".bin"), "rb") as src:
        data = src.read()
    with open(path, "r+b") as fp:
        fp.seek(0xBEEF0)
        fp.write(data)  
        
        
def generateCheat(name, v):
    print("Generating cheat file...")
    asm = os.path.join(v)
    path = os.path.join(build_dir, v+".bin")
    if v == "EventLoaderJPN":
        file = CwCheatIO(os.path.join(build_dir, name, "ULJM05066.ini"))
        file.write(f"Event Quest Loader v1.1 [JPN]")
        file.write(f"_L 0x210ee7f8 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
        file.write(f"_L 0x210ee7fc 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop  
        
        file.seek(0x08802000)
        with open(path, "rb") as bin:
            file.write(bin.read())
        file.close()
    elif v == "EventLoaderUSA":
        
        file = CwCheatIO(os.path.join(build_dir, name, "ULUS10084.ini"))
        file.write(f"Event Quest Loader v1.3 [USA]")
        
        # Allow cursor to move one more position
        file.write(f"_L 0x210EE7F4 0x24460002\n")
        
        # Shift menu options upwards
        file.write(f"_L 0x211331D0 0x00280198\n")
        file.write(f"_L 0x211331E8 0x00100100\n")
        file.write(f"_L 0x211331F4 0x00080110\n")
        file.write(f"_L 0x21133200 0x00090118\n")
        file.write(f"_L 0x2113320C 0x00190118\n")
        file.write(f"_L 0x21133218 0x00190198\n")
        file.write(f"_L 0x21133224 0x00C40118\n")
        file.write(f"_L 0x21133230 0x00200100\n")
        file.write(f"_L 0x2113323C 0x00180110\n")
        file.write(f"_L 0x21133248 0x00190118\n")
        file.write(f"_L 0x21133254 0x00290118\n")
        file.write(f"_L 0x21133260 0x00290198\n")
        file.write(f"_L 0x2113326C 0x008C0118\n")
        
        # Event Menu Hook
        file.write(f"_L 0x210F2414 0x0e200848\n")
        file.write(f"_L 0x210F2418 0x00000000\n")

        # Event Loader Hook
        file.write(f"_L 0x210ef140 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
        file.write(f"_L 0x210ef144 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
        file.seek(0x08802000)
        with open(path, "rb") as bin:
            file.write(bin.read())
        file.close()
    elif v == "EventLoaderEUR":
        file = CwCheatIO(os.path.join(build_dir, name, "ULES00318.ini"))
        file.write(f"Event Quest Loader v1.3.1 [EUR]")
        
        # Allow cursor to move one more position
        file.write(f"_L 0x210EF7C4 0x24460002\n")
        
        # Shift menu options upwards
        file.write(f"_L 0x211341A8 0x00280198\n")
        file.write(f"_L 0x211341C0 0x00100100\n")
        file.write(f"_L 0x211341CC 0x00080110\n")
        file.write(f"_L 0x211341D8 0x00090118\n")
        file.write(f"_L 0x211341E4 0x00190118\n")
        file.write(f"_L 0x211341F0 0x00190198\n")
        file.write(f"_L 0x211341FC 0x00C40118\n")
        file.write(f"_L 0x21134208 0x00200100\n")
        file.write(f"_L 0x21134214 0x00180110\n")
        file.write(f"_L 0x21134220 0x00190118\n")
        file.write(f"_L 0x2113422C 0x00290118\n")
        file.write(f"_L 0x21134238 0x00290198\n")
        file.write(f"_L 0x21134244 0x008C0118\n")
        
        # Event Menu Hook
        file.write(f"_L 0x210F33E4 0x0e200848\n")
        file.write(f"_L 0x210F33E8 0x00000000\n")
        
        file.write(f"_L 0x210f0110 0x0a200800\n") # lw v1,0x0(v0) -> j 0x08802000
        file.write(f"_L 0x210f0114 0x00000000\n") # bnel v1,zero,0x098EE80C -> nop
        file.seek(0x08802000)
        with open(path, "rb") as bin:
            file.write(bin.read())
        file.close()

def patchISO(name, v):
    print("Patching ISO...")
    path = os.path.join(build_dir, name, f"Patched_{v}.iso")
    shutil.copyfile(os.path.join(original_file_dir, v+".iso"), path)
    subprocess.run(
        [umd_replace, path, "/PSP_GAME/USRDIR/DATA.BIN", os.path.join(build_dir, name, "DATA.BIN")],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    subprocess.run(
        [umd_replace, path, "/PSP_GAME/SYSDIR/EBOOT.BIN", os.path.join(build_dir, name, "EBOOT.BIN")],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    if(name == "EventLoaderJPN (DX)"):
        icon = os.path.join(original_file_dir, "IconJPN.png")
        subprocess.run(
            [umd_replace, path, "/PSP_GAME/ICON0.PNG", icon],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )
    elif(name == "EventLoaderUSA (DX)" or name == "EventLoaderEUR (DX)"):
        icon = os.path.join(original_file_dir, "Icon.png")
        subprocess.run(
            [umd_replace, path, "/PSP_GAME/ICON0.PNG", icon],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )
    
def creatPatch(name, v):
    print("Creating Patch...")
    unmodified = os.path.join(original_file_dir, v+".iso")
    modified = os.path.join(build_dir, name, f"Patched_{v}.iso")
    patch = os.path.join(build_dir, name, f"{name}.xdelta")
    subprocess.run(
        [xdelta, "-e", "-s", unmodified, modified, patch],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    
def generate(name, v, db, eb):
    path = os.path.join(build_dir, name)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)
    buildASM(v, 0x088C215C)
    writeHook(name, v, db)
    writeEBOOT(name, v, eb)
    buildASM(v, 0x08802000)
    generateCheat(name, v)
    patchISO(name, v)
    creatPatch(name, v)
    print("\nDone!")
        
if __name__ == "__main__":
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir, exist_ok=True)
    generate("EventLoaderJPN", "EventLoaderJPN", "DATA_JPN.BIN", "EBOOT_JPN.BIN")
    generate("EventLoaderJPN (DX)", "EventLoaderJPN", "DATA_JPN_DX.BIN", "EBOOT_JPN_DX.BIN")
    generate("EventLoaderUSA", "EventLoaderUSA", "DATA_USA.BIN", "EBOOT_USA.BIN")
    generate("EventLoaderUSA (DX)", "EventLoaderUSA", "DATA_USA_DX.BIN", "EBOOT_USA_DX.BIN")
    generate("EventLoaderEUR", "EventLoaderEUR", "DATA_EUR.BIN", "EBOOT_EUR.BIN")
    generate("EventLoaderEUR (DX)", "EventLoaderEUR", "DATA_EUR_DX.BIN", "EBOOT_EUR_DX.BIN")
        