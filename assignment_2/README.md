# Assignment 2: METACOIN

Metacoin implements a simple loan and credit contract using solidity.
The address deploying the contract is considered owner of the account and can therefore use functions veiwdues(to veiw loan pending for a specific creditor) and 
settledues(to settle his dues to the creditor)
Functions can be tested using two test accounts on remix, one acting as owner the other as creditor.

![image](https://user-images.githubusercontent.com/51286478/175783589-699140de-6e82-4d22-a49e-ae898ab1e2f0.png)

Here address 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4 is of the owner.
Next let us use another address to request loan payment from the owner.
![image](https://user-images.githubusercontent.com/51286478/175783677-22830e35-d298-4151-b27b-c1b8445765f0.png)

On the owner side, the pending dues is updated

![image](https://user-images.githubusercontent.com/51286478/175783728-2d614cd1-c5d8-401b-95f6-a5ae1741aa0b.png)

Now, we can pay these dues by using settle dues, after which the pending dues will change to 0.

![image](https://user-images.githubusercontent.com/51286478/175783793-2fafc258-6dbc-470a-b9a1-c883170a0c7d.png)
