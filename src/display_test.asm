ld hl, $0000        ; Using HL as the memory pointer, initialize to 0
ld a, #128          ; Using a for the draw loop, 128 will fill up half the screen
ld b, #0
draw:
    ld [hl], b      ; Load the value 20 into the mem address HL
    inc hl          ; Increment register HL by one
    inc b           ; Increment register B (next color)
    dec a           ; Decrement register A by one
    jp nz, draw     ; Jump to draw if a is not zero

end:
    ret             ; Program is finished
