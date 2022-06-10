# coding = "utf-8"

class UsersException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
