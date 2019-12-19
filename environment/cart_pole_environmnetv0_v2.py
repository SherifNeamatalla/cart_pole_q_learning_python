import gym

from environment.environment import Environment


class CartPoleEnvironmentV0_V2(Environment):
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

        for cart_velocity in range(2):
            for pole_velocity in range(2):
                for cart_position in range(-1, 2):
                    for cart_angle in range(-1, 2):
                        state_tuple = cart_velocity, pole_velocity, cart_position, cart_angle
                        result.append(state_tuple)

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
        cart_position = -1 if cart_position <= -2 else 1 if cart_position >= 2 else 0
        cart_angle = -1 if cart_angle <= -2 else 1 if cart_angle >= 2 else 0

        return cart_velocity, pole_velocity, cart_position, cart_angle

    def get_game_over_reward(self):
        return -5
