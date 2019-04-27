# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.dynamic.comment_service import CommentService


@Resource('dynamic.comment')
class AComment(ApiResource):

	@param_required(['user', 'dynamic_id', 'content'])
	def put(self):
		user = self.params['user']
		param_object = ParamObject({
			'user_id': user.id,
			'dynamic_id': self.params['dynamic_id'],
			'content': self.params['content']
		})
		comment = CommentService(user).comment(param_object)

		return {
			comment.id
		}

	@param_required(['user', 'id'])
	def delete(self):
		user = self.params['user']
		comment = CommentService(user).get_comment_by_id(self.params['id'])
		if not user.is_manager or comment.user_id != user.id:
			raise BusinessError(u'操作无权限')
		param_object = ParamObject({
			'id': self.params['id']
		})
		CommentService(user).cannel(param_object)

		return {}
