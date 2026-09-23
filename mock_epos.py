class MockEpos:
    def __init__(self):
        self.connected = False
        self.enabled = False
        self.fault = False

    def open(self):
        self.connected = True
        print("[MOCK] Connection opened.")

    def close(self):
        self.connected = False
        print("[MOCK] Connection closed.")

    def clear_fault(self):
        self.fault = False
        print("[MOCK] Fault cleared.")

    def enable(self):
        if not self.connected:
            raise RuntimeError("Not connected.")
        self.enabled = True
        print("[MOCK] Controller enabled.")

    def disable(self):
        self.enabled = False
        print("[MOCK] Controller disabled.")

    def status(self):
        return {
            "connected": self.connected,
            "enabled": self.enabled,
            "fault": self.fault,
        }
