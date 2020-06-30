import { Component, OnInit } from '@angular/core';
import styles from './traffic-map-style.json';
import traffic_light_pools from '../../../assets/demo-pool.json';
import { faTimesCircle } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'traffic-map',
  templateUrl: './traffic-map.component.html',
  styleUrls: ['./traffic-map.component.scss']
})

export class TrafficMapComponent implements OnInit {
  latitude: number = 42.690546;
  longitude: number = 23.337446;
  zoom: number = 16;
  styles: any = styles;
  traffic_light_pools: any = traffic_light_pools;
  current_drawer_pool: number = 0;
  fa = {
    close: faTimesCircle,
  }

  constructor() {
  }

  ngOnInit() {
  }

}
