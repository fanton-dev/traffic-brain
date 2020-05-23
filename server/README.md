# Main controlling server
> The main server is the brain of the whole project. It is used to communicate with each and every traffic light node, the object recognition model deployed in GCE and the front-end control panel.

<p align="center">
<a href="https://github.com/braind3d/traffic-brain/actions?query=workflow%3A%22Server+CI">
<img src="https://img.shields.io/github/workflow/status/braind3d/traffic-brain/Server+CI?style=flat-square" alt="Server CI status">
</a>

<a href="https://github.com/braind3d/traffic-brain/issues?q=is%3Aopen+is%3Aissue+label%3Aserver">
<img src="https://img.shields.io/github/issues-raw/braind3d/traffic-brain/server?label=open%20issues&style=flat-square" alt="Server open issues badge">
</a>

<a href="https://github.com/braind3d/traffic-brain/issues?q=is%3Aissue+label%3Aserver+is%3Aclosed">
<img src="https://img.shields.io/github/issues-closed-raw/braind3d/traffic-brain/server?label=closed%20issues&style=flat-square" alt="Server closed issues badge">
</a>

<a href="LICENSE">
<img src="https://img.shields.io/github/license/braind3d/traffic-brain?style=flat-square" alt="License badge">
</a>
</p>

## Built With
* 	[Maven](https://maven.apache.org/) - Dependency Management
* 	[Flyway](https://flywaydb.org/) - Version control for database
* 	[JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) - Java™ Platform, Standard Edition Development Kit 
* 	[Spring Boot](https://spring.io/projects/spring-boot) - Framework to ease the bootstrapping and development of new Spring Applications
* 	[MySQL](https://www.mysql.com/) - Open-Source Relational Database Management System
* 	[git](https://git-scm.com/) - Free and Open-Source distributed version control system 
* 	[Thymeleaf](https://www.thymeleaf.org/) - Modern server-side Java template engine for both web and standalone environments.
* 	[Prometheus](https://prometheus.io/) - Monitoring system and time series database
* 	[Lombok](https://projectlombok.org/) - Never write another getter or equals method again, with one annotation your class has a fully featured builder, Automate your logging variables, and much more.
* 	[Swagger](https://swagger.io/) - Open-Source software framework backed by a large ecosystem of tools that helps developers design, build, document, and consume RESTful Web services.


## Get started
There are several ways to run a Spring Boot application on your local machine. One way is to execute the `main` method in the `com.braind3d.traffic-brain.Server` class from your IDE.

- Download the zip or clone the Git repository.
- Unzip the zip file (if you downloaded one)
- Open Command Prompt and Change directory (cd) to folder containing pom.xml
- Open Eclipse 
   - File -> Import -> Existing Maven Project -> Navigate to the folder where you unzipped the zip
   - Select the project
- Choose the Spring Boot Application file (search for @SpringBootApplication)
- Right Click on the file and Run as Java Application

Alternatively you can use the [Spring Boot Maven plugin](https://docs.spring.io/spring-boot/docs/current/reference/html/build-tool-plugins-maven-plugin.html) like so:

```shell
mvn spring-boot:run
```

### Security

```
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

Spring Boot Starter Security default username is `user` and a generated security password is printed in the console like `Using generated security password: 0423bec1-6759-4ed2-8e3e-e8196effadf9`

Automated dependency updates done via [Dependabot](https://dependabot.com/)

### Actuator

To monitor and manage your application

|  URL |  Method |
|----------|--------------|
|`http://localhost:8080`  						| GET |
|`http://localhost:8080/actuator/`             | GET |
|`http://localhost:8080/actuator/health`    	| GET |
|`http://localhost:8080/actuator/info`      	| GET |
|`http://localhost:8080/actuator/prometheus`| GET |
|`http://localhost:8080/actuator/httptrace` | GET |

### URLs

|  URL |  Method | Remarks |
|----------|--------------|--------------|
|`http://localhost:8080/bw/tech-stack`                           | GET | Custom Response Headers|
|`http://localhost:8080/api/generic-hello`                       | GET | |
|`http://localhost:8080/api/personalized-hello/`                 | GET | |
|`http://localhost:8080/api/personalized-hello?name=spring-boot` | GET | |
|`http://localhost:8080/api/loggers`                             | GET | |

### Person URLs

|  URL |  Method | Remarks |
|----------|--------------|--------------|
|`http://localhost:8080/api/person`                           | GET | Header `Accept:application/json` or `Accept:application/xml` for content negotiation|
|`http://localhost:8080/api/person/1`                       | GET | |

## Documentation
* [Postman Collection](https://documenter.getpostman.com/view/2449187/RWTiwzb2) - online, with code auto-generated snippets in cURL, jQuery, Ruby,Python Requests, Node, PHP and Go programming languages
* [Postman Collection](https://github.com/AnanthaRajuC/Spring-Boot-Application-Template/blob/master/Spring%20Boot%20Template.postman_collection.json) - offline
* [Swagger](http://localhost:8088/swagger-ui.html) - Documentation & Testing

## Files and Directories

The project (a.k.a. project directory) has a particular directory structure. A representative project is shown below:

```
.
├── Spring Elements
├── src
│   └── main
│       └── java
│           ├── com.arc.application
│           ├── com.arc.application.config
│           ├── com.arc.application.controller
│           ├── com.arc.application.exception
│           ├── com.arc.application.model
│           ├── com.arc.application.util
│           ├── com.arc.application.repository
│           └── com.arc.application.service
├── src
│   └── main
│       └── resources
│           └── static
│           │   ├── css
│           │   │   └── bootstrap.css
│           │   ├── images
│           │   ├── js
│           │   ├── favicon.ico
│           │   └── index.html
│           ├── templates
│           │   └── view.html
│           ├── application.properties
│           ├── banner.txt
│           └── log4j2.xml
├── src
│   └── test
│       └── java
├── JRE System Library
├── Maven Dependencies
├── bin
├── logs
│   └── application.log
├── src
├── target
│   └──application-0.0.1-SNAPSHOT
├── mvnw
├── mvnw.cmd
├── pom.xml
└── README.md
```

## packages

- `models` — to hold our entities;
- `repositories` — to communicate with the database;
- `services` — to hold our business logic;
- `security` — security configuration;
- `controllers` — to listen to the client;

- `resources/` - Contains all the static resources, templates and property files.
- `resources/static` - contains static resources such as css, js and images.
- `resources/templates` - contains server-side templates which are rendered by Spring.
- `resources/application.properties` - It contains application-wide properties. Spring reads the properties defined in this file to configure your application. You can define server’s default port, server’s context path, database URLs etc, in this file.

- `test/` - contains unit and integration tests

- `pom.xml` - contains all the project dependencies
 
## Reporting Issues

This Project uses GitHub's integrated issue tracking system to record bugs and feature requests. If you want to raise an issue, please follow the recommendations below:

* Before you log a bug, please https://github.com/braind3d/traffic-brain/search?type=Issues[search the issue tracker]
  to see if someone has already reported the problem.
* If the issue doesn't already exist, https://github.com/braind3d/traffic-brain/issues/new[create a new issue]. 
* Please provide as much information as possible with the issue report.
* If you need to paste code, or include a stack trace use Markdown +++```+++ escapes before and after your text. 

## License
Distributed under the MIT license. See [LICENSE](../LICENSE) for more informat