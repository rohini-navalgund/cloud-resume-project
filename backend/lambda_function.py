import json

# Initialize counter outside function
counter = 0

def lambda_handler(event, context):
    global counter
    try:
        counter += 1
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Hello from Lambda!',
                'count': counter
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Internal Server Error',
                'error': str(e)
            })
        }
