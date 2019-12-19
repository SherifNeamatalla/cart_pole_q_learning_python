class Environment:
    def __init__(self) -> None:
        super().__init__()

    def perform_action(self, state, action):
        raise Exception('This is an interface! Method Not Implemented!')

    def get_possible_states(self):
        raise Exception('This is an interface! Method Not Implemented!')

    def get_possible_actions(self):
        raise Exception('This is an interface! Method Not Implemented!')

    def reset(self):
        raise Exception('This is an interface! Method Not Implemented!')

    def render(self):
        raise Exception('This is an interface! Method Not Implemented!')

    def get_state_id(self, state):
        raise Exception('This is an interface! Method Not Implemented!')

    def close(self):
        raise Exception('This is an interface! Method Not Implemented!')

    def get_random_action(self):
        raise Exception('This is an interface! Method Not Implemented!')

    def get_game_over_reward(self):
        raise Exception('This is an interface! Method Not Implemented!')
