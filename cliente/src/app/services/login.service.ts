import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Login } from '../models/Login';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  
  API_URI='http://localhost:3000/';

  constructor(private http: HttpClient) { }

  iniciarSesion(login:Login){
    return this.http.post(`${this.API_URI}iniciarSesion`, login);
  }
}

