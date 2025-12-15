
from fastapi import HTTPException
from src.changelog_agent.utils.logger_config import log

import hashlib
import hmac


def verify_github_signature(payload_body: bytes, secret_token: str, signature_header: str):
    """
    Verify that the payload was sent from GitHub using SHA-1.

    Args:
        payload_body: Raw request body (request.body())
        secret_token: GitHub webhook secret
        signature_header: Value of 'X-Hub-Signature'
    """

    if not signature_header:
        log.warning("No GitHub signature header received")
        raise HTTPException(
            status_code=403,
            detail="X-Hub-Signature header is missing"
        )

    # Create HMAC SHA-1 digest
    hash_object = hmac.new(
        secret_token.encode("utf-8"),
        msg=payload_body,
        digestmod=hashlib.sha1
    )

    expected_signature = f"sha1={hash_object.hexdigest()}"

    # Constant-time comparison (security critical)
    if not hmac.compare_digest(expected_signature, signature_header):
        log.error(
            f"GitHub signature mismatch | "
            f"expected={expected_signature}, received={signature_header}"
        )
        raise HTTPException(
            status_code=403,
            detail="Invalid GitHub signature"
        )
    log.info(f'expected_signature={expected_signature}, received={signature_header}')
    return True

