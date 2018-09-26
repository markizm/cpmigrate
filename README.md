### Catchpoint Test Migration, used for promoting tests from non-prod divisions 

Official API Docs: https://io.catchpoint.com/ui/help

Description: Script to migrate tests from/to different divisions

#### Maintainer

Mark Magaling - magaling.markizm@gmail.com

### Usage:
.app.py -t {testid} -d {client}

##### TestIDs appear in the test properties, centered at top of the page
##### Available divisions for migrate tests to:

"client" = client division 

"nonprod" = non-prod division 

"consumer" = consumer division    


### Example
##### Add testid 212779 to client division:
$ .app.py -t 212779 -d client

### Notes

Uses OAUTH2.0 framework for authentication 

Written in Python 2.7 

##test
