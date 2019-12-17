class AlgorithmConfiguration:
    def __init__(self, epsilon, gamma, learning_rate, epsilon_decay, epsilon_min) -> None:
        super().__init__()
        self.epsilon = epsilon
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
