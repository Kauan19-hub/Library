import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Publisher } from '../models/publisher';
import { environment } from '../../environments/environments';

@Injectable({  providedIn: 'root'})

export class PublishersService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar():Observable<Publisher[]> {
    const url = `${this.base.replace(/\/+$/, '')}/api/publishers/`;
    return this.http.get<Publisher[]>(url);
    
  }
}

