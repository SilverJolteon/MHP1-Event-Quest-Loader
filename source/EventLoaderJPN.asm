.psp

sceIoOpen	equ	0x088AF800
sceIoLseek	equ	0x088AF7C8
sceIoRead	equ	0x088AF7B0
sceIoClose	equ	0x088AF7F8
sceKernelDcacheWritebackInvalidateAll	equ	0x088AF9FC

SLOT_1		equ	0x094F31E0
SLOT_SIZE	equ	0x6800

.createfile "./build/EventLoader.bin", 0x08802000 ; Free Memory
	; Backup registers v0 and s0
	addiu	sp, sp, -8
	sw		s0, 0x4(sp)
	sw		v0, 0x0(sp)
	
	; Open quests file
	la		a0, QUESTS_BIN
	li		a1, 0x1
	jal		sceIoOpen
	li		a2, 0x0
	; Check if file exists
	li		v1, 0x80010002
	beq		v0, v1, NoFile ; Return - no event quests found
	nop
	li 		v1, 0x0
	move	s0, v0	
	; Correct offset to load quest
	lw		a2, 0x0(sp)
	li		t0, SLOT_1
	sub	a2, a2, t0
	li		t0, 0x6810
	div	a2, t0
	mflo	a2
	li		t0, 0x6800
	mult	a2, t0
	mflo	a2
	; Seek to offset in file
	move 	a0, s0 ; fd
	li		a1, 0x0 ; whence
	li		a3, 0x0
	jal		sceIoLseek
	li		t0, 0x0
	; Read from offset into quest slot
	move	a0, s0
	li		a1, SLOT_1
	jal		sceIoRead
	li		a2, SLOT_SIZE
	; Close quests file
	jal		sceIoClose
	move 	a0, s0
	jal		sceKernelDcacheWritebackInvalidateAll
    nop
	; Restore registers backup and return
	jal		Restore
	nop
	j		0x098EE80C ; Jump back
	sw		v0, 0x7C(s0)
	
	Restore:
		; Restore s0 and set v0 to Quest Slot 1
		li		v0, SLOT_1
		lw		s0, 0x4(sp)
		addiu	sp, sp, 8
		jr		ra
		nop
	
	NoFile:
		jal		Restore
		nop
		j		0x098EE800;
		nop
	
	QUESTS_BIN:
		.ascii "ms0:/PSP/SAVEDATA/ULJM05066QST/MHPSP.bin"
		.align 0x4
.close