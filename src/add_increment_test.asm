ld a, #0    ;load 0 into register a
ld b, a     ;load the value of register a into b
ld b, $0F   ;load 15 into register b

inc b       ;increment register b by 1
inc b       ;increment register b by 1

add a, #10  ;add 10 to register a
add a, b    ;add register b to register a

loop:
    inc b       ;increment register b by 1
    dec a       ;decrement a by one
    jp nz, loop ;jump to loop if a is not zero
ret ;exit program, b should be 44