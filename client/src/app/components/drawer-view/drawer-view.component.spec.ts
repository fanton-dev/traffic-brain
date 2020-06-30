import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DrawerViewComponent } from './drawer-view.component';

describe('DrawerViewComponent', () => {
  let component: DrawerViewComponent;
  let fixture: ComponentFixture<DrawerViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DrawerViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DrawerViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
