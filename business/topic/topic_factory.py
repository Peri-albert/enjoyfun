# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from business.topic.topic import Topic
from db.topic import models as topic_models


class TopicFactory(business.Service):

	def create(self, param_object):
		if topic_models.Topic.select().dj_where(name=param_object.name).first():
			raise BusinessError('existed')

		db_model = topic_models.Topic.create(
			name = param_object.name,
			avatar = param_object.avatar,
			description = param_object.description
		)

		return Topic(db_model)

	def update(self, param_object):
		db_model = topic_models.Topic.select().dj_where(id=param_object.id).first()
		modified = False
		if param_object.name is not None and db_model.name != param_object.name:
			if topic_models.Topic.select().dj_where(name=param_object.name).first():
				raise BusinessError('existed')
			db_model.name = param_object.name
			modified = True

		if param_object.avatar is not None and db_model.avatar != param_object.avatar:
			db_model.avatar = param_object.avatar
			modified = True

		if param_object.description is not None and db_model.description != param_object.description:
			db_model.description = param_object.description
			modified = True

		modified and db_model.save()

