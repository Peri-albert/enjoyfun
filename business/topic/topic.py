# coding: utf8

from rust.core import business


class Topic(business.Model):
	"""
	话题
	"""
	__slots__ = (
		'id',
		'name',
		'avatar',
		'description',
		'created_at',
		'is_banned'
	)

	def __init__(self, db_model=None):
		super(Topic, self).__init__(db_model)

