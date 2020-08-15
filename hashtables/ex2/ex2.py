#  Hint:  You may not need all of these.  Remove the unused functions.




class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


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

tickets_dict = {}

def create_table():
    for ticket in tickets:
        tickets_dict[ticket.source] = ticket.destination

create_table()

print(tickets_dict)

route = []

# print(route)


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
   
    start = tickets_dict['NONE']
    route.append(start)

    next = None

    for _ in range(1,9):
        
        next = tickets_dict[route[-1]]
        route.append(next)

   

                    


        
    print(f'route = {route}')
  


        
        
    
   

reconstruct_trip(tickets,10)



