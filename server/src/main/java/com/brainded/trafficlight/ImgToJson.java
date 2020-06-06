//package com.brainded.trafficlight;
//
//import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
//import com.google.api.client.http.*;
//import com.google.api.client.json.JsonFactory;
//import com.google.api.client.json.jackson2.JacksonFactory;
//import com.google.api.services.discovery.Discovery;
//import com.google.api.services.discovery.model.JsonSchema;
//import com.google.api.services.discovery.model.RestDescription;
//import com.google.api.services.discovery.model.RestMethod;
//import com.google.auth.http.HttpCredentialsAdapter;
//import com.google.auth.oauth2.AccessToken;
//import com.google.auth.oauth2.GoogleCredentials;
//
//import java.io.File;
//import java.util.Date;
//
//public class ImgToJson {
//    public static String Convert(int[][][] image) throws Exception {
//        HttpTransport httpTransport = GoogleNetHttpTransport.newTrustedTransport();
//        JsonFactory jsonFactory = JacksonFactory.getDefaultInstance();
//        Discovery discovery = new Discovery.Builder(httpTransport, jsonFactory, null).build();
//
//        RestDescription api = discovery.apis().getRest("ml", "v1").execute();
//        RestMethod method = api.getResources().get("projects").getMethods().get("predict");
//
//        JsonSchema param = new JsonSchema();
//        String projectId = "traffic-brain";
//        // You should have already deployed a model and a version.
//        // For reference, see https://cloud.google.com/ml-engine/docs/deploying-models.
//        String modelId = "traffic_brain_classification";
//        String versionId = "tb__2020_06_03__17_20_35";
//        param.set("name", String.format("projects/%s/models/%s/versions/%s", projectId, modelId, versionId));
//
//        GenericUrl url =
//                new GenericUrl(UriTemplate.expand(api.getBaseUrl() + method.getPath(), param, true));
//        System.out.println(url);
//
//        String contentType = "application/json";
////        File requestBodyFile = new File();
////        var jsonImg = JsonConvert.SerializeObject();
////        HttpContent content = new FileContent(contentType, requestBodyFile);
//        System.out.println(content.getLength());
//
//        GoogleCredentials credential = GoogleCredentials.getApplicationDefault();
////        GoogleCredentials credential = GoogleCredentials.create(new AccessToken("AIzaSyAV_jgJVuCk6EkGFsT0tnhRxobcRlYsHRs", new Date(2019, 8, 16))); //ACCESS TOKEN
//
//        HttpRequestInitializer requestInitializer = new HttpCredentialsAdapter(credential);
//
//        HttpRequestFactory requestFactory = httpTransport.createRequestFactory(requestInitializer);
//        HttpRequest request = requestFactory.buildRequest(method.getHttpMethod(), url, content);
//
//        String response = request.execute().parseAsString();
//        System.out.println(response);
//        return response;
//    }
//}
//
