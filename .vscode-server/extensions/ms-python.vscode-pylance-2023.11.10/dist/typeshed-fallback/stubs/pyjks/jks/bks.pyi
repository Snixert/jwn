from _typeshed import Incomplete
from typing_extensions import Final, Self

from .jks import TrustedCertEntry
from .util import AbstractKeystore, AbstractKeystoreEntry

ENTRY_TYPE_CERTIFICATE: Final = 1
ENTRY_TYPE_KEY: Final = 2
ENTRY_TYPE_SECRET: Final = 3
ENTRY_TYPE_SEALED: Final = 4
KEY_TYPE_PRIVATE: Final = 0
KEY_TYPE_PUBLIC: Final = 1
KEY_TYPE_SECRET: Final = 2

class AbstractBksEntry(AbstractKeystoreEntry):
    cert_chain: Incomplete
    def __init__(self, **kwargs) -> None: ...

class BksTrustedCertEntry(TrustedCertEntry): ...

class BksKeyEntry(AbstractBksEntry):
    type: Incomplete
    format: Incomplete
    algorithm: Incomplete
    encoded: Incomplete
    pkey_pkcs8: Incomplete
    pkey: Incomplete
    algorithm_oid: Incomplete
    public_key_info: Incomplete
    public_key: Incomplete
    key: Incomplete
    key_size: Incomplete
    def __init__(self, type, format, algorithm, encoded, **kwargs) -> None: ...
    def is_decrypted(self): ...
    def decrypt(self, key_password) -> None: ...
    @classmethod
    def type2str(cls, t): ...

class BksSecretKeyEntry(AbstractBksEntry):
    key: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def is_decrypted(self): ...
    def decrypt(self, key_password) -> None: ...

class BksSealedKeyEntry(AbstractBksEntry):
    def __init__(self, **kwargs) -> None: ...
    def __getattr__(self, name): ...
    def is_decrypted(self): ...
    def decrypt(self, key_password) -> None: ...

class BksKeyStore(AbstractKeystore):
    version: Incomplete
    def __init__(self, store_type, entries, version: int = 2) -> None: ...
    @property
    def certs(self): ...
    @property
    def secret_keys(self): ...
    @property
    def sealed_keys(self): ...
    @property
    def plain_keys(self): ...
    @classmethod
    def loads(cls, data, store_password, try_decrypt_keys: bool = True) -> Self: ...

class UberKeyStore(BksKeyStore):
    @classmethod
    def loads(cls, data, store_password, try_decrypt_keys: bool = True) -> Self: ...
    version: Incomplete
    def __init__(self, store_type, entries, version: int = 1) -> None: ...
