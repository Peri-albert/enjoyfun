# -*- coding: utf-8 -*-

from rust.core import business

from db.dynamic import models as dynamic_models

from .resource import Resource
from .comment import Comment
from .approval import Approval


class FillDynamicService(business.Service):
	"""
	填充动态服务
	"""
	def __fill_resource_data(self, dynamics):
		"""
		填充资源数据
		"""
		id2dynamic = {dynamic.id: dynamic for dynamic in dynamics}

		dynamic_ids = [dynamic.id for dynamic in dynamics]
		db_models = dynamic_models.DynamicResource.select().dj_where(dynamic_id__in=dynamic_ids).order_by('id')
		for dynamic in dynamics:
			dynamic.resources = []

		for db_model in db_models:
			id2dynamic.setdefault(db_model.dynamic_id, []).resources.append(Resource(db_model))

	def __fill_comment_data(self, dynamics):
		"""
		填充评论数据
		"""
		id2dynamic = {dynamic.id: dynamic for dynamic in dynamics}

		dynamic_ids = [dynamic.id for dynamic in dynamics]
		db_models = dynamic_models.DynamicComment.select().dj_where(dynamic_id__in=dynamic_ids).order_by('id')
		for dynamic in dynamics:
			dynamic.comments = []

		for db_model in db_models:
			id2dynamic.setdefault(db_model.dynamic_id, []).comments.append(Comment(db_model))

		for dynamic in dynamics:
			dynamic.comment_amount = len(dynamic.comments)

	def __fill_approval_data(self, dynamics):
		"""
		填充点赞数据
		"""
		id2dynamic = {dynamic.id: dynamic for dynamic in dynamics}

		dynamic_ids = [dynamic.id for dynamic in dynamics]
		db_models = dynamic_models.DynamicApproval.select().dj_where(dynamic_id__in=dynamic_ids)
		for dynamic in dynamics:
			dynamic.approvals = []

		for db_model in db_models:
			id2dynamic.setdefault(db_model.dynamic_id, []).approvals.append(Approval(db_model))

		for dynamic in dynamics:
			dynamic.approval_amount = len(dynamic.approvals)

	def fill(self, dynamics, options=None):
		"""
		填充选项
		"""
		options = options or {}
		if options.get('with_resource', False):
			self.__fill_resource_data(dynamics)

		if options.get('with_comment', False):
			self.__fill_comment_data(dynamics)

		if options.get('with_approval', False):
			self.__fill_approval_data(dynamics)
