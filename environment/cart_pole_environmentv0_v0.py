import math

import gym

from environment.environment import Environment


class CartPoleEnvironmentV0_V0(Environment):
    CART_VELOCITY_MAX = 20
    CART_VELOCITY_MIN = 0

    ANGLE_VELOCITY_MAX = 20
    ANGLE_VELOCITY_MIN = 0

    def __init__(self) -> None:
        super().__init__()
        self.env = gym.make('CartPole-v0')

    def perform_action(self, state, action):
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def get_possible_states(self):
        result = list()
        cart_position = self.env.observation_space.low[0]

        while cart_position < self.env.observation_space.high[0]:
            cart_angle = self.env.observation_space.low[2]
            while cart_angle < self.env.observation_space.high[2]:
                for cart_velocity in range(2):
                    for pole_velocity in range(2):
                        cart_velocity_sign = -1 if cart_velocity == 0 else 1
                        pole_velocity_sign = -1 if pole_velocity == 0 else 1

                        state_tuple = self._get_state(cart_velocity_sign, pole_velocity_sign, cart_position, cart_angle)
                        result.append(state_tuple)
                cart_angle = cart_angle + 0.1
            cart_position = cart_position + 0.1

        return result

    def get_random_action(self):
        return self.env.action_space.sample()

    def get_state_id(self, state):

        return self._get_state(state[1], state[3], state[0], state[2])

    def get_possible_actions(self):
        return self.env.action_space

    def render(self):
        return self.env.render()

    def close(self):
        return self.env.close()

    def _get_state(self, cart_velocity, pole_velocity, cart_position, cart_angle):
        cart_velocity = 0 if cart_velocity <= 0 else 1
        pole_velocity = 0 if pole_velocity <= 0 else 1
        return cart_velocity, pole_velocity, round(cart_position, 1), round(cart_angle, 1)

    def get_game_over_reward(self):
        return -5
