import pandas as pd 
import dateutil

sentence="Thomas Jefferson started building monte cello at the age of 26"

token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))
# print('vocab is '+ vocab)
pd.DataFrame(onehot_vectors, column=vocab)