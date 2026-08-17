import os
import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Author

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=os.path.join(settings.BASE_DIR, "api","population","authors.csv")
        )
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        df=pd.read_csv(o["file"], encoding="utf-8-sig")
        df.columns=[c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if o["truncate"]: 
            Author.objects.all().delete()

        df['author']=df['author'].astype(str).str.strip()
        df['s_author']=df['s_author'].astype(str).str.strip()
        df['birth']=pd.to_datetime(df["birth_date"],errors="coerce", format="%Y-%m-%d").dt.date
        
        if 'nacionality' not in df.columns and 'nationality' in df.columns:
            df['nacionality']=df['nationality']
        elif 'nacionality' not in df.columns:
            df['nacionality']=""

        df['nacionality']=df['nacionality'].astype(str).str.strip().str.capitalize().replace({"": None, "Nan": None})
        df=df.query("author != '' and s_author != ''")

        if o["update"]:
            createds=updated=0

            for r in df.itertuples(index=False):
                _, created=Author.objects.update_or_create(
                    author=r.author,
                    s_author=r.s_author,
                    birth=r.birth,   
                    defaults={'nacionality': r.nacionality}
                )

                createds += int(created)
                updated += int(not created)

            self.stdout.write(self.style.SUCCESS(f"Criados: {createds} | Atualizados: {updated}"))

        else:
            objs=[
                Author(
                    author=r.author,
                    s_author=r.s_author,
                    birth=r.birth,
                    nacionality=r.nacionality
                ) 
                
                for r in df.itertuples(index=False)
            ]
            
            Author.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Criados: {len(objs)}'))