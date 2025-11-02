module ImageProcessing {
    
    sequence<byte> ImageBytes;
    
    interface ImageProcessor {

        ImageBytes Color2BW(ImageBytes colorImage);
    }
}