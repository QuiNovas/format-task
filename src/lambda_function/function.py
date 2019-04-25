import logging.config
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info('Processing event :{}'.format(json.dumps(event)))
    results = event['Results']
    arguments = event['Arguments']
    if isinstance(results, dict):
        for key in results:
            results[key] = results[key].format(**arguments)
        return results
    elif isinstance(results, (list, tuple)):
        return [result.format(**arguments) for result in results]
    elif isinstance(results, str):
        return results.format(**arguments)
    else:
        raise ValueError('Invalid results type {}'.format(type(results)))
