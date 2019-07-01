sentences = """Thomas Jefferson began building Monticello at the\
age of 26.\n"""
sentences += """Construction was done mostly by local masons and\
carpenters.\n"""
sentences += "He moved into the South Pavilion in 1770. the \n"
sentences += """Turning Monticello into a neoclassical masterpiece\
    was Jefferson's obsession."""
corpus = {}
for i, sent in enumerate(sentences.split('\n')):
    corpus['sent{}'.format(i)] = dict((tok, 1) for tok in sent.split())   
print(corpus.keys())
for k,v in corpus.items():
    print(k,v)
