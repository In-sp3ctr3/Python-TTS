from ..parseUtils.parseHandler import Parsing
from ..lexicalAnalysisEngine.lexical_analyzer import Analyzer
from ..Optimizer.optimizer import Optimizer

class Processing:

    def runAnalysis(string):
        
        noRepeatedSentences = Optimizer.remove_duplicated_sentences(string)
        noRepeatedWords = Optimizer.remove_repeated_words(noRepeatedSentences)
        spell_checked_tokens = Optimizer.spellCheck(noRepeatedWords)
        noDuplicateLetters = Optimizer.search_for_duplicate_letters(spell_checked_tokens)
        noInvalid = Optimizer.remove_invalid_words(noDuplicateLetters)
        tokens = Analyzer.tokenize(noInvalid) 

        print('\n Sentences: ->', Analyzer.sentence_tokenizer(string))
        print('\n Tokens: ->', tokens)
        print('\n No repeated Words: ->', noRepeatedWords)
        print('\n No repeated Sentences: ->', noRepeatedSentences)
        print('\n No Invalid Words: ->', noInvalid)
        print('\n No Duplicate Letters: ->', Optimizer.search_for_duplicate_letters(noInvalid))
        print('\n Tri-grams: ->', Analyzer.ngram_tokenizer(3, tokens))
        print('\n Stop Words: ->', Analyzer.stop_word_remover(tokens))
        print('\n Normalized Tokens: ->', Analyzer.token_normalizer(tokens))
        print('\n Lemmatized Tokens: ->', Analyzer.lemmatization(tokens))
        print('\n Parts of Speech: ->', Analyzer.tag_pos(tokens))
        pos_groupings = []
        pos_grouping = (Analyzer.tag_pos(tokens))
        pos_groupings.append(pos_grouping)

        return pos_groupings