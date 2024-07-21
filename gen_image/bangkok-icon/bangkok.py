from PIL import Image, ImageDraw, ImageFont

# Function to create favicon
def create_favicon():
    # Set the size and colors
    size = (32, 32)
    background_color = (0, 128, 0)  # Green background
    text_color = (255, 255, 255)  # White text

    # Create a new image with a transparent background
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw a green circle using the mask
    draw.ellipse([(0, 0), size], fill=background_color)

    # Load a font that supports Thai characters
    font_path = "gen_image/font/SaoChingcha-Bold.otf"
    font_size = 14  # Reduced font size for better fit
    font = ImageFont.truetype(font_path, font_size)

    # Define the text and get its size
    text = "กทม"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Calculate the position to center the text
    text_position = ((size[0] - text_width) // 2 + 1, (size[1] - text_height) // 2 - 1)

    # Draw the text onto the image
    draw.text(text_position, text, font=font, fill=text_color)


    # Save the image to a file
    favicon_path = "gen_image/favicon.png"
    image.save(favicon_path)
    print(f"Favicon saved to {favicon_path}")

# Call the function to create the favicon
create_favicon()
