import sys
import json
import collections

def get_sent_dict(sent_file):
    """
    creates a dictionary where key = term, value = sentiment as integer
    """

    scores = collections.defaultdict(int)

    for line in sent_file:
        term, score = line.split('\t') #extract term and score from tab delimited file
        scores[term] = int(score) #convert string to int
    return scores

def score_tweet(tweet_text, sent_dictionary):

    """
    score the sentiment for a given tweet,
    input = raw text of one tweet, and the dictionary of sentiment for each word
    """

    tweet_score = 0
    tweet_text = tweet_text.split(' ')

    for word in tweet_text:
        tweet_score += sent_dictionary[word]
    return tweet_score


def extract_text(json_obj):
    tweet_dict = json.loads(json_obj)

    if not tweet_dict.has_key('text'):
        return ''

    else:
        return tweet_dict['text']


def transform_and_save(input_list):
    if not input_list:
        return False
    else:
        for score in input_list:
            print score
        outfile = open("problem_2_test.txt", "w")
        print >> outfile, "\n".join(str(score) for score in input_list)
        outfile.close()
        #return True

def score_all_tweets(tweets, sent_dict):

    tweet_scores = []
    for json_obj in tweets:
        text = extract_text(json_obj) 

        total_score = score_tweet(text, sent_dict)

        tweet_scores.append(total_score)

    return tweet_scores

if __name__ == '__main__':
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dict = get_sent_dict(sent_file)
    scores_list = score_all_tweets(tweet_file, sent_dict)

    transform_and_save(scores_list)



