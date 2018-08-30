import re
import collections

def get_stats(vocab):
    """For the given merge step, get the bigram counts, for every pair of symbols (strings).

    For each word and its freq in the corpus, add the number of instances for each of its subword parts.
    """
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    """Merge the vocab, adding in the new pair. """
    v_out = {}
    bigram_pattern = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram_pattern + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def byte_pair_encoding(vocab, num_merges=5):
    """For the given number of merges, find the most common pairs of symbols. 
    """
    for _ in range(num_merges):
        pairs = get_stats(vocab)
        best = max(pairs, key=pairs.get)
        if pairs[best] < 2:
            print('no pair has frequency > 1. Stopping\n')
            break
        vocab = merge_vocab(best, vocab)
    print(vocab)

vocab = {
  'l o w </w>' : 5, 
  'f a r t h e s t </w>' : 5,
  'n e w e r </w>': 5,
  'w i d e r </w>': 5 }
byte_pair_encoding(vocab)