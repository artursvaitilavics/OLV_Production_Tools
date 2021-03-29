

class TestParsing:
    def clean_sockets(self, sockets):
        for socket in sockets:
            a = socket.split("_")
            b = list(filter(None, a))
        return {"layer": b[-2], "pass": b[-1]}
