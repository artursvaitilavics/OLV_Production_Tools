class ParseSockets:
    def clean_socket(self, socket):
        a = socket.split("_")
        b = list(filter(None, a))
        c = socket
        return {"layer": b[-2], "pass": b[-1], "socket": c}
