## How to Contribute

## Tech Stack
### GUI Electron

We use Electron + VueJS

- [Electron-vue](https://github.com/SimulatedGREG/electron-vue/)
- [Element](http://element.eleme.io/)

## Install guide

#### GUI Electron
```
$ git clone https://github.com/tealinuxos/modularitea
$ cd modularitea/gui-electron
$ npm install
```

#### CLI
```
$ cd modularitea-cli/
$ sudo python3 setup.py install
```

##### Execute test command
```
$ gksu 'x-terminal-emulator -e /usr/local/bin/modularitea-cli --module=nama_module'
```

#### Run
```
$ npm run dev
```

#### Build
- into .deb

```
$ node_modules/.bin/build --linux deb  
```
