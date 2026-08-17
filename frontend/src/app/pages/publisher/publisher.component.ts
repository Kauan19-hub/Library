import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { PublishersService } from '../../services/publishers.services';
import { Publisher } from '../../models/publisher';
import { AuthService } from '../../services/auth.services';

@Component({
  selector: 'app-publisher.component',
  imports: [RouterLink],
  templateUrl: './publisher.component.html',
  styleUrls: ['./publisher.component.css']
})
export class PublisherComponent {
  readonly error = signal(false);

  private svc = inject(PublishersService);
  private auth = inject(AuthService);

  publishers = signal<Publisher[]>([]);
  loading = signal(true);

  constructor() {
      this.svc.list().subscribe({
      next: (data) => { 
        this.publishers.set(data); 
        this.loading.set(false); 
      },

      error: () => { 
        this.error.set(true); 
        console.error("Erro ao carregar editoras")

        setTimeout(() => {
          this.error.set(false);
        }, 3000);
      }
    });
  }
}
