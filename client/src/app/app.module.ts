import { environment } from '../environments/environment';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { TrafficMapComponent } from './components/traffic-map/traffic-map.component';

import { AgmCoreModule } from '@agm/core';

@NgModule({
  declarations: [
    AppComponent,
    TrafficMapComponent
  ],
  imports: [
    BrowserModule,
    AgmCoreModule.forRoot({
      apiKey: environment.google_maps_api_key
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
