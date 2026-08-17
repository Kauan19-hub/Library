import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AuthorsPage} from './pages/authors/authors.component';
import { BooksComponent } from './pages/books/books.component';
import { PublisherComponent } from './pages/publisher/publisher.component';
import { LoginComponent } from './pages/login/login.component';
import { authGuard } from './auth.guard';
import { ImagesComponent } from './pages/image/image.components';

export const routes: Routes = [
    {path: '', component: LoginComponent},
    {path: 'login', component: LoginComponent},
    {path: 'home', component: HomeComponent},
    {path: 'authors', component: AuthorsPage, canActivate: [authGuard]},
    {path: 'publishers', component: PublisherComponent, canActivate: [authGuard]},
    {path: 'books', component: BooksComponent, canActivate: [authGuard]},
    {path: 'images', component: ImagesComponent}
    
];