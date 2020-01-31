#Written By Anirudh Giri
#A Program To Parse A .wnn File For The "WNN : File Format For Neural Network Interchange" Paper
import sys

file = open(sys.argv[1])#open the file passed as the argument through the command line

inputs = int(file.readline())#the first line of the file contains the number of inputs
print("Number of Inputs : {}".format(inputs))

hiddens = int(file.readline())#the second line of the file contains the number of hidden layers
print("Number of Hidden Layers : {}".format(hiddens))

nodes_per_hidden_layer = file.readline().strip()#the third line contains the number of nodes per hidden layer
if len(nodes_per_hidden_layer) == 1: #if there is only one number listed, all hidden layers contain that number of nodes 
    print("Number of Nodes Per Hidden Layer : {}".format(nodes_per_hidden_layer[0]))
else:
    for i,num in enumerate(nodes_per_hidden_layer):#else, the number of nodes for each hidden layer is listed seperated by linebreaks
        print("Number of Nodes in layer {} : {}".format(i+1,nodes_per_hidden_layer[i]))

outputs = int(file.readline())#the fourth line contains the number of outputs
print("Number of Outputs : {}".format(outputs))

activation_functions_dictionary = {
    0 : "Sigmoid",
    1 : "Tanh",
    2 : "Arctan",
    3 : "Softplus",
    4 : "ReLU",
    5 : "Leaky Relu",
    6 : "ELU"
}
activation_function = int(file.readline())#the fifth line contains the activation function used
print("Activation Function Used : {}".format(activation_functions_dictionary[activation_function]))

if activation_function == 5 or activation_function ==  6:
    alpha_value = file.readline()#an alpha value is used for the Leaky ReLU and ELU activation functions
    print("Alpha value : {}".format(alpha_value))

print("Weight values : ")
for i in range(hiddens+1):
    print(file.readline().strip())#The weight values per layer are then listed
print("Bias Values:")
for i in range(hiddens+1):
    print(file.readline().strip())#Finally, the bias values per layer are listed
