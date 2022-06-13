import datetime
import rsa
from botocore.signers import CloudFrontSigner

def rsa_signer(message):
    private_key = open('/Path/to/private_key.pem', 'r').read()
    return rsa.sign(message, rsa.PrivateKey.load_pkcs1(private_key.encode('utf8')),'SHA-1')

key_id = 'K1DGBEXAMPLE'  -- Key ID on the Public Keys Screen
url = 'https://d28gks2t63pxns.cloudfront.net/'   -- Distribution domain name
expire_at = datetime.datetime(2022, 10, 12)

cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)
policy = cloudfront_signer.build_policy(url, expire_at).encode('utf8')
policy_64 = cloudfront_signer._url_b64encode(policy).decode('utf8')

signature = rsa_signer(policy)
signature_64 = cloudfront_signer._url_b64encode(signature).decode('utf8')

print("CloudFront-Policy=" + policy_64)
print("CloudFront-Signature=" + signature_64)
print("CloudFront-Key-Pair-Id=" + key_id)

#CURL command for test
#curl --verbose --location --request GET 'https://d28gks2t63pxns.cloudfront.net/' \
#--header 'Cookie: CloudFront-Policy=first_cookie_value  ; CloudFront-Signature=second-cookie-value  ; CloudFront-Key-Pair-Id=third-cookie-value' \
#--output cataws2.jpg
