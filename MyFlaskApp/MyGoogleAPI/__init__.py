
class MyGoogleAPI:
    def __init__(self, api_key):
        """
        Inits a service connection.
        :param api_key: api_key
        """
        from googleapiclient.discovery import build
        service = build('plus', 'v1', developerKey=api_key)
        self.people_resource = service.people()

    def get(self, id):
        """
        Gets user description.
        :param id: user id
        :return: user descriptions
        """
        return self.people_resource.get(userId=id).execute()

    def search(self, query, max_results=10):
        """
        Perform a search.
        :param query: query
        :param max_results: result count
        :return: user ids
        """
        return self.people_resource.search(maxResults=max_results, query=query).execute()
