import { inject, Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";
import { environment } from "../../environments/environments";

export type Image = {
    id: number;
    image: string;
    url: string;
    created_at: string;
}

@Injectable({providedIn: 'root'})
export class ImageService {
    private http = inject(HttpClient)
    private base = `${environment.apiBase}api/images`

    private headers(): HttpHeaders {
        const token = localStorage.getItem('access')
        return token ? new HttpHeaders({Authorization: `Bearer ${token}`}) : new HttpHeaders()
    } 

    list(): Observable<Image[]> {
        return this.http.get<Image[]>(this.base, {headers: this.headers()})
    }

    send(file: File): Observable<Image> {
        const form = new FormData()
        form.append('image', file)
        return this.http.post<Image>(this.base, form, {headers: this.headers()})
    }

    delete(id: number) {
        return this.http.delete(`${this.base}${id}/`, {headers: this.headers()})
    }
}