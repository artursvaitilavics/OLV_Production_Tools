class ParseSockets:
    def clean_socket(self, socket):
        # clean_socket = socket.split("_")
        # clean_socket = clean_socket[0]
        a = socket.split("/")
        b = list(filter(None, a))
        pass_name = b[1].split("_")
        c = socket
        return {"layer": b[0], "pass": pass_name[0], "socket": c}


clean_socket = ParseSockets().clean_socket("layer_01/Denoise_")
print(clean_socket)