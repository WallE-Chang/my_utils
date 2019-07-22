def random_mini_batches(X, Y, mini_batch_size = 64):
    """
    Creates a generator of random minibatches from (X, Y)
    
    Arguments:
    X -- input data, of shape (input size, number of examples) or transposition
    Y -- true "label" vector (1 for blue dot / 0 for red dot), of shape (1, number of examples) or transposition
    mini_batch_size -- size of the mini-batches, integer
    
    Returns:
    mini_batches -- generator of synchronous (mini_batch_X, mini_batch_Y)
    """
    import numpy as np
    transposition=0
    if X.shape[0]==Y.shape[0]:
        transposition=1
        X=X.T
        Y=Y.reshape(1,-1)
    m = X.shape[1]                  # number of training examples
        
    # Step 1: Shuffle (X, Y)
    permutation = list(np.random.permutation(m))


    # Step 2: Partition (X, Y)
    num_minibatches = m//mini_batch_size # number of mini batches of size mini_batch_size in your partitionning
    for index in np.array_split(permutation,num_minibatches):# return array of size mini_batch_size+1 or mini_batch_size
        mini_batch_X = X[:, index]
        mini_batch_Y = Y[:, index]
        if transposition==0:
            yield mini_batch_X,mini_batch_Y
        else:
            yield mini_batch_X.T,mini_batch_Y.T
