from PIL import Image
import stepic

def encode(image_path, message):
    # Open the image
    im = Image.open(image_path)

    # Encode the message using steganography
    im1 = stepic.encode(im, message)

    # Save the modified image
    im1.save('modified_image.png', 'PNG')

def decode(image_path):
    # Open the image
    image = Image.open(image_path)

    # Decode the message using steganography
    message = stepic.decode(image)

    return message

if __name__ == '__main__':
    # Encode the message
    image_path = "cover.png"
    message = b'Test Message'
    encode(image_path, message)
    print('Message encoded successfully in the image.')

    # Decode the message
    image_path = 'modified_image.png'
    message = decode(image_path)
    print('Decoded message:', message)
