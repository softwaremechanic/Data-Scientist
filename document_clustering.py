
# coding: utf-8

# In[17]:

from datascienceutils import analyze
from datascienceutils import features
from datascienceutils.features import nlp
from datascienceutils import plotter
from datascienceutils import utils
from datascienceutils import sklearnUtils as sku
from datascienceutils import settings
settings.MODELS_BASE_PATH='./models'

import pandas as pd
import numpy as np
import bokeh
from bokeh.plotting import output_notebook
#output_notebook(bokeh.resources.INLINE)

#get_ipython().magic('matplotlib inline')


# In[18]:


max_topics = 8
def read_input(filename):
    with open(filename, 'r') as fd:
        inputs = fd.readlines()
    num_docs = int(inputs.pop(0))
    assert len(inputs) == num_docs
    return [nlp.filter_letters_only(each.strip('\n')) for each in inputs]


# In[19]:

input_docs = [each.split(' ') for each in read_input('./trainingdata.txt')]
input_docs = [nlp.filter_stop_words(each) for each in input_docs]


# In[ ]:

model = features.nlp.word_2_vector(input_docs, hs=1, negative=0)


# In[ ]:

df = pd.DataFrame()
from scipy import spatial
import itertools

def get_sent_vector(sent):
    vectors = list()
    for word in sent:
        if word in model.wv.vocab:
            vectors.append(model[word])
    return np.mean(vectors)

df['id'] = pd.Series(range(len(input_docs)))
df['score'] = model.score(input_docs)
df['doc_vector'] = [get_sent_vector(doc) for doc in input_docs]




################################################################################
#       SPECTRAL
################################################################################
model = utils.get_model_obj('spectral', n_clusters=8)
cluster_labels = model.fit_predict(dataframe)


if len(set(cluster_labels)) > 1:
    silhouette_avg = silhouette_score(dataframe, cluster_labels)
    print("For clusters =8",
            "The average silhouette_score is :", silhouette_avg)
else:
    print("No cluster found with cluster no:%d and algo type: %s"%(cluster, cluster_type))
model_params= {'model_type': 'spectral'}
sku.dump_model(model, 'spectral_model')


################################################################################
#      K-MEANS
################################################################################
model = utils.get_model_obj('kmeans', n_clusters=8)
cluster_labels = model.fit_predict(dataframe)


if len(set(cluster_labels)) > 1:
    silhouette_avg = silhouette_score(dataframe, cluster_labels)
    print("For clusters =8",
            "The average silhouette_score is :", silhouette_avg)
else:
    print("No cluster found with cluster no:%d and algo type: %s"%(cluster, cluster_type))
model_params= {'model_type': 'kmeans'}
sku.dump_model(model, 'kmeans_model')
# In[ ]:

#plotter.show(analyze.dist_analyze(df, 'score'))


# In[ ]:

# Based on this flowchart http://scikit-learn.org/stable/tutorial/machine_learning_map/ for unsupervised clustering,
# we can use either k-means or spectral clustering
#analyze.silhouette_analyze(df, cluster_type='spectral')


# In[ ]:

#analyze.silhouette_analyze(df, cluster_type='kmeans')


# In[ ]:

#df.head()


# In[ ]:

#import sompy as sp
#factory = sp.SOMFactory()
#sm = factory.build(tfidfFeatures, mapsize=(10,10),normalization='var', initialization='pca')
#sm.train(n_job=6, verbose='INFO')
#
#
## In[ ]:
#
#v=sompy.mapview.View2DPacked(50,50, 'test', text_size=8)
#v.show(sm, what='codebook', cmap='jet', col_sz=6)
#v.show(sm, what='cluster', cmap='jet', col_sz=6)
#
#h = sompy.hitmap.HitMapView(10, 10, 'hitmap', text_size=8, show_text=True)
#h.show(sm)

