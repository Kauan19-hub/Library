import os
import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Publisher

class Command(BaseCommand):
   def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=os.path.join(settings.BASE_DIR, "api","population","publishers.csv")
        )
        parser.add_argument("--truncate",action="store_true")
        parser.add_argument("--update",action="store_true")
   
   @transaction.atomic
   def handle(self, *a, **o):
        df=pd.read_csv(o["file"], encoding="utf-8-sig" )
        df.columns=[c.strip().lower().lstrip("\ufeff") for c in df.columns]
        if o["truncate"]: Publisher.objects.all().delete()

        df['publisher']=df['publisher'].astype(str).str.strip()
        df['cnpj']=df['cnpj'].astype(str).str.strip()
        df['address']=df['address'].astype(str).str.strip()
        df['phone']=df['phone'].astype(str).str.strip()
        df['email']=df['email'].astype(str).str.strip()
        df['site']=df['site'].astype(str).str.strip()
            
        if o["update"]:
            createds=updateds=0

            for r in df.itertuples(index=False):
                _, created=Publisher.objects.update_or_create(
                    publisher=r.publisher,cnpj=r.cnpj,address=r.address,  
                    phone=r.phone,email=r.email,site=r.site
                )

                createds += int(created)
                updateds += int(not created)

            self.stdout.write(self.style.SUCCESS(f"Criados: {createds} | {updateds}"))
        else:
            objs=[Publisher(
                  publisher=r.publisher,cnpj = r.cnpj,address=r.address, 
                  phone=r.phone, email=r.email,site=r.site

            ) for r in df.itertuples(index=False)
            ]

            Publisher.objects.bulk_create(objs,ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Criados {len(objs)}'))