from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

# !!!! SELECT MODE !!!!
MODE = "DEVELOPMENT"

# Close all open positions and orfers
ABORT_ALL_POSITIONS = False

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Place Trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880  # MONEY in your account

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Etherium Address
ETHEREUM_ADDRESS = "0x58C8437e945A65F15a1D5ec2438f08177748F9E3"

# KEYS - Production
# Must be on Mainnet on DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS - Development
# Must be on Testnet on DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = (
    STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
)
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = (
    DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
)
DYDX_API_PASSPHRASE = (
    DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET
)


# HOST - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

# HTTP Provider
HTTP_PROVIDER_MAINNET = (
    "https://eth-mainnet.g.alchemy.com/v2/2JaFNCdMIFLKNl_9yjkj-nkhI-UNS6Iy"
)
HTTP_PROVIDER_TESTNET = (
    "https://eth-goerli.g.alchemy.com/v2/kYAQj5ifxOqPrdu4lYBaF_z_F8LGs6a4"
)
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET
