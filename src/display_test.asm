ld hl, $0000        ; Using HL as the memory pointer, initialize to 0
ld a, #255          ; Using a for the draw loop, 255 will fill up the screen
ld b, #0            ; Register B, used for selecting color

draw:
    ld [hl], b      ; Load the value inside register B into the mem address HL
    inc hl          ; Increment register HL by one
    inc b           ; Increment register B (next color)
    dec a           ; Decrement register A by one
    jp nz, draw     ; Jump to draw if register A is not zero

end:
    ret             ; Program is finished
