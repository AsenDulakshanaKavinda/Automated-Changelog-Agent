

import hmac
import hashlib

def verify_github_signature(
        payload: bytes,
        signature_header: str,
        secret: str
) -> bool:
    
    """
    Securely verify the authenticity of a webhook payload from Github 

    - Args
        payload: bytes - raw body of the webhook request
        signature_header - value from the Github webhook
        secret - Github webhook secret (shared key between application and Github)

    - Return
        True if they match (payload is authentic), False otherwise

    """
    
    # if no signature -> return false
    if not signature_header:
        return False
    
    # splits header -> hash algorithm name & actural signature (sha256, abc123)
    sha_name, signature = signature_header.split("=")

    # signature must use SHA-256
    if sha_name != 'sha256':
        return False
    
    # create new HMAC obj.
    mac = hmac.new(
        secret.encode(), # convert to bytes
        msg=payload, # use raw payload as message
        digestmod=hashlib.sha256 # Specifies SHA-256 as the hash function.
    )

    # Gets the HMAC as a hexadecimal string and compare with signature
    return hmac.compare_digest(mac.hexdigest(), signature)








