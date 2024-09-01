#Implement a Perceptron Class that can be initialized with a list of weights and bias and a method named 
#forward to compute sigmoid of weighted sum of inputs and bias.

import math

class Perceptron: 
  def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias

  def sigmoid(self,x):
    return 1 / (1 + math.exp(-x))

  def forward(self, inputs):
    weighted_sum = 0
    for x, w in zip(inputs, self.weights):
      weighted_sum += x * w
    weighted_sum += self.bias
    return self.sigmoid(weighted_sum)


#usage

weights = [0.5,0.3,0.2]
bias = 1
perceptron = Perceptron(weights, bias)

inputs = [1,2,3]
output = perceptron.forward(inputs)
print(output)
    
