import threading
import queue
import time
import json
import os
import serial
import base64
import paho.mqtt.client as mqtt

from wasmer import engine, Store, ImportObject, Function, Module, Instance, Memory, MemoryType
from wasmer_compiler_cranelift import Compiler