from __init__ import create_celery_app

celery = create_celery_app()

import img_deal.tasks

