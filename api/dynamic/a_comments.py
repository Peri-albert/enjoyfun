# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.dynamic.comment_service import CommentService
from business.dynamic.encode_comment_service import EncodeCommentService


@Resource('dynamic.comments')
class AComments(ApiResource):

	@param_required(['user', 'dynamic_id', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		user = self.params['user']
		target_page = TargetPage(self.params)
		filters = self.params.get('filters')

		param_object = ParamObject({
			'dynamic_id': self.params['dynamic_id']
		})
		comments = CommentService(user).get_comments(param_object, filters, target_page)

		return {
			'dynamics': [EncodeCommentService(user).encode(comment) for comment in comments],
			'page_info': target_page.to_dict() if target_page else {}
		}