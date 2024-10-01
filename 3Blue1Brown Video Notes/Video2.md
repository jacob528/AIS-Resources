# 3Brown1Blue Video 2

## Training a Network:

- For the example of a neural network that uses digits, to test this network you would want an algorithm so that you could train the network with labeled data.
- To ensure that this network could work, you continue testing with different sets of labeled data (in this case handwritten numbers) and then see how accurately it classifies the images and adjust weights/biases.
- It’s more like calculus that helps the machine learn (finding the minima of a function).
- Define some cost function (that tells the computer it does not work).
- Cost function (add up squares of differences between bad values and values you want). The cost should be small so you know the network knows. Consider the average cost of all training data.
- You should tell the computer and program to improve cost. Find an input to minimize the cost function.

## Gradient Descent:

- A more flexible task is to find the slope of where the input should step to make the cost closer. To the left if positive, to the right if negative. This should help find the minimal cost. The global minimum is hard to find, because the cost function could have multiple local inputs.
- Say the function is a 3D space: Use the negative of the gradient (direction of steepest decrease) to find the direction you should step to go downhill.
- Compute cost, take a small step downward—this is called **Gradient Descent**.
- Algorithm for computing gradient efficiently is called **Backpropagation**.
- This means you should have a very smooth and nice output from the cost function to make the machine learn most effectively.
- Relative components (weights and biases) from the output determine which ones we should improve more (target more wrong values).
- Some weights could have more effect towards the cost function.
- In some input function/cost function like `3/2x^2 + ½y`, x has way more importance, so moving in the x direction is more important.

## How Well Does It Do?

- In the digit example, it works with 96% accuracy, and sometimes the data is so hard to tell.
- The weights and biases pick up a random pattern, not really splitting the digits up like originally thought in video 1.