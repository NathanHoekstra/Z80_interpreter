ld b, #62               ; Store 62 inside register B
call subtract_b_by_12   ; Branch to substract_b_by_12
call push_pop           ; Branch to push_pop
add a, #20              ; Add the value 20 to the value inside register A
jp end                  ; Jump to end

subtract_b_by_12:   ; Input and output on B, Destroys any existing data inside register A
    ld a, b         ; Load the value inside register B into register A
    sub #12         ; Substract 12 from the value inside register A
    ld b, a         ; Load the value inside register A into register B
    ret             ; Return

push_pop:
    ld bc, $AABB    ; Load 43707 inside register BC
    push bc         ; Push the value inside register BC onto the stack
    pop de          ; Pop a value from the stack into register DE
    ret             ; Return, both BC and DE should contain 43707

end:
    ret             ; Register B should be 50, register A should be 70