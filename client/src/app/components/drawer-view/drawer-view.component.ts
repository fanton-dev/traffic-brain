import { Component, OnInit, Input } from '@angular/core';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'drawer-view',
  templateUrl: './drawer-view.component.html',
  styleUrls: ['./drawer-view.component.scss']
})


export class DrawerViewComponent implements OnInit {
  @Input('traffic_light_pool')
  traffic_light_pool: any;

  google_maps_api_key: string = environment.google_maps_api_key;

  
  constructor() { }

  ngOnInit() {
  }  
}
