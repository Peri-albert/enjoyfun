# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from db.dynamic import models as dynamic_models

from .approval import Approval


class LikeService(business.Service):
	"""
	点赞服务
	"""
	def like(self, param_object):
		"""
		点赞
		"""
		if dynamic_models.DynamicApproval.select().dj_where(
			user_id=param_object.user_id,
			dynamic_id=param_object.dynamic_id
		).exists():
			raise BusinessError('existed')
		else:
			db_model = dynamic_models.DynamicApproval.create(
				user_id=param_object.user_id,
				dynamic_id=param_object.dynamic_id
			)

			return Approval(db_model)

	def dislike(self, param_object):
		"""
		点赞取消
		"""
		dynamic_models.DynamicApproval.delete().dj_where(
			id=param_object.id,
		).execute()

	def get_approval_by_id(self, approval_id):
		"""
		根据id获取Approval对象
		"""
		db_model = dynamic_models.DynamicApproval.select().dj_where(id=approval_id).first()
		if db_model:
			return Approval(db_model)