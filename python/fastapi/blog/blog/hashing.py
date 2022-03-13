from passlib.context import CryptContext as CC


pw_ctx = CC(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def encrypt(password: str):
        return pw_ctx.hash(password)

    def verify(plain_password, hashed_password):
        return pw_ctx.verify(plain_password, hashed_password)
