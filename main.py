from algorithm.algorithm_configuration import AlgorithmConfiguration
from algorithm.q_algorithm_controller import QAlgorithmController
from environment.cart_pole_environmentv0_v0 import CartPoleEnvironmentV0_V0
from environment.cart_pole_environmnetv0_v1 import CartPoleEnvironmentV0_V1
from environment.cart_pole_environmnetv0_v2 import CartPoleEnvironmentV0_V2

environment = CartPoleEnvironmentV0_V1()
algorithm_configuration = AlgorithmConfiguration(0.4, 1, 0.4, 0.99993, 0.005)
controller = QAlgorithmController(environment, algorithm_configuration)

controller.train(1000)
controller.train(100)

controller.train(100)

controller.train(100)

controller.train_and_render(100)
