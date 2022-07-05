from os import name
import nltk
from nltk import RegexpParser
from ..lexicalAnalysisEngine.lexical_analyzer import Analyzer
nltk.download('maxent_ne_chunker')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('cmudict')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from nltk.metrics.distance  import edit_distance
nltk.download('words')
from nltk.corpus import words

import pandas as pd
import numpy as np
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize
from nltk import Tree
import spacy
import deplacy
#run command -> python -m spacy download en_core_web_sm
en = spacy.load('en_core_web_sm')
from nltk.corpus import wordnet
import re
from pattern.text.en import suggest

correct_words = words.words()

class Optimizer:
    
    def spellCheck(string):
        tokens = Analyzer.tokenize(string)
        corrected_tokens = []
        for token in tokens:
            temp = [(edit_distance(token, w),w) for w in correct_words if w[0]==token[0]]
            corrected_tokens.append(sorted(temp, key = lambda val:val[0])[0][1])
            # if token in spell_corrector:
            #     corrected_tokens.append(token)
            # else:
            #     corrected_tokens.append(spell_corrector.get(token, token))
        return ' '.join(corrected_tokens)

    def remove_invalid_words(string):
        tokens = Analyzer.tokenize(string)
        fixed_sentence = list(filter(lambda x: x in words.words(), tokens))
        output = ' '.join(fixed_sentence)
        return output

    def remove_repeated_words(string):
        tokens = Analyzer.tokenize(string)
        seen = set()
        seen_add = seen.add
        def add(x):
            seen_add(x)  
            return x
        return ' '.join( add(i) for i in tokens if i not in seen )

    def remove_duplicated_sentences(string): 
        sentences = Analyzer.sentence_tokenizer(string)
        unique_sentences = []
        for sentence in sentences:
            if sentence not in unique_sentences:
                unique_sentences.append(sentence)
        return ' '.join(unique_sentences)
    
    def search_for_duplicate_letters(string):
        tokens = Analyzer.tokenize(string)
        duplicate_letters = []
        for token in tokens:
            result = "".join(dict.fromkeys(token))
            duplicate_letters.append(result)
        return ' '.join(duplicate_letters)

    #Splitting Independent clauses
    def spl_by_clause(str_sen):
        text = str_sen
        doc = en(text)
        seen = set()
        chunks = []
        for sent in doc.sents:
            heads = [cc for cc in sent.root.children if cc.dep_ == 'conj']
            for head in heads:
                words = [ww for ww in head.subtree]
                for word in words:
                    seen.add(word)
                chunk = (' '.join([ww.text for ww in words]))
                chunks.append( (head.i, chunk) )
            unseen = [ww for ww in sent if ww not in seen]
            chunk = ' '.join([ww.text for ww in unseen])
            chunks.append( (sent.root.i, chunk) )
        chunks = sorted(chunks, key=lambda x: x[0])
        for ii, chunk in chunks:
            print(chunk)
        print()
    
    def remove_repeated_characters(word):
        pattern = re.compile(r"(\w*)(\w)\2(\w*)")
        substitution_pattern = r"\1\2\3"
        while True:
            if wordnet.synsets(word):
                return word
            new_word = pattern.sub(substitution_pattern,word)
            if new_word != word:
                word = new_word
                continue
            else:
                return new_word
        
