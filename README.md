<h3 align="center" >Bitocredit python package</h3>
<h5>python wrapper for Bitocredit API</h5>

# usage
install package using pip
<br>
<br>
```bash
pip install pythonGateway
```

<br>
<br>

and use package like this:

```python
    from pythonGateway.Api import BitocreditApi
    
    baseurl = "https://bitocredit.com/api/";
    token = "TOKEN"; # fill your token
    
    Api = BitocreditApi(baseurl , token);
    
    res = Api.createWallet("1")  # replace wallet_id with your wallet id
    print(res)

```

# methods

- [createWallet](#createwallet)
- [transactionCheck](#transactioncheck)
- [transactionRecovery](#transactionrecovery)
- [transactionFee](#transactionfee)
- [transactionExample](#transactionexample)


# <a id="createwallet">createWallet</a>

This method used for creating wallet for user
<br>
<br>
endpoint : https://bitocredit.com/api/create/wallet/{token}
<br>
<br>

```python
    res = Api.createWallet("1")  # replace wallet_id with your wallet id
    print(res)
    
```

# <a id="transactioncheck">transactionCheck</a>

This method used for check a transaction is confirmed or not
<br>
<br>
endpoint : https://bitocredit.com/api/transaction/check/{token}
<br>
<br>

```python 
    res = Api.transactionCheck("transaction_hash" , "wallet_address") # replace transaction_hash and wallet_address with your transaction hash and wallet address
    print(res)

```

# <a id="transactionrecovery">transactionRecovery</a>

This method used for check a transaction that is lost in blockchain
<br>
<br>
endpoint : https://bitocredit.com/api/transaction/recovery/{token}
<br>
<br>

```python 
    res = Api.transactionRecovery("transaction_hash")  # replace transaction_hash with your transaction hash
    print(res)

```


# <a id="transactionfee">transactionFee</a>

This method used for check a transaction that is lost in blockchain
<br>
<br>
endpoint : https://bitocredit.com/api/transaction/fee/{token}
<br>
<br>

```python
    res = Api.transactionFee()
    print(res)

```


# <a id="transactionexample">transactionExample</a>

Please only use this api for test ! it's only an example to show how the server sends data to callback after payment confirmation
<br>
<br>
endpoint : https://bitocredit.com/api/transaction/example/callback
<br>
<br>

```python 
    res = Api.transactionExample("transaction_hash") # replace transaction_hash with your transaction hash
    print(res)

```