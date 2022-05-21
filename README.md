# p-club-summer-project-recruitment-task
Deep dive into web3.0 recruitment task

# Program for Loaning service using OOP concepts

The program emulates a loaning service which allows the user to lend/borrow to/from other registered users<br/>
An object of the "Bank" class is used to keep record of the registered members and their transactions (in the variables members and \_ledger)<br/>
Whenever a user wants to lend/borrow, it acts like an object of the lender or borrower class
which both are the children of the bank class.<br/>
An analogy can be given that the lender and borrower objects act like clerks in the bank that manage individual loans and the bank object acts like an overall bookeeper that records the history of each transaction.<br/>

Note- To run the program, download the .exe file and run it. Instructions on various tasks will be printed at the start<br/>
Make sure to register user before performing any other task<br/>
An example run is shown below


![image](https://user-images.githubusercontent.com/51286478/169633642-5c323b9a-32ab-497d-b197-63c84d08e56d.png)


# Is this an example of centralized or decentralized system? 

This is an example of a centralized loan system as the bank object keeps track of all transactions and does not share the whole ledger with anyone (only the users own transaction history can be seen). It also keeps track of the members i.e who can give/take a loan and who cannot.

# Demerits of a centralized system

1.Since a centralized authority controls the money, corruption is easy<br/>
2.No privacy from the authority since it can access all records<br/>
3.Any failure at the central level will result in a collapse of the entire system.eg- case of Nirav Modi, Vijay Mallya etc.<br/>
4.Any decision taken by the authority will be binding and hard to change.<br/>
5.The authority might charge a high transaction fee that will be non negotiable.<br/>
6.If the services provided by the central authority are sloppy you have no real alternative. eg-huge paperwork for small errands, long waiting periods etc.




