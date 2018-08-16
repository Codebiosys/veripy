Logs and Logging
================

VeriPy leverages behave's logging to provide rich details about the exact actions being performed by the statements.

The logging is configured in `settings.py`. By default the logging system will output any messages of `INFO` level or higher. Because behave reports its results to the console, the logs are written by default to `veripy.log`.

Once the tests are running simply run the following command to see the logs:

```bash
tail -f veripy.log
```

## Gotchas

Because of the way Behave imports files and tests, using the built-in Python logging with `__name__` doesn't namespace the logs as expected. Providing an explicit name is therefore preferred.

```python
import logging

logger = logging.getLogger('mymodule.name')
# ...
logger.info('My log message.')
```
