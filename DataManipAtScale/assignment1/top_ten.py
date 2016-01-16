import sys
import json

def load_tweets(tweets):
    data = []
    for line in tweets:
        data.append(json.loads(line))

    return data


def term_count(tweets):
    hash_dict = {}
    data = load_tweets(tweets)
    for i in range(len(data)):
        if 'text' in data[i]:
            text = data[i]['text']
            hashtags = data[i]['entities']['hashtags']
            if len(data[i]) > 1:
                for hashtag in hashtags:
                    tag =  hashtag['text']
                    if tag not in hash_dict:
                        hash_dict[tag] = 1
                    else:
                        hash_dict[tag] += 1
    
    return hash_dict

if __name__ == '__main__':
    tweet_file = open(sys.argv[1])

    term_count_dict = term_count(tweet_file)

    total_words = sum(term_count_dict.values())

    top_list = sorted(term_count_dict, key=term_count_dict.get, reverse=True)[0:10]
    for hastag in top_list:
        print hastag, term_count_dict[hastag]

