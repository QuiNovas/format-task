import logging.config
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('Processing event :{}'.format(json.dumps(event)))
    results = event['results']
    arguments = event['arguments']
    for key in results:
        results[key] = results[key].format(**arguments)
    return results
