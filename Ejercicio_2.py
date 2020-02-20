from Neuron import Neuron
import numpy as np

class Perceptron(object):
    def __init__(self):
        self.names = []
        self.weights = []
        self.results =  []

    def activation_function(self, x):
        if x >= 0:
            return 1
        else:
            return 0

    def file_name(self,name):
        self.names.append(name)

    def train(self,rows,learning_rate):
        tofit = Neuron(rows,learning_rate)
        tofit.print_weights()
        self.weights.append(tofit.initialize("a1.csv",1,2))
        tofit.print_weights()
        tofitI = Neuron(rows,learning_rate)
        #tofitI.print_weights()
        self.weights.append(tofitI.initialize("a1.csv",1,2))
        tofitI.print_weights()
    
    def evaluate(self, ans, ansI,input):
        y = []
        p = np.array([ans,ansI])
        x = np.insert(p,input,1)
        for i in range(2):
            y.append(self.predict(x,i))
            print(y)
        if(y[0] == 0 and y[1]==0):
            print("Es ligero y poco usado")
        elif(y[0] == 0 and y[1]==1):
            print("Es ligero y muy usuado")
        elif(y[0] == 1 and y[1]==0):
            print("Es pesado y poco usado")
        elif(y[0] == 1 and y[1]==1):
            print("Es pesado y muy usado")

    def predict(self, x, i):
        array = np.array(self.weights[i])
        weighted_sum = array.T.dot(x)
        print(weighted_sum)
        activation = self.activation_function(weighted_sum)
        return activation

def main():
    n = Perceptron()
    n.train(2,1)
    a = float(input("Peso del libro: "))
    b = float(input("Frecuencia del libro: "))
    n.evaluate(a,b,2)

main()


