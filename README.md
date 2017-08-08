# Python logging handlers

## Cisco Spark

### Requirements

At the moment you will need to know the roomId of the room you want to receive messages.  

### Usage

When creating a new handler instance you must pass the desired API key and roomId.  To indicate if your messages are plain text you should also pass 'text' to the constructor as the keyword argument 'msg_type', otherwise it will be assumed that your message is in acceptable markdown format.  You may also pass the logging level as with other logging handlers.

```python
import logging
from loghandlers import SparkHandler

log = logging.getLogger()
spark = SparkHandler('YOUR KEY GOES HERE', 'YOUR ROOMID GOES HERE', msg_type='markdown', level=logging.WARN)
log.addHandler(spark)
```

### NOTE

This software is untested and while I have no reason to believe that your messages will end up anywhere other than where you intended, I can't rule it out either.  This software is provided as-is with no warranty.
