
import json
import sys
import collections 

def hw(sent_file, tweets):

    sent_dict = get_sent_dict(sent_file)
    
    new_terms = {}
    for json_obj in tweets:
        text = extract_text(json_obj) 
        tweet_score = score_tweet(text, sent_dict)

        tweet_words = text.split(' ')
        for word in tweet_words:
            if word.encode('utf-8') not in sent_dict.keys():
                new_word_score = float(tweet_score)
                if word.encode('utf-8') in new_terms.keys():
                    new_terms[word.encode('utf-8')] = new_terms[word.encode('utf-8')] + new_word_score
                else:
                    new_terms[word.encode('utf-8')] = new_word_score

    for key, val in new_terms.iteritems():
        print key, float(val)

def get_sent_dict(sent_file):
    """
    creates a dictionary where key = term, value = sentiment as integer
    """

    scores = {}

    for line in sent_file:
        term, score = line.split('\t') #extract term and score from tab delimited file
        scores[term] = float(score) #convert string to int
    return scores

def score_tweet(tweet_text, sent_dictionary):

    """
    score the sentiment for a given tweet,
    input = raw text of one tweet, and the dictionary of sentiment for each word
    """

    tweet_score = 0
    tweet_text = tweet_text.split(' ')

    for word in tweet_text:
        if word.encode('utf-8') in sent_dictionary.keys():
            tweet_score += sent_dictionary[word]
    return tweet_score


def extract_text(json_obj):
    tweet_dict = json.loads(json_obj)

    if not tweet_dict.has_key('text'):
        return ''

    else:
        return tweet_dict['text']


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
