import sys
import os
import Ice
import ImageProcessing


def list_images(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} does not exist")
        sys.exit(1)

    images = [f for f in os.listdir(directory)
              if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

    if not images:
        print(f"No images found in {directory}")
        sys.exit(1)

    return images


def select_image(images):
    print("\nAvailable images:")
    for i, img in enumerate(images, 1):
        print(f"{i}. {img}")

    while True:
        try:
            choice = int(input("\nSelect image number: "))
            if 1 <= choice <= len(images):
                return images[choice - 1]
            print("Invalid option")
        except ValueError:
            print("Enter a valid number")


def process_image(proxy, input_path, output_path):
    with open(input_path, "rb") as f:
        image_bytes = f.read()

    print(f"\nProcessing {os.path.basename(input_path)}...")
    result_bytes = proxy.Color2BW(image_bytes)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(bytes(result_bytes))

    print(f"Image saved to: {output_path}")


def main():
    try:
        with Ice.initialize(sys.argv) as communicator:
            proxy_string = "ImageProcessor:tcp -h localhost -p 10000"
            base = communicator.stringToProxy(proxy_string)

            print(f"Proxy: {base}")
            base.ice_ping()
            print("Server responding")

            proxy = ImageProcessing.ImageProcessorPrx.checkedCast(base)
            if not proxy:
                print("Failed to connect")
                sys.exit(1)

            images = list_images("examples")
            selected = select_image(images)

            input_path = os.path.join("examples", selected)
            output_name = f"{os.path.splitext(selected)[0]}_bw.png"
            output_path = os.path.join("results", output_name)

            process_image(proxy, input_path, output_path)

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()