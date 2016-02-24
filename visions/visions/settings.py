
BOT_NAME = 'visionsChallenge'

SPIDER_MODULES = ['visions.spiders']
NEWSPIDER_MODULE = 'visions.spiders'

ITEM_PIPELINES = {	'visions.pipelines.VisionsPrettyPipeline':100,
					'visions.pipelines.VisionsJsonPipeline':100}
				  	
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

