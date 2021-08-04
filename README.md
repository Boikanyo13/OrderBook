# OrderBook

## Reflect and comment on performance aspects. If not implemented, what could be done to improve performance? 
## Reflect and comment on data consistency if a multithreaded approach is used for processing the order flow.

# Answer:
## Performace of the code is slow relative to the amount of data in the orders.xml file since each order waits for the previous one to complete the process before it is executed. The performance of the code can be improved using multi-threading. 

## Multi-threading should only be used per book rather than having multiple threads in one book. The consequences of using multiple threads in one book will result in some orders to miss matches and thus causing a delay in some transactions.
