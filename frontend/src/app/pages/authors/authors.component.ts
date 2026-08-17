import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthorsService } from '../../services/authors.services';
import { Author } from '../../models/author';
import { AuthService } from '../../services/auth.services';

@Component({
  selector: 'app-authors',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './authors.component.html'
})
export class AuthorsPage {
  private svc = inject(AuthorsService);
  private auth = inject(AuthService); 

  authors = signal<Author[]>([]);
  loading = signal(true);
  error = signal<string | null>(null); 

  constructor() {
    this.svc.list().subscribe({
      next: (data) => { 
        this.authors.set(data); 
        this.loading.set(false); 
      },

      error: () => { 
        this.error.set('Falha ao carregar autores'); 
        this.loading.set(false); 
      }
    });
  }
}