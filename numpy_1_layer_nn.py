from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        
        random.seed(1)

        self.synaptic_weights = 2 * random.random((3,1)) - 1








if __name__ = '__main__':

    neural_network = NeuralNetwork()

    print("Random starting synaptic weights")
    print(neural_network.synaptic_weights)

    training_set_inputs = array([[1,0,1],[1,1,0],[1,0,0],[1,1,1]])
    training_set_outputs = array([[1,1,0,0]]).T

    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print(" New synaptic weights after training : ",)
    print(neural_network.synaptic_weights)

    print('')