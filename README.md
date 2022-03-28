# blocek2csv

live: [link to live preview](https://blocek2csv.herokuapp.com/)

Aplikacia nacita data z blocka a vyexportuje data do CSV formatu


site down:
```
2022-03-26T08:41:26.124887+00:00 app[web.1]: [2022-03-26 08:41:26 +0000] [10] [INFO] Worker exiting (pid: 10)
2022-03-26T08:41:26.124952+00:00 app[web.1]: [2022-03-26 08:41:26 +0000] [4] [INFO] Handling signal: term
2022-03-26T08:41:26.325636+00:00 app[web.1]: [2022-03-26 08:41:26 +0000] [4] [INFO] Shutting down: Master
2022-03-26T08:41:26.472217+00:00 heroku[web.1]: Process exited with status 0
2022-03-27T19:24:18.068268+00:00 heroku[router]: at=info code=H82 desc="Free app running time quota exhausted" method=GET path="/" host=blocek2csv.herokuapp.com request_id=e94c4520-fdb3-444d-860a-bbbe5f22b4e0 fwd="69.63.184.3" dyno= connect= service= status=503 bytes= protocol=https
2022-03-27T19:24:18.082491+00:00 heroku[router]: at=info code=H82 desc="Free app running time quota exhausted" method=GET path="/" host=blocek2csv.herokuapp.com request_id=9d9c5c1a-456f-4431-8b3f-68b91cb7f7c7 fwd="69.63.184.7" dyno= connect= service= status=503 bytes= protocol=https
2022-03-27T19:24:21.922564+00:00 heroku[router]: at=info code=H82 desc="Free app running time quota exhausted" method=GET path="/" host=blocek2csv.herokuapp.com request_id=64d314f9-50fe-415b-a6b7-0654dddcd319 fwd="69.63.184.2" dyno= connect= service= status=503 bytes= protocol=https
2022-03-28T01:11:12.057112+00:00 heroku[router]: at=info code=H82 desc="Free app running time quota exhausted" method=GET path="/" host=blocek2csv.herokuapp.com request_id=d382ead6-47c9-4320-8358-a6b75819530b fwd="173.252.95.119" dyno= connect= service= status=503 bytes= protocol=https
2022-03-28T05:54:33.892505+00:00 heroku[router]: at=info code=H82 desc="Free app running time quota exhausted" method=GET path="/" host=blocek2csv.herokuapp.com request_id=3f5c0877-d3c6-4d05-add6-af6b24e2304b fwd="188.167.250.145" dyno= connect= service= status=503 bytes= protocol=https
2022-03-28T05:54:35.417744+00:00 heroku[router]: at=info code=H82 desc="Free app running time quota exhausted" method=GET path="/favicon.ico" host=blocek2csv.herokuapp.com request_id=01095e1a-7056-4b18-8689-7e878a9dc6d3 fwd="188.167.250.145" dyno= connect= service= status=503 bytes= protocol=https
```

očividne koncom mesiaca sa mi minie povolený free limit na "dyno hours" a stránka je down. Ale len do konca mesiaca, od prvého by to malo automaticky fungovať.
