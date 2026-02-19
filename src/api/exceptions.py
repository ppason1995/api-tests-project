class ApiError(Exception):
    """Base exception for API errors."""
    pass


class BadRequestError(ApiError):
    """400 Bad Request"""
    pass


class UnauthorizedError(ApiError):
    """401 Unauthorized"""
    pass


class ForbiddenError(ApiError):
    """403 Forbidden"""
    pass


class NotFoundError(ApiError):
    """404 Not Found"""
    pass


class ServerError(ApiError):
    """5xx Server error"""
    pass


