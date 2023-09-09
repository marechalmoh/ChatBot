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
#         return "action_demander_nom_produits"
    
#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


#         dispatcher.utter_message(text="Hello World!")

#         return []
    
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormValidationAction, FormValidationAction


#
#DEMANDER INFOS PRODUITS
#
class DemanderInfosProduitsForm(FormValidationAction):
    def name(self) -> Text:
        return "action_formulaire_demander_infos_produits"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["produit", "categorie", "marque", "taille", "date"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "produit": self.from_entity(entity="produit", intent="demander_infos_produits"),
            "categorie": self.from_entity(entity="categorie", intent="demander_infos_produits"),
            "marque": self.from_entity(entity="marque", intent="demander_infos_produits"),
            "taille": self.from_entity(entity="taille", intent="demander_infos_produits"),
            "date": self.from_entity(entity="date", intent="demander_infos_produits")
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

#
#DEMANDER PRIX PRODUITS
#
class DemanderPrixProduitsForm(FormValidationAction):
    def name(self) -> Text:
        return "action_formulaire_demander_prix_produits"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["produit, prix"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "produit": self.from_entity(entity="produit", intent="demander_prix_produits"),
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

class ActionDemanderPrixProduits(Action):
    def name(self) -> Text:
        return "action_demander_prix_produits"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        produit = next(tracker.get_latest_entity_values("produit"))
        prix = next(tracker.get_latest_entity_values("prix"))
        
        message = f"PRODUIT : {produit}, PRIX : {prix}" 
        return []
    
#
#DEMANDER DISPONIBILITE PRODUITS
#
class DemanderDisponibiliteProduitsForm(FormValidationAction):
    def name(self) -> Text:
        return "action_formulaire_demander_disponibilite_produits"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["produit"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "produit": self.from_entity(entity="produit", intent="demander_disponibilite_produits")
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

class ActionDemanderDisponibiliteProduits(Action):
    def name(self) -> Text:
        return "action_demander_disponibilite_produits"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        produit = next(tracker.get_latest_entity_values("produit"))
        
        message = f"PRODUIT : {produit},"
        dispatcher.utter_message(text=message)
        
        return []

#
#DEMANDER DETAILS PRODUITS
#
class DemanderDetailsProduitsForm(FormValidationAction):
    def name(self) -> Text:
        return "action_formulaire_demander_details_produits"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["produit"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "produit": self.from_entity(entity="produit", intent="demander_details_produits")
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

class ActionDemanderDetailsProduits(Action):
    def name(self) -> Text:
        return "action_demander_details_produits"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        produit = next(tracker.get_latest_entity_values("produit"))
        
        message = f"PRODUIT : {produit},"
        dispatcher.utter_message(text=message)
        
        return []
    
#
#DEMANDER DATE DISPONIBILITE
#
class DemanderDateDisponibiliteForm(FormValidationAction):
    def name(self) -> Text:
        return "action_formulaire_demander_date_disponibilite"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["produit"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "produit": self.from_entity(entity="produit", intent="demander_date_disponibilite")
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

class ActionDemanderDateDisponibilite(Action):
    def name(self) -> Text:
        return "action_demander_date_disponibilite"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        produit = next(tracker.get_latest_entity_values("produit"))
        
        message = f"PRODUIT : {produit},"
        dispatcher.utter_message(text=message)
        
        return []
    
#
#DEMANDER ACHAT PRODUITS
#
class DemanderAchatProduitsForm(FormValidationAction):
    def name(self) -> Text:
        return "action_formulaire_demander_achat_produits"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["produit"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "produit": self.from_entity(entity="produit", intent="demander_achat_produits")
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

class ActionDemanderAchatProduits(Action):
    def name(self) -> Text:
        return "action_demander_achat_produits"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        produit = next(tracker.get_latest_entity_values("produit"))
        
        message = f"PRODUIT : {produit},"
        dispatcher.utter_message(text=message)
        
        return []