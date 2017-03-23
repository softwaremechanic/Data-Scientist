import gensim

# Ok few observations:
# * -- this is a unsupervised clustering problem
# * -- It is a NLP-area problem
# * -- The documents has a bunch of mis-spelt/sms shortened words, so can benefit from some
# translation measure
# * -- Max topics/document types 8
# * -- Not much grammar or structure so most likely reviews/comments on the internet
# * -- since so much of the text is mis-spelt and not structured most standard linguistics based
# approach will need massive preprocessing


max_topics = 8
def read_input(filename):
    with open(filename, 'r') as fd:
        inputs = fd.readlines()
    num_docs = int(inputs.pop(0))
    assert len(inputs) == num_docs
    return [each.strip('\n') for each in inputs]

# Perhaps just a simple tf-idf will work let's start some experimentatnos
#def
print(read_input('trainingdata.txt'))
