class LoadDBException(Exception):
    def __init__(self):
        self.txt = 'Error in load DB'
        super().__init__(self.txt)
