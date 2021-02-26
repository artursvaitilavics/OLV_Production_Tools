

class TestParsing:
    def clean_sockets(self, sockets):
        for socket in sockets:
            a = socket.split("_")
            b = list(filter(None, a))
        return {"layer": b[-2], "pass": b[-1]}




# Testing class

# parsing = Parsing()


# sockets = ["SYD_XG_2L_img_Image/SYD_XG_2L_img_Image_",
#            "SYD_XG_2L_img_Denoise/SYD_XG_2L_img_Denoise_"]



# print(parsing.clean_sockets(sockets).get("pass"))