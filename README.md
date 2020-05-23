# Traffic Brain
> Traffic Brain is an open-source traffic light control system. Using a classifier, information about the current road situation is collected and automated light switch decision is made based on it.

<p align="center">
<img src="docs/img/Export/Banner_(3840x2160).png" alt="Project Banner">
</p>


<p align="center">
<a href="https://github.com/braind3d/traffic-brain/actions?query=workflow%3A%22Classification+CI">
<img src="https://img.shields.io/github/workflow/status/braind3d/traffic-brain/Classification+CI?label=classification+ci&style=flat-square" alt="Classification CI">
</a>

<a href="https://github.com/braind3d/traffic-brain/actions?query=workflow%3A%22Server+CI">
<img src="https://img.shields.io/github/workflow/status/braind3d/traffic-brain/Server+CI?label=server+ci&style=flat-square" alt="Server CI status">
</a>

<a href="https://github.com/braind3d/traffic-brain/actions?query=workflow%3A%22Embedded+CI">
<img src="https://img.shields.io/github/workflow/status/braind3d/traffic-brain/Embedded+CI?label=embedded+ci&style=flat-square" alt="Embedded CI status">
</a>

<a href="https://github.com/braind3d/traffic-brain/actions?query=workflow%3A%22Client+CI">
<img src="https://img.shields.io/github/workflow/status/braind3d/traffic-brain/Client+CI?label=client+ci&style=flat-square" alt="Client CI status">
</a>
</p>


<p align="center">
<a href="https://github.com/braind3d/traffic-brain">
<img src="http://hits.dwyl.com/braind3d/traffic-brain.svg" alt="Hit count badge">
</a>

<a href="https://github.com/braind3d/traffic-brain/issues?q=is%3Aissue+is%3Aopen">
<img src="https://img.shields.io/github/issues-raw/braind3d/traffic-brain?style=flat-square" alt="Open issues status badge">
</a>

<a href="https://github.com/braind3d/traffic-brain/issues?q=is%3Aissue+is%3Aclosed">
<img src="https://img.shields.io/github/issues-closed-raw/braind3d/traffic-brain?style=flat-square" alt="Closed issues status badge">
</a>

<a href="https://github.com/braind3d/traffic-brain/fork">
<img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square" alt="Contributions welcome badge">
</a>

<a href="LICENSE">
<img src="https://img.shields.io/github/license/braind3d/traffic-brain?style=flat-square" alt="License badge">
</a>
</p>


## Get started
<p align="center">
<img src="docs/img/Export/Architecture.png" alt="Project Architecture">
</p>


The project consists of 4 main components:
- **Object recognition** for traffic detection (located in "[/classification](/classification)")
- **Main server** controlling all the traffic light nodes (located in "[/server](/server)")
- **Embedded server** and **traffic light schematics** (located in "[/embedded](/embedded)")
- **Front-end client** for communicating with the server (still incomplete; located in "[/client](/client)")

For each of the components' directories there is a coresponding `README.md` with instructions on how to get started.

## Authors
- **Angel Penchev** ([@angel-penchev](https://github.com/angel-penchev)) - Object detection neural network, Embedded traffic light
- **Bogdan Mironov** ([@bogdanmironov](https://github.com/bogdanmironov)) - Main controlling server
- **Simeon Georgiev** ([@simo1209](https://github.com/simo1209)) - Thank you for helping me out to complete the embedded <3

## Contributions
1. Fork it (<https://github.com/braind3d/traffic-brain/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -a`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
6. Upon review it will be merged.

## License
Distributed under the MIT license. See [LICENSE](LICENSE) for more information.