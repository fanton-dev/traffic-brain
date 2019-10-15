import { app, BrowserWindow } from 'electron'
import * as path from 'path'
import * as url from 'url'

let win: BrowserWindow;

function createWindow() {
  win = new BrowserWindow({ width: 1440, height: 920 })

  win.loadURL(
    url.format({
      pathname: path.join(__dirname, `/../../dist/client/index.html`),
      protocol: 'file:',
      slashes: true,
    })
  )

  win.webContents.openDevTools()

  win.on('closed', () => {
    win = null
  })
}

// Create window on electron intialization
app.on('ready', createWindow)

app.on('activate', function () {
  // macOS specific close process
  if (win === null) {
    createWindow()
  }
})

// Quit when all windows are closed.
app.on('window-all-closed', function () {

  // On macOS specific close process
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
