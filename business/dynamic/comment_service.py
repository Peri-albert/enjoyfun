# coding: utf8

from rust.core import business

from db.dynamic import models as dynamic_models

from .comment import Comment


class CommentService(business.Service):
	"""
	评论服务
	"""
	def comment(self, param_object):
		"""
		发布评论
		"""
		db_model = dynamic_models.DynamicComment.create(
			user_id=param_object.user_id,
			dynamic_id=param_object.dynamic_id,
			content=param_object.content
		)

		return Comment(db_model)

	def cannel(self, param_object):
		"""
		删除评论
		"""
		dynamic_models.DynamicComment.delete().dj_where(
			id=param_object.id
		).execute()

	def get_comment_by_id(self, comment_id):
		"""
		根据id获取评论
		"""
		db_model = dynamic_models.DynamicComment.select().dj_where(id=comment_id).first()
		if db_model:
			return Comment(db_model)

	def get_comments(self, param_object, filters=None, target_page=None):
		"""
		获取评论列表
		"""
		db_models = dynamic_models.DynamicComment.select().dj_where(
			dynamic_id = param_object.dynamic_id
		)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('id')
		return [Comment(db_model) for db_model in db_models]
