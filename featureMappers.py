import nltk

class FeatureMapper():
    """Each featureMap would inherit from this class"""
    
    def combineFeatures(featureMapArray):
        """ Combine multiple features to one. """
        pass # ToDo: Implement
    
    def getTokens(self, string):
        return nltk.word_tokenize(string)

    def getTags(self, string):
        tokens = self.getTokens(string)
        return nltk.pos_tag(tokens)


class TagSequence(FeatureMapper):

    def getFeatureVector(self,string):
        """
        Inputs a tweet string and map features
        Returns a vector of floats 
        """
        tags = self.getTags(string)

        return [len(x[1]) for x in tags]

