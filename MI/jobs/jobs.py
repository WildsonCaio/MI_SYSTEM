from django.conf import settings
from datetime import datetime
from MI.models import Customers
from MI.send_emails import send_email
# from MI.logs.log import * 
import logging

logging.basicConfig(
    filename='info.log',
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s'
)



def schedule_api():
    customers = Customers.objects.all()
    for client in customers:
        if client.status == False:
            try:
                send_email(client.name, 'lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem ', 'Trav 5 entre 7° e 8° ruas bairro Matinha')
                client.status = True
                client.save()
                logging.info(f'{client.name} recebeu o email.')
            except:
                logging.warning((f'{client.name} não recebeu o email.'))
            
                      
    
   