import gym

from environment.environment import Environment


class CartPoleEnvironment(Environment):
    def __init__(self) -> None:
        super().__init__()
        self.env = gym.make('CartPole-v1')

    def perform_action(self, state, action):
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def get_possible_states(self):
        result = list()
        i = self.env.observation_space.low[0]
        initial_j = self.env.observation_space.low[2]

        while i < self.env.observation_space.high[0]:
            j = initial_j
            while j < self.env.observation_space.high[2]:
                state_tuple = (round(i, 1), round(j, 1))
                result.append(state_tuple)
                j = j + 0.1
            i = i + 0.1

        return result

    def get_random_action(self):
        return self.env.action_space.sample()

    def get_state_id(self, state):
        return round(state[0], 1), round(state[2], 1)

    def get_possible_actions(self):
        return self.env.action_space

    def render(self):
        return self.env.render()

    def close(self):
        return self.env.close()
