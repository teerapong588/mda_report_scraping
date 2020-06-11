# mda_report_scraping

Instruction
1. Create aws.env file in prodcontainer diretory
2. In settings.py, set FILES_STORE= < YOUR_S3_URI>
3. In pipelines.py, set table = dynamodb.Table('<YOUR_DYNAMODB_TABLE')
