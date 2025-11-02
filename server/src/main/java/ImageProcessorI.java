import ImageProcessing.ImageProcessor;
import com.zeroc.Ice.Current;
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

public class ImageProcessorI implements ImageProcessor {
    @Override
    public byte[] Color2BW(byte[] colorImage, Current current) {
        try {
            ByteArrayInputStream bais = new ByteArrayInputStream(colorImage);
            BufferedImage img = ImageIO.read(bais);

            System.out.println("Procesando imagen de " + colorImage.length + " bytes");

            BufferedImage bwImg = new BufferedImage(img.getWidth(), img.getHeight(), BufferedImage.TYPE_BYTE_GRAY);
            Graphics g = bwImg.getGraphics();
            g.drawImage(img, 0, 0, null);
            g.dispose();

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(bwImg, "png", baos);
            return baos.toByteArray();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}