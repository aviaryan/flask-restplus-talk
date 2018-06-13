class BaseError(Exception):
	def __init__(self, error='', code=400):
		Exception.__init__(self)
		self.error = error
		self.code = code

	def to_dict(self):
		return {'error': self.error}

	def __str__(self):
		return self.error

class NotFoundError(BaseError):
	def __init__(self):
		BaseError.__init__(self)
		self.error = 'Resource was not found'
		self.code = 404
