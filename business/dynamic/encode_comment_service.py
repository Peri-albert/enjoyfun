# coding: utf8

from rust.core import business


class EncodeCommentService(business.Service):
	"""
	封装评论Comment数据的服务
	"""
	def encode(self, comment):
		"""
		封装评论Comment数据
		"""
		data = {
			'id': comment.id,
			'content': comment.content,
			'dynamic_id': comment.dynamic_id,
			'user_id': comment.user_id
		}

		return data
