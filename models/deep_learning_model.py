from models.model import Model


class DeepLearningModel(Model):
    def __init__(self, environment) -> None:
        super().__init__()
        self.environment = environment
        self._deep_learning_model = self._generate_deep_learning_model()

    def _generate_deep_learning_model(self):
        return None

    def predict(self, state):
        raise Exception('This is an interface! Method Not Implemented!')

    def update_state(self, state, action, value):
        raise Exception('This is an interface! Method Not Implemented!')