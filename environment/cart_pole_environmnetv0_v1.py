import math

import gym

from environment.environment import Environment


class CartPoleEnvironmentV0_V1(Environment):

    def __init__(self) -> None:
        super().__init__()
        self.env = gym.make('CartPole-v0')
        self.buckets = (1, 1, 6, 12)

    def perform_action(self, state, action):
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def get_possible_states(self):
        result = list()

        for cart_position in range(self.buckets[0]):
            for cart_velocity in range(self.buckets[1]):
                for cart_angle in range(self.buckets[2]):
                    for pole_velocity in range(self.buckets[3]):
                        state_tuple = cart_position, cart_velocity, cart_angle, pole_velocity
                        result.append(state_tuple)

        return result

    def get_random_action(self):
        return self.env.action_space.sample()

    def get_state_id(self, state):
        return self.discretize(state)

    def get_possible_actions(self):
        return self.env.action_space

    def render(self):
        return self.env.render()

    def close(self):
        return self.env.close()

    def _get_state(self, cart_velocity, pole_velocity, cart_position, cart_angle):

        return int(cart_velocity), int(pole_velocity)

    def _scale_number(self, number, max, min, new_max, new_min):
        max = max / 10 ** 30
        min = min / 10 ** 30
        number = number / 10 ** 30
        return ((new_max - new_min) * (number - min) / (max - min)) + new_min

    def discretize(self, obs):
        upper_bounds = [self.env.observation_space.high[0], 0.5, self.env.observation_space.high[2], math.radians(50)]
        lower_bounds = [self.env.observation_space.low[0], -0.5, self.env.observation_space.low[2], -math.radians(50)]
        ratios = [(obs[i] + abs(lower_bounds[i])) / (upper_bounds[i] - lower_bounds[i]) for i in range(len(obs))]
        new_obs = [int(round((self.buckets[i] - 1) * ratios[i])) for i in range(len(obs))]
        new_obs = [min(self.buckets[i] - 1, max(0, new_obs[i])) for i in range(len(obs))]
        return tuple(new_obs)

    def get_game_over_reward(self):
        return -5
