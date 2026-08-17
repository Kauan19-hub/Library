import os
import pandas as pd

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Publisher, Author, Book

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--file_publishers",
            default=os.path.join(settings.BASE_DIR,"api","population","publishers.csv")
        )

        parser.add_argument(
            "--file_authors",
            default=os.path.join(settings.BASE_DIR,"api","population","authors.csv")
        )

        parser.add_argument(
            "--file_books",
            default=os.path.join(settings.BASE_DIR,"api","population","books.csv")
        )

        parser.add_argument("--truncate",action="store_true")
        parser.add_argument("--update",action="store_true")
        
    @transaction.atomic
    def handle(self, *a, **o):
        df_publishers=pd.read_csv(o["file_publishers"],encoding="utf-8-sig")
        df_authors=pd.read_csv(o["file_authors"],encoding="utf-8-sig")
        df_books=pd.read_csv(o["file_books"],encoding="utf-8-sig")
        df_publishers.columns=[c.strip().lower().lstrip("\ufeff") for c in df_publishers.columns]
        df_authors.columns=[c.strip().lower().lstrip("\ufeff") for c in df_authors.columns]
        df_books.columns=[c.strip().lower().lstrip("\ufeff") for c in df_books.columns]
        
        df_authors['complete_name']=df_authors['author']+' '+df_authors['s_author']
        df_authors['id']=df_authors.index + 1
        map_authors=dict(zip(df_authors['complete_name'],df_authors["id"]))
        df_books['id_author']=df_books['author'].map(map_authors)
        
        df_publishers['id']=df_publishers.index + 1
        map_publishers=dict(zip(df_publishers['publisher'], df_publishers['id']))
        df_books['id_publisher']=df_books["publisher"].map(map_publishers)

        if o["truncate"]: Book.objects.all().delete()
        
        df_books['title']=df_books["title"].astype(str).str.strip()
        df_books['subtitle']=df_books["subtitle"].astype(str).str.strip()
        
        df_books['author']=df_books["id_author"].astype(int)
        df_books['publisher']=df_books["id_publisher"].astype(int)
        
        df_books['isbn']=df_books["isbn"].astype(str).str.strip()
        df_books['description']=df_books["description"].astype(str).str.strip()
        df_books['language']=df_books["language"].astype(str).str.strip()
        df_books['year']=df_books["year"].astype(str)
        df_books['pages']=df_books["pages"].astype(int)
        df_books['price']=df_books["price"].astype(float)
        df_books['stock']=df_books["stock"].astype(int)
        df_books['discount']=df_books["discount"].astype(float)
        df_books['available']=df_books["available"].astype(bool)
        df_books['dimensions']=df_books["dimensions"].astype(str).str.strip()
        df_books['width']=df_books["width"].astype(float)

        if o["update"]:
            createds=updateds=0
            for r in df_books.itertuples(index=False):
                _, created = Book.objects.update_or_create(
                    isbn=r.isbn,
                    defaults={
                        "title": r.title,
                        "subtitle": r.subtitle or "",
                        "author_id": int(r.id_author),
                        "publisher_id": int(r.id_publisher),
                        "description": r.description or "",
                        "language": r.language or "",
                        "year": int(r.year) if pd.notna(r.year) else None,
                        "pages": int(r.pages),
                        "price": float(r.price),
                        "stock": int(r.stock),
                        "discount": float(r.discount),
                        "available": bool(r.available),
                        "dimensions": r.dimensions or "",
                        "width": float(r.width),
                    },
                )

            createds += int(created)
            updateds += int(not created)
            self.stdout.write(self.style.SUCCESS(f"Criados: {createds} | Atualizados: {updateds}"))
 
        else:
            objs=[]
            for r in df_books.itertuples(index=False):
                objs.append(
                    Book(
                        isbn=r.isbn,
                        title=r.title,
                        subtitle=r.subtitle or "",
                        author_id=int(r.id_author),
                        publisher_id=int(r.id_publisher),
                        description=r.description or "",
                        language=r.language or "",
                        year=int(r.year) if pd.notna(r.year) else None,
                        pages=int(r.pages),
                        price=float(r.price),
                        stock=int(r.stock),
                        discount=float(r.discount),
                        available=bool(r.available),
                        dimensions=r.dimensions or "",
                        width=float(r.width),
                    )
                )
            Book.objects.bulk_create(objs, ignore_conflicts=True)
            createds=len(objs)

            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objs)}"))