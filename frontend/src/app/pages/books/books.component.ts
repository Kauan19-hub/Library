import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { BooksService } from '../../services/books.services';
import { Book } from '../../models/book';
import { AuthService } from '../../services/auth.services';
import { environment } from '../../../environments/environments';

@Component({
  selector: 'app-books',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './books.component.html',
})
export class BooksComponent {
  readonly error = signal(false);

  private svc = inject(BooksService);
  private auth = inject(AuthService);

  books = signal<Book[]>([]);
  loading = signal(true);
  apiBase = (environment.apiBase ?? '').replace(/\/+$/, '');

  private pending = new Map<number, File>();
  private previews = new Map<number, string>();
  private upStatus = new Map<number, 'idle' | 'up' | 'ok' | 'err'>();

  constructor() {
    this.svc.list({ ordering: 'title' }).subscribe({
      next: (data) => {
        this.books.set(data);
        this.loading.set(false);
      },
      error: () => {
        this.error.set(true);
        this.loading.set(false);
        console.error("Erro ao carregar livros");

        setTimeout(() => {
          this.error.set(false);
        }, 3000);
      },
    });
  }

  fileInputId(id: number): string {
    return `file-cover-${id}`;
  }

  coverSrc(l: Partial<Book> & { id?: number }): string | null {
    const lid = Number(l?.id ?? (l as any)?.pk ?? -1);
    const prv = this.previews.get(lid);

    if (prv) return prv;

    const anyL = l as any;
    if (anyL?.cover_url) return String(anyL.cover_url);

    if (l.cover) {
      const rel = String(l.cover);
      const path = rel.startsWith('/media/') ? rel : `/media/${rel}`;
      return `${this.apiBase}${path}`;
    }
    return null;
  }

  statusUpload(id: number): 'idle' | 'up' | 'ok' | 'err' {
    return this.upStatus.get(id) ?? 'idle';
  }

  async onSelect(e: Event, id: number) {
    const file = (e.target as HTMLInputElement).files?.[0];
    if (!file) return;

    const url = URL.createObjectURL(file);
    const old = this.previews.get(id) || null;
    
    this.previews.set(id, url);
    this.pending.set(id, file);
    this.upStatus.set(id, 'up');
    this.svc.sendCover(id, file).subscribe({
      next: (bookUpdated) => {
        this.books.update((arr) =>
          arr.map((l) =>
            Number((l as any).id ?? (l as any).pk) === id
              ? bookUpdated
              : l
          )
        );
        this.upStatus.set(id, 'ok');
        this.pending.delete(id);

        setTimeout(() => {
          const u = this.previews.get(id);
          if (u && u.startsWith('blob:')) URL.revokeObjectURL(u);
          this.previews.delete(id);
        }, 3000);
      },

      error: (err) => {
        console.error("Falha ao enviar capa");
        this.upStatus.set(id, 'err');

        const u = this.previews.get(id);

        if (u && u.startsWith('blob:')) URL.revokeObjectURL(u);
        if (old) this.previews.set(id, old);
        else this.previews.delete(id);

        this.error.set(true);

        setTimeout(() => {
          this.error.set(false);
        }, 3000);
      },
    });
  }
}
