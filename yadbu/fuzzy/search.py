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

words, word_count = parse_tsv('fuzzy/tsv/schema.tsv') #parse the schema first (column headers)
words_dict[''] = words #a dictionary with a single list of all the words
word_counts[''] = word_count #a dictionary of dictionaries with words matched up to how many times they were counted

for i in words:
    words, word_count = parse_tsv('fuzzy/tsv/%s.tsv' % i) #parse each word (every row)
    words_dict[i] = words            
    word_counts[i] = word_count
    #create a dictionary of the space:schema, column header:row headers
    #create a dictionary of words and their counts

def search(key, incomplete_word):
    if key not in words_dict:
        return []
    result = []
    for word in words_dict[key]: #key is the column header. So iterating over rows of a column header
        if incomplete_word in word:
            result.append(word) #if part of one of the rows of a particular column header is found, fill list
    return result

def sort(key, results, incomplete_word):
    if key not in word_counts:
        return []
    result_a = [(result, result.find(incomplete_word), word_counts[key][result], len(result)) for result in results]
    result_a.sort(key=operator.itemgetter(1))
    result_a.sort(key=operator.itemgetter(3)) #preference given to incomplete_word being at the beginning and short words

    search_results = [result_distance[0] for result_distance in result_a][:25] #pass back first 25 result from result_a

    return search_results

