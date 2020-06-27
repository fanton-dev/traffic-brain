import { Component, OnInit } from '@angular/core';
import { faMap, faChartBar, faTrafficLight, faUsers, faCog, faSignOutAlt, faUser } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})

export class NavbarComponent implements OnInit {
  fa = {
    profile: faUser,
    map: faMap,
    chart: faChartBar,
    traffic_light: faTrafficLight,
    users: faUsers,
    settings: faCog,
    signout: faSignOutAlt
  }

  constructor() { }

  ngOnInit() {
  }

}
