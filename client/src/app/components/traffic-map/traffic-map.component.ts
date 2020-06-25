import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'traffic-map',
  templateUrl: './traffic-map.component.html',
  styleUrls: ['./traffic-map.component.scss']
})

export class TrafficMapComponent implements OnInit {
  latitude: number = 42.690546;
  longitude: number = 23.337446;
  zoom: number = 16;
  styles = require("./traffic-map-style.json");
  traffic_light_pool = require("../../../assets/demo-pool.json");

  constructor() {
  }

  ngOnInit() {
  }

}
