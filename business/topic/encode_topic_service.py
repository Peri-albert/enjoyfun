# coding: utf8

from rust.core import business


class EncodeTopicService(business.Service):
	"""
	封装话题Topic数据的服务
	"""
	def encode(self, topic):
		"""
		封装话题Topic数据
		"""
		data = {
			'id': topic.id,
			'name': topic.name,
			'avatar': topic.avatar,
			'description': topic.description,
			'activities': [],
			'dynamics': [],
			'activity_amount': 0,
			'dynamic_amount': 0
		}

		if topic.activities:
			data['activity_amount'] = topic.activity_amount
			for activity in topic.activities:
				data['activities'].append({
					'id': activity.id
				})

		if topic.dynamics:
			for dynamic in topic.dynamics:
				data['dynamics'].append({
					'id': dynamic.id,
					'content': dynamic.content,
					'user_id': dynamic.user_id,
					'topic_id': dynamic.topic_id,
					'longitude': dynamic.longitude,
					'latitude': dynamic.latitude
				})

		return data
