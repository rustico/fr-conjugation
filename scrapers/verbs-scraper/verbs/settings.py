# Scrapy settings for verbs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'verbs'

SPIDER_MODULES = ['verbs.spiders']
NEWSPIDER_MODULE = 'verbs.spiders'

FEED_FORMAT = 'csv'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'verbs (+http://www.yourdomain.com)'
