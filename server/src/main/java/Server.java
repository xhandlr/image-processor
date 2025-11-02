import com.zeroc.Ice.*;

public class Server {
    public static void main(String[] args) {
        try (Communicator communicator = Util.initialize(args)) {
            ObjectAdapter adapter = communicator.createObjectAdapterWithEndpoints(
                    "ImageProcessorAdapter",
                    "default -h localhost -p 10000"
            );

            ImageProcessing.ImageProcessor servant = new ImageProcessorI();
            adapter.add((com.zeroc.Ice.Object) servant, Util.stringToIdentity("ImageProcessor"));
            adapter.activate();

            System.out.println("Servidor iniciado...");
            communicator.waitForShutdown();
        }
    }
}