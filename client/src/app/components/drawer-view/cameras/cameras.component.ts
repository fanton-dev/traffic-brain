import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'drawer-cameras',
  templateUrl: './cameras.component.html',
  styleUrls: ['./cameras.component.scss']
})

export class CamerasComponent implements OnInit {
  @Input('traffic_light_pool')
  traffic_light_pool: any;
  
  default_camera_url: string = "https://elsys-bg.org/web/files/carousel/1/image/thumb_1366x0_Home10_b.jpg"
  current_camera_ip: string;
  
  constructor() {
  }
  
  ngOnInit() {
    this.current_camera_ip = this.traffic_light_pool.traffic_lights[0].ip;
  }

}
