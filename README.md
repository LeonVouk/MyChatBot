# MyChatBot
***
Chat bot initial implementation

# Domain
***
The chat bot is created for the **telecommunications** domain, specifically as an assistant to answer
as many answers and possible and/or route the customers to the correct department.

It's a sector where many needs of callers can be automatically taken care of and the only user identification
needed for most actions is an internal account ID, meaning that the bot can handle most of the authentication
without any compromise to the caller.
***
***


### Scenario 1
***
A caller has an issue with one of the modalities of their subscription. e.g Internet, TV, Mobile
The bot needs to be able to 
1) Identify the reason of the callers call
2) Identify if the caller has an account. If yes, find which account
3) Recover and return the running subscriptions of this account
4) Ask about the issue, understand it and route it to the correct technical team


### Scenario 2
***
A caller wants to check their account balance.
The bot needs to be able to 
1) Identify the reason of the callers call
2) Identify if the caller has an account. If yes, find which account
3) Access the payment information and retrieve the balance

The caller may try to dispute their balance based on their last transaction
4) Ask for their last transaction number
5) Retrieve said information, if it exists.
6) "Judge" if payment was done
7) Route the caller to the accounting team if there are discrepancies, for further investigation.


### Scenario 3
***
A caller wants to terminate their contract
The bot needs to be able to 
1) Identify the reason of the callers call
2) Identify if the caller has an account. If yes, find which account
3) Ask and log information on why the caller wants to terminate the contract.
4) Give the caller a discount, so as to keep them with the firm.
5) Log the transaction and terminate the contract if the caller insists.

***
***

# Future
The bot needs to have access to a database with the customer information and be able to retrieve
the customer accounts with their relevant information.

It needs to be able to extract that information from the text/call. That can happen either through
explicit assignment (as would happen with an account number) or by using a language model to extract
information from the callers intent. Using that information the bot, again through the use 
of a language model needs to be able to help the caller out with any tasks that don't require a human
in the loop.