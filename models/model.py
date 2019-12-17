class Model:
    def __init__(self,environment) -> None:
        super().__init__()
        self.environment = environment

    def predict(self, state):
        raise Exception('This is an interface! Method Not Implemented!')

    def update_state(self, state, action, value):
        raise Exception('This is an interface! Method Not Implemented!')
