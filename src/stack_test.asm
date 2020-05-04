ld b, #62 ; Store 62 inside register B
call subtract_b_by_12
ld a, $FE
jp end

subtract_b_by_12:
    ; Input and output on B, Destroys any existing data inside register A
    ld a, b
    sub #12
    ld b, a
    ret

end:
    NOP ; register B should be 50, register A should be 254