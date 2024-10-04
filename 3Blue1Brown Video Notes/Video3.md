# 3Blue1Brown Video 3: Backpropogation

## Video 3: Getting Correct Output / An Intuitive Example:

- The way we do a gradient descent depends on the training data, how do we train the neural network to get good activations?
- When the neural network isn't trained, the activations are going to be random values
- That's why it's very important to keep track of actions done on weights and keep track of activations
- More important to target correct activation outputs then an activation we expect, but not the neuron we are looking for
- To increase activation you can do **three things:** Increase Weights `wᵢ`, Increase Bias `b`, Change Previous Activation Layer `aᵢ`
- By adding together the values you want to adjust for each layer for the neurons, you can influence the hidden layer before the output layer
- Whats commonly done is switching the training data into a bunch of training data 
- Then compute a gradient step for every mini batch
- Not the most efficent step downhill but gives you a good approximation/significant computational speedup
- This is called Stochastic Gradient Descent
- A big challenge is doing this training right and doing the correct steps, along with having a very smooth cost function
