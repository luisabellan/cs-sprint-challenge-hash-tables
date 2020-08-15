#  Hint:  You may not need all of these.  Remove the unused functions.




class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination




tickets_dict = {}

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    for ticket in tickets:
        tickets_dict[ticket.source] = ticket.destination
   
    start = tickets_dict['NONE']
    route.append(start)

    next = None

    for _ in range(1,length):
        
        next = tickets_dict[route[-1]]
        route.append(next)

    
        
    #print(f'route = {route}')
    return route

    
""" 

# test short case
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets,len(tickets))

# test long case
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

reconstruct_trip(tickets,len(tickets)) """




