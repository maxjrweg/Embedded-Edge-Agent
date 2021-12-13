import time

from wasmer import engine, Store, ImportObject, Function, Module, Instance, Memory, MemoryType
from wasmer_compiler_cranelift import Compiler


store = Store(engine.JIT(Compiler))
memory_type = MemoryType(minimum=1, shared=False)
memory = Memory(store, memory_type)

module = Module(store, open("./hello-world-memory-import.wasm", "rb").read())

#
# Helper function to decode a string from the WASM memory buffer
# from the starting pointer and length.
#
def decode_string(memory, ptr_start, length):
    buffer = memoryview(memory.buffer)
    return str(buffer[ptr_start:(ptr_start + length)], "utf-8")

#
# Called by the EEA to log tracing information. This is useful
# during development to help debug what the EEA is doing.
#
def eea_trace(message_ptr:int, message_length:int, level:int) -> int:
    print("eea_trace")
    print(str(level) + ": " + decode_string(memory, message_ptr, message_length))
    return 0

# Import memory and functions.
# https://wasmerio.github.io/wasmer-python/api/wasmer/#wasmer.ImportObject
import_object = ImportObject()
import_object.register(
    "env",
    {
    "memory": memory,
    "eea_trace": Function(store, eea_trace),
    }
)

# Create the executable instance of the WebAssembly module.
# https://wasmerio.github.io/wasmer-python/api/wasmer/#wasmer.Instance
instance = Instance(module, import_object)

# Initialize the EEA.
return_code = instance.exports.eea_init()
print("eea_init return code: " + str(return_code))

while(True):
    # Every second, invoke the eea_loop exported function.
    # Pass the current time, in milliseconds since epoch.
    instance.exports.eea_loop(int(time.time() * 1000))
    time.sleep(1)