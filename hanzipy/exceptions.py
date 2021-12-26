class NotAHanziCharacter(Exception):
    def __init__(self, character, message=None):
        if not message:
            message = f'{character} is not a Hanzi Character.'

        self.message = message
        super().__init__()
