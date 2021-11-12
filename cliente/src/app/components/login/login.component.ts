import { Component, OnInit } from '@angular/core';
import { Login } from 'src/app/models/Login';
import { LoginService } from 'src/app/services/login.service';
import { Router, ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  datos:Login={
    user:'',
    password:'',
  };

  resp:any={
    auth:false,
    mensaje:""
  }
  constructor(private loginService:LoginService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
  }

  iniciarSesion(){
    this.loginService.iniciarSesion(this.datos).subscribe(
      res=>{
        console.log(res);
        this.resp=res;
        if(this.resp.auth ==true){
          this.router.navigate(['/home'])
        }
      },
      err=> console.error(err)
    )
    }
}
