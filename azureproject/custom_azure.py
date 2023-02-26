from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'hawkvisumfilestorage'
    account_key = 'VCVdWsO00YMX/5krpUj1r8cpBIaa+VMlymtg2iY88zNjGjOe8F/q99gOV1Eqfeu6+9r215u00gcd+AStp7mF1A=='
    azure_container = 'media'
    expiration_secs = None