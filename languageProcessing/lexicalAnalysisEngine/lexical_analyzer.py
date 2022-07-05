from ..parseUtils.parseHandler import Parsing
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('cmudict')
nltk.download('words')
from nltk.corpus import words
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer
from nltk import tokenize, pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet
from nltk.metrics.distance  import edit_distance
correct_words = words.words()

class Analyzer:

    def tokenize(string):
        pattern = re.compile(r"([-\s.,;!?])+") 
        tokens = pattern.split(string)  
        tokens = [x for x in tokens if x and x not in '- \t\n.,;!?']  
        return tokens
  
    def sentence_tokenizer(string):
        return tokenize.sent_tokenize(string)  

    def ngram_tokenizer(n, tokens):
        ntokens = list(ngrams(tokens, n)) 
        return ntokens

    def stop_word_remover(tokens):
        stop_words = nltk.corpus.stopwords.words('english')
        stop_word_tokens = [sw for sw in tokens if sw and sw in stop_words]
        return stop_word_tokens


    def token_normalizer(tokens):
        normalized_tokens = [token.lower() for token in tokens]
        return normalized_tokens

    def lemmatization(tokens):     
        
        lemmatizer = WordNetLemmatizer()

        lemmatized_tokens = []

        for token, tag in pos_tag(tokens):
            tags = tag[0].lower()
            tag = tag if tag in ['a','r','n','v'] else None
            lemma = lemmatizer.lemmatize(token, tag) if tag else token
            lemmatized_tokens.append(lemma)
        
        return lemmatized_tokens

    def tag_pos(tokens):
        pos_tokens = nltk.pos_tag(tokens)
        return pos_tokens

    def stemming(tokens): 
                    
        stemmer = PorterStemmer()
        stemmed_tokens = []
        for token in tokens:
            stemmed_token = ' '.join([stemmer.stem(w).strip("'") for w in token.split()])
            stemmed_tokens.append(stemmed_token)
        return stemmed_tokens



