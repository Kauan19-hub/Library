import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environments';
import { Book } from '../models/book';

export type BookQuery = {
  search?: string;
  title?: string;
  author?: string;
  id?: number | string;
  ordering?: string;
};

@Injectable({ providedIn: 'root' })
export class BooksService {
  private http = inject(HttpClient);
  private api = (environment.apiBase ?? '').replace(/\/+$/, '');

  private baseList = `${this.api}/api/books/`;   
  private baseDetail = `${this.api}/api/books`;  

  list(q?: BookQuery): Observable<Book[]> {
    let params = new HttpParams();
    if (q) {
      for (const [k, v] of Object.entries(q)) {
        if (v !== undefined && v !== null && String(v).trim() !== '') {
          params = params.set(k, String(v));
        }
      }
    }
    return this.http.get<Book[]>(this.baseList, { params });
  }

  sendCover(id: number, file: File) {
    const form = new FormData();
    form.append('cover', file);
    return this.http.patch<Book>(`${this.baseDetail}/${id}/`, form);
  }
}
