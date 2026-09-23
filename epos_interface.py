import ctypes
import os
import platform

from config import DEVICE_NAME, PROTOCOL_STACK, INTERFACE, PORT, NODE_ID


def find_library():
    path = os.environ.get("EPOS_LIB")
    if path:
        return path
    if platform.system() == "Windows":
        return "EposCmd64.dll"
    if platform.system() == "Linux":
        return "libEposCmd.so"
    raise RuntimeError(
        "macOS development mode: use --mock. "
        "For the real EPOS library, run this on the Linux lab laptop "
        "and set EPOS_LIB to Maxon's libEposCmd.so."
    )


class Epos:
    def __init__(self):
        self.lib = ctypes.CDLL(find_library())
        self.handle = None
        self._declare_functions()

    def _declare_functions(self):
        self.lib.VCS_OpenDevice.argtypes = [
            ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p,
            ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)
        ]
        self.lib.VCS_OpenDevice.restype = ctypes.c_void_p

        self.lib.VCS_CloseDevice.argtypes = [
            ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint)
        ]
        self.lib.VCS_CloseDevice.restype = ctypes.c_int

        for name in ("VCS_ClearFault", "VCS_SetEnableState", "VCS_SetDisableState"):
            self.lib.__getattr__(name).argtypes = [
                ctypes.c_void_p, ctypes.c_ushort, ctypes.POINTER(ctypes.c_uint)
            ]
            self.lib.__getattr__(name).restype = ctypes.c_int

        self.lib.VCS_GetEnableState.argtypes = [
            ctypes.c_void_p, ctypes.c_ushort,
            ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_uint)
        ]
        self.lib.VCS_GetEnableState.restype = ctypes.c_int

        self.lib.VCS_GetFaultState.argtypes = [
            ctypes.c_void_p, ctypes.c_ushort,
            ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_uint)
        ]
        self.lib.VCS_GetFaultState.restype = ctypes.c_int

        self.lib.VCS_GetPositionIs.argtypes = [
            ctypes.c_void_p, ctypes.c_ushort,
            ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_uint)
        ]
        self.lib.VCS_GetPositionIs.restype = ctypes.c_int

        self.lib.VCS_GetVelocityIs.argtypes = [
            ctypes.c_void_p, ctypes.c_ushort,
            ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_uint)
        ]
        self.lib.VCS_GetVelocityIs.restype = ctypes.c_int

    def _err(self):
        return ctypes.c_uint(0)

    def open(self):
        err = self._err()
        self.handle = self.lib.VCS_OpenDevice(
            DEVICE_NAME, PROTOCOL_STACK, INTERFACE, PORT, ctypes.byref(err)
        )
        if not self.handle:
            raise RuntimeError(f"VCS_OpenDevice failed: 0x{err.value:08X}")

    def close(self):
        if self.handle:
            err = self._err()
            self.lib.VCS_CloseDevice(self.handle, ctypes.byref(err))
            self.handle = None

    def clear_fault(self):
        err = self._err()
        if not self.lib.VCS_ClearFault(self.handle, NODE_ID, ctypes.byref(err)):
            raise RuntimeError(f"VCS_ClearFault failed: 0x{err.value:08X}")

    def enable(self):
        err = self._err()
        if not self.lib.VCS_SetEnableState(self.handle, NODE_ID, ctypes.byref(err)):
            raise RuntimeError(f"VCS_SetEnableState failed: 0x{err.value:08X}")

    def disable(self):
        err = self._err()
        if not self.lib.VCS_SetDisableState(self.handle, NODE_ID, ctypes.byref(err)):
            raise RuntimeError(f"VCS_SetDisableState failed: 0x{err.value:08X}")

    def status(self):
        err = self._err()
        enabled = ctypes.c_bool()
        fault = ctypes.c_bool()
        position = ctypes.c_long()
        velocity = ctypes.c_long()

        if not self.lib.VCS_GetEnableState(
            self.handle, NODE_ID, ctypes.byref(enabled), ctypes.byref(err)
        ):
            raise RuntimeError(f"GetEnableState failed: 0x{err.value:08X}")

        if not self.lib.VCS_GetFaultState(
            self.handle, NODE_ID, ctypes.byref(fault), ctypes.byref(err)
        ):
            raise RuntimeError(f"GetFaultState failed: 0x{err.value:08X}")

        if not self.lib.VCS_GetPositionIs(
            self.handle, NODE_ID, ctypes.byref(position), ctypes.byref(err)
        ):
            raise RuntimeError(f"GetPositionIs failed: 0x{err.value:08X}")

        if not self.lib.VCS_GetVelocityIs(
            self.handle, NODE_ID, ctypes.byref(velocity), ctypes.byref(err)
        ):
            raise RuntimeError(f"GetVelocityIs failed: 0x{err.value:08X}")

        return {
            "enabled": enabled.value,
            "fault": fault.value,
            "position": position.value,
            "velocity": velocity.value,
        }
