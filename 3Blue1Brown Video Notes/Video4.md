# 3Blue1Brown Video 4: Backpropogation Calculus

## Chain Rule in Networks:

- Start off with a simple example: every layer having one neuron
- Our goal is to figure out which weights and bias create the greatest decrease in the cost function
- Figure out how sensitive the cost function is to changes in the weights WL
- To do this we want the derivative of the cost function `dC` with respect to weight `dWL`
- However, the weight depends on the activation and bias, and then the sigmoid after.
- All these tiny nudges and derivatives resemble the chain rule, Where multiplying seperate functions gives us how sensitive the cost function is to the weight at a layer
- The derivative of the cost function with respect to the derivative of the activation layer shows the difference between the networks result, and what it's meant to be
- The derivative of the full cost function requires averaging the derivative expression all the training examples 
- The gradient vector we return consists of many of these partial derivatives 
- The idea of backpropogation is going back activation layers and seeing how sensitive this cost function is with respect to the partial derivatives.
- Other than the simple example, there is not much change with backpropogation with multiple neurons
- With multiple neurons, there become way more connections, weights, activations, and biases which we sum up