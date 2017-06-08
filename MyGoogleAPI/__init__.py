
class MyGoogleAPI:
    def __init__(self, api_key):
        """

        :param api_key:
        """
        from googleapiclient.discovery import build
        service = build('plus', 'v1', developerKey=api_key)
        self.people_resource = service.people()

    def get(self, id):
        """

        :param id:
        :return:
        """
        return self.people_resource.get(userId=id).execute()

    def search(self, query, max_results=10):
        """

        :param query:
        :param max_results:
        :return:
        """
        return self.people_resource.search(maxResults=max_results, query=query).execute()
