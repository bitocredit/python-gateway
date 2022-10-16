import requests


class BitocreditApi:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.header = {
            "Content-Type": "application/json",
        }

    # create wallet method

    def createWallet(self, wallet_id , network):
        return self.__request("create/wallet", "post", {"wallet_id": wallet_id , "network": network}, True)

    # transaction check method

    def transactionCheck(self, transaction_id, wallet_address):
        return self.__request("transaction/check", "post", {"transaction_id": transaction_id, "wallet_address": wallet_address}, True)

    # transaction recovery method

    def transactionRecovery(self, transaction_id):
        return self.__request("transaction/recovery", "post", {"transaction_id": transaction_id}, True)

    # transaction fee method

    def transactionFee(self):
        return self.__request("transaction/fee", "get", {}, True)

    # transaction example method

    def transactionExample(self, transaction_id):
        return self.__request("transaction/example/callback", "post", {"transaction_id": transaction_id}, False)

    def __request(self, path, method, params={}, auth=False):

        fullURL = self.base_url + path

        if auth:
            fullURL = fullURL + "/" + self.token

        try:
            if (method == "get"):
                response = requests.get(fullURL, params, headers=self.header)
            elif (method == "post"):
                response = requests.post(
                    fullURL, json=params, headers=self.header)
            else:
                raise Exception("wrong method!")

            return response.json()

        except Exception as err:
            return err
