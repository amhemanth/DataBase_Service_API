# DataBase_Service_API
An API to store and retrieve data from  Mongo db.

## Resource method Chart:
|Resource|Address|Protocol|Parameters|Status Code|
|--------|-------|--------|----------|-----------|
|Register|/register|POST|username,<br> password|200:ok|
|store sentence|/store|POST|username,<br> password,<br> Sentence|200:ok,<br> 301:out of tokens,<br> 302: invalid pass or user|
|Retreve sentence|/get|POST|username,<br>password|200:ok,<br>301:out of tokens,<br>302:Invalid user or pass|

**An Api with restful services**
