import json
from extra_utils import get_lambda_message

def lambda_handler(event, context):
    try:
        print('Received event: ', event)

        http_method = event['requestContext']['http']['method']
        path = event['requestContext']['http']['path']
        print('HTTP method: ', http_method)
        print('Path: ', path)

        if http_method == 'GET' and path == '/testGet':
            # get parameters
            query_params = event['queryStringParameters']
            print('query_params: ', query_params)

            response = {
                'statusCode': 200,
                'body': {
                    'message': 'message from GET request',
                    'request_params': query_params
                }
            }
        elif http_method == 'POST' and path == '/testPost' and valid_json(event['body']):
            body = event['body']
            print('body: ', body)

            response = {
                'statusCode': 200,
                'body': {
                    'message': 'message from POST request',
                    'request_body': body
                }
            }
        else:
            response = {
                'statusCode': 200,
                'body': {
                    'message': 'Invalid request.'
                }
            }

    except Exception as e:
        print('Error: ', e)
        return {
            'statusCode': 400,
            'body': 'Error processing request.'
        }
    
    return response
    
def valid_json(json_str):
    try:
        json.loads(json_str)
    except ValueError as e:
        return False
    return True