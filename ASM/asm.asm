section .data
    msg db "Hello, WorldS!", 10    ; Наша строка и символ перевода строки
    msg_len equ $ - msg           ; Вычисление длины строки

section .text
    global _start

_start:
    ; 1. Системный вызов для вывода текста (sys_write)
    mov rax, 1                    ; 1 — это номер системного вызова sys_write
    mov rdi, 1                    ; 1 — это файловый дескриптор stdout (экран)
    mov rsi, msg                  ; Указатель на начало нашей строки
    mov rdx, msg_len              ; Сколько байт нужно вывести
    syscall                       ; Приказ ядру Linux: "Выполни вызов!"

    ; 2. Системный вызов для корректного выхода (sys_exit)
    mov rax, 60                   ; 60 — это номер системного вызова sys_exit
    mov rdi, 0                    ; 0 — код возврата (ошибок нет)
    syscall                       ; Приказ ядру Linux: "Выйди из программы!"
