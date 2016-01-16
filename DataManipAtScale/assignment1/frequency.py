import sys
import json

def load_tweets(tweets):
    data = []
    for line in tweets:
        data.append(json.loads(line))

    return data


def term_count(tweets):
    term_dict = {}
    data = load_tweets(tweets)
    for i in range(len(data)):
        if 'text' in data[i]:
            text = data[i]['text']
            if len(data[i]) > 1:
                for word in text.split():
                    word = word.encode('utf-8')
                    if word not in term_dict:
                        term_dict[word] = 1
                    else:
                        term_dict[word] += 1
    
    return term_dict

if __name__ == '__main__':
    tweet_file = open(sys.argv[1])

    term_count_dict = term_count(tweet_file)

    total_words = sum(term_count_dict.values())

    for key, val in term_count_dict.iteritems():
       print key + ' ' +str(round(val/float(total_words),6))

