from os import name
import nltk
from nltk import RegexpParser
nltk.download('maxent_ne_chunker')
import fileHandler as FileHandler

class Parsing:

        def parser(sentences, FileName):
            grammar = RegexpParser("""
                                NP: {<DT>?<JJ.*>*<NN.*>+}   #To extract Noun Phrases
                                P: {<IN>}                   #To extract Prepositions
                                V: {<V.*>}                  #To extract all Verbs
                                PP: {<P> <NP>}              #To extract Prepositional Phrases
                                VP: {<V> <NP|PP>*}          #To extract Verb Phrases
                                FW: {<FW>}                  #To extract Foreign Words
                                CD : {<CD>}                 #To extract Cardinal Digits 
                                PRP: {<PRP.*>}              #To extract all Pronouns
                                """)

            extracted_words = []
            for x in sentences: 
                output = grammar.parse(x) 
                extracted_words.append(output)
                print("Output: -> ", output)

        def print_named_entities(pos_sentences):
            named_entities = []
            for sentence in pos_sentences:
                ne_tree = nltk.ne_chunk(sentence)
                print("\n Named Entity Tree: ->", ne_tree)

                for tree in ne_tree:
                    if hasattr(tree, 'label'):
                       named_entities.append(tree.label() + ' - ' + ' '.join(attribute[0] for attribute in tree))
            print("\n Named Entities: -> \n", named_entities)
           
            

                
