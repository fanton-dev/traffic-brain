import { Component, OnInit, Input } from '@angular/core';
import { FormControl, FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'drawer-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.scss']
})
export class SettingsComponent implements OnInit {
  @Input('traffic_light_pool')
  traffic_light_pool: any;
  
  information_options: FormGroup;
  poolModeControl: FormControl;
  poolNameControl: FormControl;
  poolTypeControl: FormControl;
  poolTrafficLightIPs: FormControl[] = [];

  constructor(fb: FormBuilder) {
    this.information_options = fb.group({
      poolMode: this.poolModeControl,
      poolName: this.poolNameControl,
      poolType: this.poolTypeControl,
      poolTrafficLightIPs: this.poolTrafficLightIPs
    })
  }
  
  ngOnInit() {
    this.poolModeControl = new FormControl(this.traffic_light_pool.mode)
    this.poolNameControl = new FormControl(this.traffic_light_pool.name);
    this.poolTypeControl = new FormControl(this.traffic_light_pool.type);
    
    for (let i = 0; i < this.traffic_light_pool.traffic_lights.length; i++) {
      this.poolTrafficLightIPs[i] = new FormControl(this.traffic_light_pool.traffic_lights[i].ip);
    }

  }
}
