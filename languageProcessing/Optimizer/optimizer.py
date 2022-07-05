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