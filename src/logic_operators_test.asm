ld a, %1010 ; Load 10 inside register A
and %1101   ; perform AND operation on register A with the value 13
ld c, a     ; The result should be 8, wich is now stored inside register C
add a, #2   ; Add 2 to register A, wich should bring it back to 10
ld b, #4    ; Load 4 into register B
or b        ; Perform OR operation on register A with register B
ld d, a     ; The result should now be 14, store the result inside register D
ld b, #1    ; Load 1 inside register B
xor b       ; Perform XOR operation on register A with register B
ret         ; Register A should be 15, register B should be 1, register C should be 8, register D should be 14
