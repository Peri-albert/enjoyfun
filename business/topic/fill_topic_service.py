# -*- coding: utf-8 -*-

from rust.core import business

from business.dynamic.dynamic import Dynamic

from db.topic import models as topic_models
from db.dynamic import models as dynamic_models

from .activity import Activity

class FillTopicService(business.Service):
	def __fill_activity_data(self, topics):
		id2topic = {topic.id: topic for topic in topics}

		topic_ids = [topic.id for topic in topics]
		db_models = topic_models.TopicActivity.select().dj_where(topic_id__in=topic_ids).order_by('id')
		for topic in topics:
			topic.resources = []

		for db_model in db_models:
			id2topic.setdefault(db_model.topic_id, []).activities.append(Activity(db_model))

		for topic in topics:
			topic.activity_amount = len(topic.activities)

	def __fill_dynamic_data(self, topics):
		id2topic = {topic.id: topic for topic in topics}

		topic_ids = [topic.id for topic in topics]
		db_models = dynamic_models.Dynamic.select().dj_where(topic_id__in=topic_ids).order_by('-id')
		for topic in topics:
			topic.dynamics = []

		for db_model in db_models:
			id2topic.setdefault(db_model.topic_id, []).dynamics.append(Dynamic(db_model))


	def fill(self, topics, options=None):
		options = options or {}
		if options.get('with_activity', False):
			self.__fill_activity_data(topics)

		if options.get('with_dynamic', False):
			self.__fill_dynamic_data(topics)