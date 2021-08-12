class FlyffException(Exception):

    def __init__(self, http_status, code, msg, reason=None):
        self.http_status = http_status
        self.code = code
        self.msg = msg
        self.reason = reason

    def __str__(self):
        return 'http status: {0}, code: {1} - {2}, reason: {3}'.format(
            self.http_status, self.code, self.msg, self.reason)
