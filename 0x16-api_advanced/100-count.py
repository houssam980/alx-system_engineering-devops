#!/usr/bin/python3
""" Module of counting """
from requests import get


def count_words(subreddit, word_list, word_count=[], page_after=None):
    headers = {'User-Agent': 'HolbertonSchool'}
    word_list = [word.lower() for word in word_list]

    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        ref = get(url, headers=headers, allow_redirects=False)
        if ref.status_code == 200:
            for child in ref.json()['data']['children']:
                iter = 0
                for iter in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[iter] == word:
                            word_count[iter] += 1
                    iter += 1

            if ref.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, ref.json()['data']['after'])
    else:
        url = ('https://www.reddit.com/r/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))
        ref = get(url, headers=headers, allow_redirects=False)

        if ref.status_code == 200:
            for child in ref.json()['data']['children']:
                iter = 0
                for iter in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[iter] == word:
                            word_count[iter] += iter
                    iter += 1
            if ref.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, ref.json()['data']['after'])
            else:
                dicto = {}
                for key_word in list(set(word_list)):
                    iter = word_list.index(key_word)
                    if word_count[iter] != 0:
                        dicto[word_list[iter]] = (word_count[iter] *
                                               word_list.count(word_list[iter]))

                for key, value in sorted(dicto.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(key, value))
