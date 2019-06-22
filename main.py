from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

#Extract abstracts from txt file and put them in a list
with open('data/abstracts.txt', 'r') as file:
    abstracts = file.read().lower()
abstract_set = abstracts.split('\n\n')

#creare Tokenizer
tokenizer = RegexpTokenizer(r'\w+')

#create English stop words list
en_stop = get_stop_words('en')

#create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

texts = []

for abstract in abstract_set:
    #create token from each token
    raw = abstract.lower()
    tokens = tokenizer.tokenize(raw)
    
    #remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    #stem token
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    texts.append(stemmed_tokens)

dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]

ldamodel_1 = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=100)
ldamodel_2 = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=100)

print("=========== Model 1 ===========")
print(ldamodel_1.print_topics(num_topics=5, num_words=4))

print("=========== Model 2 ===========")
print(ldamodel_2.print_topics(num_topics=4, num_words=4))