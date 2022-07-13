from rasa_sdk.events import AllSlotsReset , SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from sanic import request
from sanic.request import Request

        
class ActionNome(Action):

    def name(self) -> Text:
        return "action_retorno"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:
        
        retorno = tracker.get_slot('retorno')
        print(f'RETORNO: {retorno}')
        retorno = True
        
        return [SlotSet("retorno", retorno)]
