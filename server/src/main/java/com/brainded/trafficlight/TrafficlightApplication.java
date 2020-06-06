package com.brainded.trafficlight;

import com.brainded.trafficlight.storage.StorageProperties;
import com.brainded.trafficlight.storage.StorageService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.boot.autoconfigure.jdbc.DataSourceTransactionManagerAutoConfiguration;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;

import java.awt.*;
import java.io.IOException;

//@Configuration
//@EnableAutoConfiguration
//@ComponentScan
@SpringBootApplication(exclude = {
        DataSourceAutoConfiguration.class,
        DataSourceTransactionManagerAutoConfiguration.class,
        HibernateJpaAutoConfiguration.class
})
@EnableConfigurationProperties({StorageProperties.class})
public class TrafficlightApplication {

    public static void main(String[] args) throws IOException {
        ImageResizer.resize("/home/bogdan8/Desktop/DataTest.jpg"); //LOCATION OF IMG

//        SpringApplication.run(TrafficlightApplication.class, args);
    }

    @Bean
    CommandLineRunner init(StorageService storageService) {
        return (args) -> {
            storageService.deleteAll();
            storageService.init();
        };
    }
}
