# coding: utf8

from rust.core import business


class Comment(business.Model):
	"""
	评论
	"""
	__slots__ = (
		'id',
		'content',
		'created_at'
	)

	def __init__(self, db_model=None):
		super(Comment, self).__init__(db_model)

	@property
	def user_id(self):
		return self.context['db_model'].user_id

	@property
	def dynamic_id(self):
		return self.context['db_model'].dynamic_id
