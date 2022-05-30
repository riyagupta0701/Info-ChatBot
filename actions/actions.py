# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class InfoForm(FormAction):

    def name(self):
        return "info_form"

    def required_slots(tracker):
        return ['name', 'email', 'company', 'job_title']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": [
                self.from_entity(entity='name'),
                self.from_intent(intent='affirm', value=True)
            ],
            "email": [
                self.from_entity(entity='email'),
                self.from_intent(intent='affirm', value=True)
            ],
            "company": [
                self.from_entity(entity='company')
            ],
            "job_title": [
                self.from_entity(entity='job_title')
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []
        
# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
