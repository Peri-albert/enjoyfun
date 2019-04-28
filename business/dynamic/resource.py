# coding: utf8

from rust.core import business
from db.dynamic import models as dynamic_models


class Resource(business.Model):
	"""
	资源
	"""
	__slots__ = (
		'id',
		'url',
		'size'
	)

	def __init__(self, db_model=None):
		super(Resource, self).__init__(db_model)

	@property
	def type(self):
		return dynamic_models.DYNAMIC_RESOURCE_TYPE2TEXT[self.context['db_model'].type]
