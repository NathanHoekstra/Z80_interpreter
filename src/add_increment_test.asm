ld a, #0    ;load 0 into register a
ld b, $0F   ;load 15 into register b
inc b       ;increment register b by 1
inc b       ;increment register b by 1
add a, #10  ;add 10 to register a
add a, b    ;add register b to register a
loop:
    add a, #1 ;add 1 to register a
    djnz loop ;loop if b is not zero
ret ;exit program