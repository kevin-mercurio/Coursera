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

def extract_place(json_obj):
    tweet_dict = json.loads(json_obj)

    if not tweet_dict.has_key('place'):
        return None
    else:
        return tweet_dict['place']


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

def score_by_state(tweets, sent_dict):

    tweet_scores = []
    state_sent = {}
    for json_obj in tweets:
        text = extract_text(json_obj) 
        usr = extract_place(json_obj) 
        if usr != None and usr['country_code'] == 'US':
            state = usr['full_name'][-2:]
            total_score = score_tweet(text, sent_dict)

            if state not in state_sent:
                state_sent[state] = total_score
            else:
                state_sent[state] += total_score

    return state_sent

if __name__ == '__main__':
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dict = get_sent_dict(sent_file)
    state_scores = score_by_state(tweet_file, sent_dict)
    print sorted(state_scores, key = state_scores.get, reverse=True)[0]




