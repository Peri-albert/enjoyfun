# coding: utf8

from rust.core import business


class Approval(business.Model):
	"""
	点赞
	"""
	__slots__ = (
		'id'
	)

	def __init__(self, db_model=None):
		super(Approval, self).__init__(db_model)

	@property
	def user_id(self):
		return self.context['db_model'].user_id

	@property
	def dynamic_id(self):
		return self.context['db_model'].dynamic_id