# ROT26

Two times better than ROT13!

Secure your message by using the endpoint:
```
/api/rot26/<message>
```
Returns:
```
{
  "result": "superencryptedmessage"
}
```


##### With Docker
```
docker build -t rot26 --rm .
docker run -p 5000:5000 rot26 --rm
```

##### Without Docker
```
pip3 install -r requirements.txt
python3 rot26.py
```