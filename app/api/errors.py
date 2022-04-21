from fastapi import HTTPException, status


class UnfilledException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='{detail} Unfilled'.format(detail=detail),
        )


class DuplicationException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='{detail} Already Registered'.format(detail=detail),
        )


class InvalidPasswordException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password Invalid",
            headers={"WWW-Authenticate": "Bearer"}
        )


class PermissionException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Enough Permissions",
        )


class JWTDecodeException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could Not Decode JWT token",
        )


class ValidationException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could Not validate credentials",
        )


class NotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='{detail} Not Found'.format(detail=detail),
        )
