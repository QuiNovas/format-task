import json
import logging.config
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('Processing event :{}'.format(json.dumps(event)))
    results = event['Results']
    arguments = event('Arguments', {})
    pattern = event('Pattern', 'a^')
    repl = event('Replacement', '')
    if isinstance(results, dict):
        for key in results:
            results[key] = re.sub(pattern, repl, results[key]).format(**arguments)
        return results
    elif isinstance(results, (list, tuple)):
        return [re.sub(pattern, repl, result).format(**arguments) for result in results]
    elif isinstance(results, str):
        return re.sub(pattern, repl, results).format(**arguments)
    else:
        raise ValueError('Invalid results type {}'.format(type(results)))
