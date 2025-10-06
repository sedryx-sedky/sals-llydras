class LlydrasError(Exception):
    """Base exception for all llydras errors."""
    pass

class PortfolioError(LlydrasError):
    """Portfolio related errors."""
    pass

class SourceError(LlydrasError):
    """Erroros related to Source data retrival."""
    pass

class InsufficientFundsError(PortfolioError):
    def __init__(self, required, available):
        message = (
            f"Insufficient funds (required: £{required:.2f}, available: £{available:.2f})."
        )
        super().__init__(message)

class ShortSellingError(PortfolioError):
    ...