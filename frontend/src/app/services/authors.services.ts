import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Author } from '../models/author';
import { environment } from '../../environments/environments';

@Injectable({
  providedIn: 'root'
})

export class AuthorsService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  list():Observable<Author[]> {
    const url = `${this.base}api/authors/`;
    return this.http.get<Author[]>(url);
  }
}

