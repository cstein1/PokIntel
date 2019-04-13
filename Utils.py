def window(iterator, window_width):
    inds = [[a for a in range(i-window_width,i)] for i in range(window_width, len(iterator)+1)]
    return [tuple([iterator[i] for i in ind]) for ind in inds]

def last_occ(itr, itm):
  return ''.join(str(i) for i in itr).rindex(str(itm))
