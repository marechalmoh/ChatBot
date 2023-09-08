# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# #
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

# class DemanderNomProduit(Action):
#     def name(self) -> Text:
#         return "action_demander_nom_produit"
    
#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


#         dispatcher.utter_message(text="Hello World!")

#         return []
    
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction, FormAction

class DemanderInfosProduitsForm(FormAction):
    def name(self) -> Text:
        return "action_formulaire_demander_infos_produit"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["produit", "categorie", "marque", "taille", "date", "promotion"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "produit": self.from_entity(entity="produit", intent="demander_infos_produits"),
            "categorie": self.from_entity(entity="categorie", intent="demander_infos_produits"),
            "marque": self.from_entity(entity="marque", intent="demander_infos_produits"),
            "taille": self.from_entity(entity="taille", intent="demander_infos_produits"),
            "date": self.from_entity(entity="date", intent="demander_infos_produits"),
            "promotion": self.from_entity(entity="promotion", intent="demander_infos_produits"),
        }

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        # Vous pouvez implémenter une validation personnalisée ici si nécessaire.
        # Par exemple, vérifier si le produit est disponible dans la catégorie spécifiée.
        # Si la validation échoue, renvoyez un SlotSet avec la valeur None pour le slot en question.
        return []

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # Une fois que tous les slots requis sont remplis, vous pouvez effectuer des actions ici.
        # Par exemple, interroger une base de données pour obtenir des informations sur le produit.
        return []

class ActionDemanderInfosProduits(Action):
    def name(self) -> Text:
        return "action_demander_infos_produits"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        produit = next(tracker.get_latest_entity_values("produit"))
        taille = next(tracker.get_latest_entity_values("taille"))
        categorie = next(tracker.get_latest_entity_values("categorie"))
        couleur = next(tracker.get_latest_entity_values("couleur"))
        
        message = f"PRODUIT : {produit}, TAILLE : {taille}, CATEGORIE : {categorie}, COULEUR : {couleur}"
        dispatcher.utter_message(text=message)
        
        return []


