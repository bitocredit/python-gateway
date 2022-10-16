from ast import Str
import unittest
from pythonGateway.Api import BitocreditApi

class TestApi(unittest.TestCase):

    BASE_URL = ""
    TOKEN = ""
    TRANSACTION_ID = ""
    WALLET_ADDRESS = ""
    
    def setUp(self):
        self.header = {
            "Content-Type": "application/json",
        }
        self.api = BitocreditApi(self.BASE_URL , self.TOKEN)
    
    def test_createWallet(self):
        res = self.api.createWallet("1" , "tron")
        self.assertEqual(res['status'] , 200)
        self.assertEqual(res['message'] , "ok")

    def test_transactionCheck(self):
        res = self.api.transactionCheck(self.TRANSACTION_ID , self.WALLET_ADDRESS);
        self.assertEqual(res['status'] , 200)

    def test_transactionRecovery(self):
        res = self.api.transactionRecovery(self.TRANSACTION_ID);
        self.assertEqual(res['status'] , 200)

    def test_transactionFee(self):
        res = self.api.transactionFee();
        self.assertEqual(res['status'] , 200)

    def test_transactionExample(self):
        res = self.api.transactionExample(self.TRANSACTION_ID);
        self.assertEqual(res['status'] , 200)
