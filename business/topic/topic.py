# coding: utf8

from rust.core import business

class Topic(business.Model):

	__slots__ = (
		'id',
		'name',
		'created_at',
	)

	def __init__(self, db_model=None):
		super(Topic, self).__init__(db_model)

