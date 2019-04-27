# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.topic.topic_repository import TopicRepository
from business.topic.topic_factory import TopicFactory


@Resource('topic.topic')
class ATopic(ApiResource):

	@param_required(['user', 'id:int'])
	def get(self):
		user = self.params['user']
		topic = TopicRepository(user).get_topic_by_id(self.params['id'])
		if not topic:
			return 500, u'不存在'
		else:
			return {
				'id': topic.id,
				'name': topic.name
			}

	@param_required(['user', 'name'])
	def put(self):
		user = self.params['user']
		param_object = ParamObject({
			'name': self.params['name']
		})
		topic = TopicFactory(user).create(param_object)
		return {
			'id': topic.id
		}

	@param_required(['user', 'id:int', 'name'])
	def post(self):
		user = self.params['user']
		param_object = ParamObject({
			'id': self.params['id'],
			'name': self.params['name']
		})
		TopicFactory(user).update(param_object)
		return {}

	@param_required(['user', 'id:int'])
	def delete(self):
		user = self.params['user']
		param_object = ParamObject({
			'id': self.params['id']
		})
		TopicFactory(user).delete(param_object)
		return {}

