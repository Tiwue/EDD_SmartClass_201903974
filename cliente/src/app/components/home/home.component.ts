import { Component, OnInit } from '@angular/core';
import { SesionService } from 'src/app/services/sesion.service';
import { Router, ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  resp:any={
    auth:0,
    mensaje:""
  }

  constructor(private sesionService: SesionService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    
    this.sesionService.getSesion().subscribe(
      res=>{
        this.resp=res;
        if (this.resp.auth== 0){
          this.router.navigate(['/login'])
        }
      },
      err=> console.error(err)
    );
  }

}
