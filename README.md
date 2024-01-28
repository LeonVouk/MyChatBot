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


# Forms
***
To incorporate forms the scenarios changed to be more formulaic and ask for the user's
account early on in the stories. A slot was created to store the account name extracted by the form. An account name 
is given, which in the future would be extracted from the input and compared with a database,
and in return the bot affirms that the account has been found and asks for the user's issue.

In the event that a different path is taken while the form is being handled, in this situation a token question is used
of asking the bot if it's a bot. The bot answers the question and then returns to inquiring about the user's account.


# Policies
### RulePolicy
The rule policy works best when we need the bot to behave in a specific manner no matter what has happened in the
conversation up to this point. Using the policy alone completely breaks our chat bot since we've only implemented 
rules that cover the ending of the conversation and the handling of account names. The RulePolicy can work really well
in combination with other policies to take care of situations where specific information is needed for the conversation
to continue correctly.

## MemoizationPolicy
The memoization policy works by leveraging the history of the current conversation to make predictions based on exact
matches in the data the bot was trained on. The policy works flawlessly when encountering an input that can be found in
the intents e.g "I would like to terminate my account please", but fails when a variation is given which has the same
meaning e.g "I am done with your company.".

## TEDPolicy
As this policy uses a transformer model to predict the next action of the bot, the prediction is done based on the
extracted context and natural language understanding of the underlying model. It doesn't seem to really fail at any task,
but the excess training time and complexity added by the TED policy is lost when following formulaic paths, as one can
find in the help required in our three stories. That being the case, the second there is any deviation from the examples
seen, the TEDPolicy greatly outperforms the MemoizationPolicy, making it a staple in our model. Another caveat is that
extracting forms and slots from inputs, is much more consistent and efficient with the RulePolicy, rather than the
TEDPolicy, meaning that in that account, the TEDPolicy does get outperformed.

## Our Implementation
We implement a combination of the RulePolicy and TEDPolicy to take care of different abilities of our chatbot.
The TEDPolicy takes care of the next action prediction and NLU of the user's intents and the RulePolicy leverages that
and helps with extracting the required slots, handling the forms and providing the formulaic response that is required
at points during the conversation of a user with an agent.


# Future
The bot needs to have access to a database with the customer information and be able to retrieve
the customer accounts with their relevant information.

It needs to be able to extract that information from the text/call. That can happen either through
explicit assignment (as would happen with an account number) or by using a language model to extract
information from the callers intent. Using that information the bot, again through the use 
of a language model needs to be able to help the caller out with any tasks that don't require a human
in the loop.