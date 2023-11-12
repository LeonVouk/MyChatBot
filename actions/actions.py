# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import random


class ActionCheckAccount(Action):

    def name(self) -> Text:
        return "action_check_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        available_subscriptions = ['mobile', 'tv', 'internet']
        rand_int = random.randint(1, 3)
        subs = random.sample(available_subscriptions, rand_int)
        dispatcher.utter_message(text=f"I see that your account contains "
                                      f"the following subscriptions: {', '.join(subs)}. "
                                      f"Where would the problem be?")

        return []

class ActionAskIssue(Action):

    def name(self) -> Text:
        return "action_ask_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        target_facility = tracker.get_slot('facility')
        available_subscriptions = ['mobile', 'tv', 'internet']
        if target_facility in available_subscriptions:
            message = f"Thank you for your help, what might be the problem with your {target_facility}"
        else:
            message = (f"I'm sorry as I said earlier I can't see a subscription for {target_facility} in your account, "
                       f"have you given me the correct account info?")
        dispatcher.utter_message(text=message)
        return []


class ActionFindAccountBalance(Action):

    def name(self) -> Text:
        return "action_find_account_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        balance = random.random() * 100
        dispatcher.utter_message(text=f"It seems that you owe {balance} euros.")

        return []
