import threading
import random
import time
thread_id = 1
ticketsAvailable = 2
lst_seats_available = list(range(1, ticketsAvailable + 1))
empty_lst = []
boolean = [True, False]


class Customer(threading.Thread):
    ticketsSold = 0

    def __init__(self):
        threading.Thread.__init__(self)
        global thread_id
        self.name = thread_id
        thread_id += 1
        print('Customer {} buying ticket \n'.format(self.name))

    def run(self):
        global lst_seats_available
        global max_seats
        global empty_lst
        global ticketsAvailable
        global boolean
        running = True
        print('The following tickets are available: ' +
              str(lst_seats_available) + '\n')
        while running:
            self.randomDelay()
            if ticketsAvailable == 0:
                running = False
                print('No more tickets available for Customer {} \n'.format(self.name))

            else:
                index_rand = random.randint(0, len(lst_seats_available) - 1)
                x = lst_seats_available[index_rand]
                if x not in empty_lst:
                    empty_lst.append(x)
                    print('Ticket {} is in the basket for Customer {} \n'.format(
                        x, self.name))
                    time.sleep(1)
                    ticket_bought = boolean[random.randint(0, 1)]
                    if ticket_bought:
                        lst_seats_available.remove(x)
                        print('Ticket {} succesfully booked for Customer {} \n'.format(
                            x, self.name))
                        ticketsAvailable -= 1
                        print('There is ' + str(ticketsAvailable) +
                              ' ticket left \n')
                        self.ticketsSold = self.ticketsSold + 1
                        running = False
                    else:
                        print('Seat {} expired for Customer {}'.format(x, self.name))
                        empty_lst.remove(x)

                else:
                    print('Ticket {} is no longer available for Customer {} \n'.format(
                        x, self.name))

    def randomDelay(self):
        time.sleep(1)


customers = []
for i in range(3):
    customer = Customer()
    customer.start()
    customers.append(customer)
# joining all our customers
for customer in customers:
    customer.join()
