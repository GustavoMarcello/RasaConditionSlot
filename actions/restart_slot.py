from rasa_sdk.events import AllSlotsReset, SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction


class ActionOtherConsult(Action):

    def name(self) -> Text:
        return "action_restart_slot"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:
        
        # coleta variável de fluxo para verificação
        flow = tracker.get_slot('flow')
        print(f'FLOW: {flow}')
        
        return [AllSlotsReset(), SlotSet("retorno", True),FollowupAction(name="utter_slot")]

        