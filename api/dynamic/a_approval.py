# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.dynamic.like_service import LikeService


@Resource('dynamic.approval')
class AApproval(ApiResource):
	"""
	点赞
	"""
	@param_required(['user', 'dynamic_id'])
	def put(self):
		"""
		点赞
		"""
		user = self.params['user']
		param_object = ParamObject({
			'user_id': user.id,
			'dynamic_id': self.params['dynamic_id']
		})
		approval = LikeService(user).like(param_object)

		return {
			id: approval.id
		}

	@param_required(['user', 'id'])
	def delete(self):
		"""
		点赞取消
		"""
		user = self.params['user']
		approval = LikeService(user).get_approval_by_id(self.params['id'])
		if approval.user_id != user.id:
			raise BusinessError(u'操作无权限')
		param_object = ParamObject({
			'id': self.params['id']
		})
		LikeService(user).dislike(param_object)

		return {}
