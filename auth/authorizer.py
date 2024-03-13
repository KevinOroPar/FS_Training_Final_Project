from jose import jwt
import json

def custom_authorizer(event, context):
    token = event['authorizationToken']
    claims = jwt.get_unverified_claims(token)
    requester_user_id = claims.get('username')
    tmp = event['methodArn'].split(':')
    apiGatewayArnTmp = tmp[5].split('/')
    user_id = apiGatewayArnTmp[-1]

    if user_id == requester_user_id:
        print('authorized')
        response = generatePolicy('user', 'Allow', event['methodArn'])
    else: 
        print('unauthorized')
        response = generatePolicy('user', 'Deny', event['methodArn'])
   
    return json.loads(response)
    
        
                                   
def generatePolicy(principalId, effect, resource):
        authResponse = {}
        authResponse['principalId'] = principalId
        if (effect and resource):
            policyDocument = {}
            policyDocument['Version'] = '2012-10-17'
            policyDocument['Statement'] = [];
            statementOne = {}
            statementOne['Action'] = 'execute-api:Invoke'
            statementOne['Effect'] = effect
            statementOne['Resource'] = resource
            policyDocument['Statement'] = [statementOne]
            authResponse['policyDocument'] = policyDocument
        authResponse['context'] = {
            "stringKey": "stringval",
            "numberKey": 123,
            "booleanKey": True
        }
        authResponse_JSON = json.dumps(authResponse)
        return authResponse_JSON