if __name__ = '__main__':

    neural_network = NeuralNetwork()

    print("Random starting synaptic weights")
    print(neural_network.synaptic_weights)

    training_set_inputs = array([[1,0,1],[1,1,0],[1,0,0],[1,1,1]])
    training_set_outputs = array([[1,1,0,0]]).T