//package com.brainded.trafficlight.service;
//
//import com.google.gson.Gson;
//import org.springframework.stereotype.Service;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.net.HttpURLConnection;
//import java.net.MalformedURLException;
//import java.net.URL;
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.Map;
//
//@Service
//public class AIService {
//
//    public static final String ADDRESS = "";
//    public static final double MIN_SCORE = 0.5;
//    public static final double MIN_IOU = 0.45;
//
//    static URL url;
//
//    static {
//        try {
//            url = new URL(ADDRESS);
//        } catch (MalformedURLException e) {
//            e.printStackTrace();
//        }
//    }
//
//    public static void postPicture() {
//        try {
//            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
//            connection.setRequestMethod("POST");
//
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }
//
//    public static int[][][][] getPrediction() throws IOException { //TODO Decide what to do when connection fails
//        int[][][][] responseValue = null;
//
//        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
//        connection.setRequestMethod("GET");
//
//        connection.setRequestProperty("Content-Type", "application/json");
//
//        int status = connection.getResponseCode();
//
//
//        if (status == 200) {
//            BufferedReader in = new BufferedReader(
//                    new InputStreamReader(connection.getInputStream()));
//            String inputLine;
//            StringBuilder content = new StringBuilder();
//            while ((inputLine = in.readLine()) != null) {
//                content.append(inputLine);
//            }
//            in.close();
//
//            Gson gson = new Gson();
//            Map map = gson.fromJson(content.toString(), Map.class);
//
//            responseValue = (int[][][][]) map.values().toArray(new int[16][16][5][12]);
//        } else {
//            System.out.println("Failed to retrieve prediction, error message: " + status);
//        }
//
//        connection.disconnect();
//        return responseValue;
//    }
//
//    public static HashMap<String, Integer> parseResponse() throws IOException {
//        Map<String, Integer> FoundObjects = Map.of("bicycle", 0,
//                                                    "bus", 0,
//                                                    "car", 0,
//                                                    "horse", 0,
//                                                    "motorbike", 0,
//                                                    "person", 0,
//                                                    "train", 0);
//
//        int[][][][] AIResponse = getPrediction();
//
//        for (int i = 0; i < 16; i++) {
//            for (int j = 0; j < 16; j++) {
//                int[][] cell = AIResponse[i][j];
//                //A bounding box prediction is with size 5 (x of box center, y of box center, w of the box, h of the box, probability that an object exists in this box) + 7 probabilities of a given class existing in the grid cell (classes listed here)
//
//            }
//        }
//
//    }
//
//}
