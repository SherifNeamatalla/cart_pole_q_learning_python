from algorithm.algorithm_configuration import AlgorithmConfiguration
from algorithm.q_algorithm_controller import QAlgorithmController
from environment.cart_pole_environment import CartPoleEnvironment

environment = CartPoleEnvironment()
algorithm_configuration = AlgorithmConfiguration(0.2, 0.95, 0.1, 0.99993, 0.005)
controller = QAlgorithmController(environment, algorithm_configuration)
controller.train(500)

controller.train(100)
controller.train(100)

controller.train(100)

controller.train(100)

controller.train_and_render(100)
