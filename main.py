from nltk.tokenize import RegexpTokenizer
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from gensim import corpora, models
import gensim

#Extract abstracts from txt file and put them in a list
with open('data/abstracts.txt', mode='r', encoding='utf-8-sig') as file:
    abstracts = file.read().lower()
abstract_set = abstracts.split('\n\n')

#create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

def lemmatize_stemming(text):
    return p_stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def preprocess(text):
    processed_text = []
    
    #create token and remove stop words
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            processed_text.append(lemmatize_stemming(token))
    return processed_text
    
processed_docs = []

for abstract in abstract_set:
    processed_docs.append(preprocess(abstract))

#create dictionary from processed docs
dictionary = corpora.Dictionary(processed_docs)

#convert text to Bag of Word
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

#Run LDA
lda_model = gensim.models.LdaMulticore(corpus, num_topics=5, id2word = dictionary, passes=10)

for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic ))
    print("\n")
