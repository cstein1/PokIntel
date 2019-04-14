def window(iterator, window_width):
    '''
    Creates a new iterator from in iterator that provides lists of length window_width
    window([1,2,3,4,5], 3) = [(1,2,3),(2,3,4),(3,4,5)]
    '''
    inds = [[a for a in range(i-window_width,i)] for i in range(window_width, len(iterator)+1)]
    return [tuple([iterator[i] for i in ind]) for ind in inds]

def last_occ(itr, itm):
    '''Returns the index of the last occurance of an object'''
    return ''.join(str(i) for i in itr).rindex(str(itm))

def filter_ind(itr, cond):
    '''
    cond is function that takes the iterator
    Grabs index of items that would survive the filter condition
    '''
    # cond is function that takes the iterator
    inds = []
    for ind, i in enumerate(itr):
        if cond(i):
