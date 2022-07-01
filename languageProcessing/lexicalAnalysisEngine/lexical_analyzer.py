from ..parseUtils.parseHandler import Parsing
import re
import nltk
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer
from nltk import tokenize, pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet

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

      #print(pos_tag(tokens))

      for token, tag in pos_tag(tokens):
          tags = tag[0].lower()
          tag = tag if tag in ['a','r','n','v'] else None
          lemma = lemmatizer.lemmatize(token, tag) if tag else token
          lemmatized_tokens.append(lemma)
      
      #print(lemmatized_tokens)
      
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

  def runAnalysis(string):
    print('\n Sentences: ->', Analyzer.sentence_tokenizer(string))
    print('\n Tokens: ->', Analyzer.tokenize(string))
    tokens = Analyzer.tokenize(string)
    print('\n Tri-grams: ->', Analyzer.ngram_tokenizer(3, tokens))
    print('\n Stop Words: ->', Analyzer.stop_word_remover(tokens))
    print('\n Normalized Tokens: ->', Analyzer.token_normalizer(tokens))
    print('\n Lemmatized Tokens: ->', Analyzer.lemmatization(tokens))
    print('\n Parts of Speech: ->', Analyzer.tag_pos(tokens))
    print('\n Stemmed Tokens: ->', Analyzer.stemming(tokens))

    sentences = Analyzer.sentence_tokenizer(string)
    pos_groupings = []
    for unit in sentences:
      pos_grouping = (Analyzer.tag_pos(Analyzer.tokenize(unit)))
      pos_groupings.append(pos_grouping)


    return pos_groupings


