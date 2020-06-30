import { environment } from '../environments/environment';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { AgmCoreModule } from '@agm/core';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { TrafficMapComponent } from './components/traffic-map/traffic-map.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSidenavModule, MatCardModule, MatTabsModule, MatButtonToggleModule, MatDatepickerModule, MatNativeDateModule, MatFormFieldModule, MatInputModule, MatSelectModule } from '@angular/material';
import { DrawerViewComponent } from './components/drawer-view/drawer-view.component';
import { ReactiveFormsModule } from '@angular/forms';
import { ChartsModule } from 'ng2-charts';
import { CamerasComponent } from './components/drawer-view/cameras/cameras.component';
import { StatisticsComponent } from './components/drawer-view/statistics/statistics.component';
import { SettingsComponent } from './components/drawer-view/settings/settings.component';

@NgModule({
  declarations: [
    AppComponent,
    TrafficMapComponent,
    NavbarComponent,
    DrawerViewComponent,
    CamerasComponent,
    StatisticsComponent,
    SettingsComponent
  ],
  imports: [
    BrowserModule,
    AgmCoreModule.forRoot({
      apiKey: environment.google_maps_api_key
    }),
    FontAwesomeModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatCardModule,
    MatTabsModule,
    MatButtonToggleModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    ReactiveFormsModule,
    ChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
