# coding: utf8

from rust.core import business


class EncodeDynamicService(business.Service):
	"""
	封装动态Dynamic数据的服务
	"""
	def encode(self, dynamic):
		"""
		封装动态Dynamic数据
		"""
		data = {
			'id': dynamic.id,
			'content': dynamic.content,
			'user_id': dynamic.user_id,
			'topic_id': dynamic.topic_id,
			'longitude': dynamic.longitude,
			'latitude': dynamic.latitude,
			'resources': [],
			'comments': [],
			'approvals': [],
			'approval_amount': 0,
			'comment_amount': 0
		}

		if dynamic.resources:
			for resource in dynamic.resources:
				data['resources'].append({
					'id': resource.id,
					'url': resource.url,
					'size': resource.size,
					'type': resource.type
				})

		if dynamic.approvals:
			data['approval_amount'] = dynamic.approval_amount
			for approval in dynamic.approvals:
				data['approvals'].append({
					'id': approval.id
				})

		if dynamic.comments:
			data['comment_amount'] = dynamic.comment_amount
			for comment in dynamic.comments:
				data['comments'].append({
					'id': comment.id,
					'content': comment.content,
					'user_id': comment.user_id,
					'dynamic_id': comment.dynamic_id
				})

		return data
