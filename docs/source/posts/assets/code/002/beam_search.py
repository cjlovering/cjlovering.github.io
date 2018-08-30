import torch
import heapq
from torch.autograd import Variable

from collections import namedtuple
Beam = namedtuple('Beam', ['ys', 'log_prob_seq'])

def beam_search_decode(model, src, src_mask, max_len, start_symbol, beam_count=3):
    """Basic beam search decode function. (Untested).
    """
    memory = model.encode(src, src_mask)
    candidates = [ Beam(torch.ones(1, 1).fill_(start_symbol).type_as(src.data), 0) ]
    # generate a word up to the max length. the system could represent stop symbols to stop early.
    for i in range(max_len-1):
        # for each path, operate on that path (autoregressive).
        outputs = [
            model.decode(
                memory,
                src_mask,
                Variable(c.ys),
                Variable(c.ys.size(1)).type_as(src.data))
            for c in candidates
        ]
        # select the most probable words
        results = []
        for out in outputs:
            # generate a probability distribution over the possible output symbols.
            dist = model.generator(out[:, -1])
            # look at the top beam_count possibilities in each path.
            for _ in range(beam_count):
                prob, next_word = torch.max(dist, dim = 1)
                log_prob = torch.log(prob)
                next_word = next_word.data[0]
                dist[next_word] = -1e9 # zero out.
                ys = torch.cat([out.ys, torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=1)
                log_prob_seq = out.log_prob_seq + log_prob
                results.append(Beam(ys, log_prob_seq))
        candidates = heapq.nlargest(beam_count, results, key=lambda b: b.log_prob_seq)
    return ys