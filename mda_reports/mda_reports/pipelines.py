# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import boto3


class MdaReportsPipeline(object):
    def process_item(self, item, spider):
        return item

class ManageDataPipeline(object):
    """ file_urls was not processed through items.
        Takefirst() was not applied to it.
        Thus it returned list items.
    """

    def process_item(self, item, spider):
        if item['file_urls']:
            item['file_urls'] = item['file_urls'][0]
        if item['files']:
            item['files'] = item['files'][0]['path'].split('/')[1]
        return item

class DynamoDBStorePipeline(object):

    def process_item(self, item, spider):
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb',region_name=os.environ['region'])

        table = dynamodb.Table('MdaReports03')

        table.put_item(
        Item={
        'date': str(item['date']),
        'time': str(item['time']),
        'character': str(item['character']),
        'symbol': str(item['symbol']),
        'company': str(item['company']),
        'market': str(item['market']),
        'heading': str(item['heading']),
        'file_urls': str(item['file_urls']),
        'files': str(item['files']),
        })
        return item
