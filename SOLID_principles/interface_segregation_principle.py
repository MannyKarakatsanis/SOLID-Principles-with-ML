"""
    SOL>I<D 
    I = interface segregation principle.

    definition:
    "Client code shouldn't depend on methods it doesn't use." 
"""


from abc import abstractmethod, ABC

class ItemRecommender(ABC):

    @abstractmethod
    def get_closest_items(self, item):
        pass


class PersonalisedRecommender(ABC):

    @abstractmethod
    def get_personalised_recommendations(self, user):
        pass


class CollaborativeFilteringRecommender(ItemRecommender, PersonalisedRecommender):

    def get_closest_items(self, item):
        print("Recommended closest items")

    def get_personalised_recommendations(self, user):
        print("Provided personalised recommendations")


class DLRecommender(ItemRecommender, PersonalisedRecommender):

    def get_closest_items(self, item):
        print("Recommended closest items")

    def get_personalised_recommendations(self, user):
        print("Provided personalised recommendations")


class NearestNeighbourRecommender(ItemRecommender):

    def get_closest_items(self, item):
        print("Recommended closest items")
