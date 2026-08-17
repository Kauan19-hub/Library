import { Component, inject,  signal } from '@angular/core';
import { RouterLink, Router } from '@angular/router';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.services';

@Component({
  selector: 'app-login.component',
  standalone: true,
  imports: [RouterLink, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})

export class LoginComponent {
  readonly error = signal(false);

  private fb = inject(FormBuilder);
  private auth = inject(AuthService);
  private router = inject(Router);

  loading = signal(false)
  form = this.fb.group({username: ['', [Validators.required]], password: ['', [Validators.required]]})

  onSubmit() {
    if (this.form.invalid) return

    this.loading.set(true)

    const {username, password} = this.form.value as {username: string, password: string}

    this.auth.login(username, password).subscribe({
      next: () => {
        this.loading.set(false)
        this.router.navigateByUrl('/home')
      },

      error: (e) => {
        this.loading.set(false)
        this.error.set(true)
        console.error("Usuário ou senha inválido");

        setTimeout(() => {
          this.error.set(false);
        }, 3000);
      }
    })
  }
}