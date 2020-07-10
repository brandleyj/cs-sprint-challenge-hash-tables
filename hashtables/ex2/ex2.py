#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
     
    cache = {}

    for i in tickets:
        cache[i.source] = i.destination

    route = []

    for k, v in cache.items():
        if k == "NONE":
            route.append(v)

    ticket_complete = False

    while not ticket_complete:
        prev_stop = route[-1]

        if prev_stop in cache.keys():
            route.append(cache[prev_stop])
        
        if prev_stop == "NONE":
            ticket_complete = True

    return route[:length]