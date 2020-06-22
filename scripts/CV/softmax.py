# http://dataaspirant.com/2017/03/07/difference-between-softmax-function-and-sigmoid-function/
import numpy as np

def softmax(inputs):

    """
    Calculate the softmax for the give inputs (array)
    :param inputs:
    :return:
    """
    import pdb; pdb.set_trace()
    l = np.exp(inputs)
    print(f"np.exp(l) is {l}  and its type is {type(l)}")
    sum_l = print(f"np.exp(l) is {float(sum(np.exp(inputs)))}  and its type is {type(float(sum(np.exp(inputs))))}")
    
    return np.exp(inputs)/ float(sum(np.exp(inputs)))
softmax_inputs=[ 2,3,5,6]
print(f"softmax functions output:: {softmax(softmax_inputs)}")
