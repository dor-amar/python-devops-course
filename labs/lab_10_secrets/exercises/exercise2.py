"""Secrets management module for handling sensitive data."""

import os
import json
import logging
import base64
from typing import Any, Dict, Optional, Union
from datetime import datetime, timedelta
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from jose import JWTError, jwt
from jose.utils import base64url_decode
import hvac


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SecretsManager:
    """Manager for handling secrets and sensitive data."""

    def __init__(
        self,
        encryption_key: Optional[str] = None,
        vault_url: Optional[str] = None,
        vault_token: Optional[str] = None,
        vault_path: str = "secret"
    ):
        """Initialize the secrets manager.

        Args:
            encryption_key: Key for local encryption
            vault_url: HashiCorp Vault URL
            vault_token: Vault authentication token
            vault_path: Vault secrets path
        """
        self.encryption_key = encryption_key or self._generate_key()
        self.fernet = Fernet(self._derive_key(self.encryption_key))
        self.vault_url = vault_url
        self.vault_token = vault_token
        self.vault_path = vault_path
        self.vault_client = self._init_vault_client()

    def _generate_key(self) -> str:
        """Generate a random encryption key.

        Returns:
            str: Generated key
        """
        return Fernet.generate_key().decode()

    def _derive_key(self, key: str) -> bytes:
        """Derive a key using PBKDF2.

        Args:
            key: Base key

        Returns:
            bytes: Derived key
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"secrets_manager",
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(key.encode()))

    def _init_vault_client(self) -> Optional[hvac.Client]:
        """Initialize Vault client if credentials are provided.

        Returns:
            Optional[hvac.Client]: Vault client
        """
        if self.vault_url and self.vault_token:
            return hvac.Client(
                url=self.vault_url,
                token=self.vault_token
            )
        return None

    def encrypt(self, data: Union[str, Dict[str, Any]]) -> str:
        """Encrypt data locally.

        Args:
            data: Data to encrypt

        Returns:
            str: Encrypted data
        """
        if isinstance(data, dict):
            data = json.dumps(data)
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, encrypted_data: str) -> Union[str, Dict[str, Any]]:
        """Decrypt data locally.

        Args:
            encrypted_data: Encrypted data

        Returns:
            Union[str, Dict[str, Any]]: Decrypted data
        """
        try:
            decrypted = self.fernet.decrypt(encrypted_data.encode()).decode()
            try:
                return json.loads(decrypted)
            except json.JSONDecodeError:
                return decrypted
        except Exception as e:
            logger.error(f"Decryption failed: {e}")
            raise

    def store_secret(
        self,
        key: str,
        value: Any,
        expiration: Optional[timedelta] = None
    ) -> None:
        """Store a secret in Vault.

        Args:
            key: Secret key
            value: Secret value
            expiration: Secret expiration time
        """
        if not self.vault_client:
            raise ValueError("Vault client not initialized")

        try:
            secret_data = {
                "value": value,
                "created_at": datetime.utcnow().isoformat(),
                "expires_at": (
                    datetime.utcnow() + expiration
                ).isoformat() if expiration else None
            }

            self.vault_client.secrets.kv.v2.create_or_update_secret(
                path=f"{self.vault_path}/{key}",
                secret=secret_data
            )
            logger.info(f"Secret '{key}' stored successfully")
        except Exception as e:
            logger.error(f"Failed to store secret '{key}': {e}")
            raise

    def get_secret(self, key: str) -> Any:
        """Retrieve a secret from Vault.

        Args:
            key: Secret key

        Returns:
            Any: Secret value

        Raises:
            ValueError: If secret is expired or not found
        """
        if not self.vault_client:
            raise ValueError("Vault client not initialized")

        try:
            response = self.vault_client.secrets.kv.v2.read_secret_version(
                path=f"{self.vault_path}/{key}"
            )
            secret_data = response["data"]["data"]

            # Check expiration
            if secret_data.get("expires_at"):
                expires_at = datetime.fromisoformat(secret_data["expires_at"])
                if datetime.utcnow() > expires_at:
                    raise ValueError(f"Secret '{key}' has expired")

            return secret_data["value"]
        except Exception as e:
            logger.error(f"Failed to retrieve secret '{key}': {e}")
            raise

    def delete_secret(self, key: str) -> None:
        """Delete a secret from Vault.

        Args:
            key: Secret key
        """
        if not self.vault_client:
            raise ValueError("Vault client not initialized")

        try:
            self.vault_client.secrets.kv.v2.delete_secret_versions(
                path=f"{self.vault_path}/{key}",
                versions=[1]
            )
            logger.info(f"Secret '{key}' deleted successfully")
        except Exception as e:
            logger.error(f"Failed to delete secret '{key}': {e}")
            raise

    def rotate_key(self) -> None:
        """Rotate the encryption key."""
        self.encryption_key = self._generate_key()
        self.fernet = Fernet(self._derive_key(self.encryption_key))
        logger.info("Encryption key rotated successfully")

    def generate_jwt(
        self,
        payload: Dict[str, Any],
        expiration: Optional[timedelta] = None
    ) -> str:
        """Generate a JWT token.

        Args:
            payload: Token payload
            expiration: Token expiration time

        Returns:
            str: JWT token
        """
        if expiration:
            payload["exp"] = datetime.utcnow() + expiration
        return jwt.encode(payload, self.encryption_key, algorithm="HS256")

    def verify_jwt(self, token: str) -> Dict[str, Any]:
        """Verify a JWT token.

        Args:
            token: JWT token to verify

        Returns:
            Dict[str, Any]: Token payload

        Raises:
            JWTError: If token is invalid
        """
        try:
            return jwt.decode(token, self.encryption_key, algorithms=["HS256"])
        except JWTError as e:
            logger.error(f"JWT verification failed: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize secrets manager
        secrets = SecretsManager()

        # Test local encryption
        print("Testing local encryption:")
        data = {"username": "admin", "password": "secret123"}
        encrypted = secrets.encrypt(data)
        print(f"Encrypted: {encrypted}")
        decrypted = secrets.decrypt(encrypted)
        print(f"Decrypted: {decrypted}")

        # Test JWT generation and verification
        print("\nTesting JWT:")
        payload = {"user_id": 123, "role": "admin"}
        token = secrets.generate_jwt(payload, timedelta(hours=1))
        print(f"Generated token: {token}")
        verified = secrets.verify_jwt(token)
        print(f"Verified payload: {verified}")

        # Test Vault integration (if credentials provided)
        if os.getenv("VAULT_URL") and os.getenv("VAULT_TOKEN"):
            print("\nTesting Vault integration:")
            secrets = SecretsManager(
                vault_url=os.getenv("VAULT_URL"),
                vault_token=os.getenv("VAULT_TOKEN")
            )

            # Store secret
            secrets.store_secret(
                "api_key",
                "secret123",
                expiration=timedelta(days=1)
            )

            # Retrieve secret
            value = secrets.get_secret("api_key")
            print(f"Retrieved secret: {value}")

            # Delete secret
            secrets.delete_secret("api_key")
            print("Secret deleted")

    except Exception as e:
        print(f"Error: {e}") 