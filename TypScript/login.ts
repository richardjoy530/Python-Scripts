import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  login(event:any){
    console.log(event.target.username.value)
    var username = event.target.username.value
    var password = event.target.password.value
  }
}
