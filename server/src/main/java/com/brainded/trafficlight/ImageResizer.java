package com.brainded.trafficlight;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class ImageResizer {

    private static int scaledWidth = 512;
    private static int scaledHeight = 512;

    /**
     * Resizes an image to a absolute width and height (the image may not be
     * proportional)
     *
     * @param inputImagePath  Path of the original image
     * @throws IOException
     */
    public static int[][][] resize(String inputImagePath)
            throws IOException {

        // reads input image
        File inputFile = new File(inputImagePath);
        BufferedImage inputImage = ImageIO.read(inputFile);

        // creates output image
        BufferedImage outputImage = new BufferedImage(scaledWidth,
                scaledHeight, inputImage.getType());

        // scales the input image to the output image
        Graphics2D g2d = outputImage.createGraphics();
        g2d.drawImage(inputImage, 0, 0, scaledWidth, scaledHeight, null);
        g2d.dispose();


        int[][][] img = new int[512][512][3];

        for (int i = 0; i < 512; ++i) {
            for (int j = 0; j < 512; ++j) {
                Color pixelColor = new Color(outputImage.getRGB(i, j));

                img[i][j][0] = pixelColor.getRed() / 255;
                img[i][j][1] = pixelColor.getGreen() / 255;
                img[i][j][2] = pixelColor.getBlue() / 255;
            }
        }

        return img;
    }
}
