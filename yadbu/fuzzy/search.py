import operator 

words_dict = {}
word_counts = {}

def parse_tsv(filename):
    word_count = {}
    words = []
    with open(filename) as dataset:
        for row in dataset:
            word, frequency = row.split('\t')                               #splitting it into word and occurence frequency
            word_count[word] = int(frequency.strip())               #inserting into the wordcount dictionary key as word and value as frequency
            words.append(word)
    return words, word_count

words, word_count = parse_tsv('fuzzy/tsv/schema.tsv')
words_dict[''] = words
word_counts[''] = word_counts

for i in words:
    words, word_count = parse_tsv('fuzzy/tsv/%s.tsv' % i)
    words_dict[i] = words
    word_counts[i] = word_count

def print_dict(key):
    print(words_dict[key])

def search(key, incomplete_word):
    if key not in words_dict:
        return []
    result = []
    for word in words_dict[key]:
        if incomplete_word in word:
            result.append(word)
    return result

def sort(key, results, incomplete_word):
    if key not in word_counts:
        return []
    result_a = [(result, result.find(incomplete_word), word_counts[key][result], len(result)) for result in results]
    result_a.sort(key=operator.itemgetter(1))
    result_a.sort(key=operator.itemgetter(3))

    search_results = [result_distance[0] for result_distance in result_a][:25]

    return search_results

