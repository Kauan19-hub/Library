import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageService, Image } from '../../services/images.services';
import { enviroment } from '../../../environments/environments.prod';

@Component({
  standalone: true,
  selector: 'app-images',
  imports: [CommonModule],
  templateUrl: './image.components.html',
})

export class ImagesComponent {
  private svc = inject(ImageService);
  images = signal<Image[]>([]);
  status = '';
  file: File | null = null;
  preview: string | null = null;
  apiBase = enviroment.apiBase

  load() {
    this.svc.list().subscribe({
      next: (data: any) => {
        this.images.set(Array.isArray(data) ? data : data.results ?? []);
      },
      error: () => this.status = 'Falha ao carregar imagens'
    });
  }

  onFile(e: Event) {
    const input = e.target as HTMLInputElement;
    this.file = input.files?.[0] ?? null;

    if (this.file) {
      const reader = new FileReader();
      reader.onload = () => this.preview = reader.result as string;
      reader.readAsDataURL(this.file);
    } else {
      this.preview = null;
    }
  }

  onSubmit(ev: Event) {
    ev.preventDefault();
    if (!this.file) return;
    this.status = 'Enviando...';

    this.svc.send(this.file).subscribe({
      next: (img) => {
        this.status = 'Imagem enviada';
        this.file = null;
        this.preview = null;
        this.images.update((arr) => [img, ...arr]);
      },
      error: (err) => {
        console.error(err);
        this.status = 'Falha ao enviar';
      }
    });
  }

  remove(id: number) {
    this.svc.delete(id).subscribe({
      next: () => this.images.update((arr) => arr.filter(i => i.id !== id)),
      error: () => this.status = 'Falha ao remover'
    });
  }
}
