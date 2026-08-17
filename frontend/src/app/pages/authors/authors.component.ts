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
  readonly error = signal(false);

  private svc = inject(AuthorsService);
  private auth = inject(AuthService); 

  authors = signal<Author[]>([]);
  loading = signal(true);

  constructor() {
    this.svc.list().subscribe({
      next: (data) => { 
        this.authors.set(data); 
        this.loading.set(false); 
      },

      error: () => { 
        this.error.set(true); 
        this.loading.set(false); 
        console.error("Erro ao carregar autores");

        setTimeout(() => {
          this.error.set(false);
        }, 3000);
      }
    });
  }
}