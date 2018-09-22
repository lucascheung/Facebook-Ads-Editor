#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:21:17 2017

@author: lucascheung
"""

from facebookads.api import FacebookRequest
from facebookads.typechecker import TypeChecker
from facebookads.adobjects.objectparser import ObjectParser
from facebookads.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class DeliveryEstimate(
AbstractObject,
):

    def __init__(self, api=None):
	    super(DeliveryEstimate, self).__init__()
	    self._isDeliveryEstimate = True
	    self._api = api

    @staticmethod
    def get_delivery_estimate(adaccount, fields=None, params=None, batch=None, pending=False):
   
        	param_types = {
        		'optimization_goal': 'optimization_goal_enum',
        		'targeting_spec': 'Targeting',
        	}
        	enums = {
        		'optimization_goal_enum': DeliveryEstimate.OptimizationGoal.__dict__.values(),
        	}
        	request = FacebookRequest(
        		node_id=adaccount['id'],
        		method='GET',
        		endpoint='/delivery_estimate',
        		api=adaccount._api,
        		param_checker=TypeChecker(param_types, enums),
        		target_class=DeliveryEstimate,
        		api_type='EDGE',
        		response_parser=ObjectParser(target_class=DeliveryEstimate),
        	)
        	request.add_params(params)
        	request.add_fields(fields)
        
        	if batch is not None:
        		request.add_to_batch(batch)
        		return request
        	elif pending:
        		return request
        	else:
        		adaccount.assure_call()
        		return request.execute()

    class Field(AbstractObject.Field):
        	data = 'data'
        	bid_estimate = 'bid_estimate'
        	min_bid = 'min_bid'
        	median_bid = 'median_bid'
        	max_bid = 'max_bid'
        	daily_outcomes_curve = 'daily_outcomes_curve'
        	spend = 'spend'
        	impressions = 'impressions'
        	actions = 'actions'
        	estimate_dau = 'estimate_dau'
        	estimate_mau = 'estimate_mau'
        	estimate_ready = 'estimate_ready' 

    class OptimizationGoal:
        	none = 'NONE'
        	app_installs = 'APP_INSTALLS'
        	brand_awareness = 'BRAND_AWARENESS'
        	clicks = 'CLICKS'
        	engaged_users = 'ENGAGED_USERS'
        	event_responses = 'EVENT_RESPONSES'
        	impressions = 'IMPRESSIONS'
        	lead_generation = 'LEAD_GENERATION'
        	link_clicks = 'LINK_CLICKS'
        	offer_claims = 'OFFER_CLAIMS'
        	offsite_conversions = 'OFFSITE_CONVERSIONS'
        	page_engagement = 'PAGE_ENGAGEMENT'
        	page_likes = 'PAGE_LIKES'
        	post_engagement = 'POST_ENGAGEMENT'
        	reach = 'REACH'
        	social_impressions = 'SOCIAL_IMPRESSIONS'
        	video_views = 'VIDEO_VIEWS'
        	app_downloads = 'APP_DOWNLOADS'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'delivery_estimate'

    _field_types = {
        	'data':'list<Object>',
        	'bid_estimate':'bid_estimate',
        	'min_bid':'unsigned int',
        	'median_bid':'unsigned int',
        	'max_bid':'unsigned int',
        	'daily_outcomes_curve':'list<Object>',
        	'spend':'unsigned int',
        	'impressions':'unsigned int',
        	'actions':'unsigned int',
        	'estimate_dau':'unsigned int',
        	'estimate_mau':'unsigned int',
        	'estimate_ready':'bool', 
            }

    @classmethod
    def _get_field_enum_info(cls):
        	field_enum_info = {}
        	field_enum_info['OptimizationGoal'] = DeliveryEstimate.OptimizationGoal.__dict__.values()
        	return field_enum_info