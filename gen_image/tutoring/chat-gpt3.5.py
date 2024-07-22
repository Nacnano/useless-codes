from PIL import Image, ImageDraw, ImageFont

def draw_text_with_wrapping(draw, text, position, font, max_width):
    lines = []
    words = text.split()
    line = ""
    
    for word in words:
        test_line = f"{line} {word}".strip()
        width, _ = draw.textsize(test_line, font=font)
        if width <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    
    if line:
        lines.append(line)
    
    y = position[1]
    for line in lines:
        draw.text((position[0], y), line, font=font, fill=(0, 51, 102))
        y += font.getsize(line)[1] + 10
    
    return y

# Create a blank image with a light blue background
img = Image.new('RGB', (1080, 1080), color = (173, 216, 230))
d = ImageDraw.Draw(img)

# Load a font
font_path = "gen_image/font/SaoChingcha-Bold.otf"
title_font = ImageFont.truetype(font_path, 70)
body_font = ImageFont.truetype(font_path, 40)

# Title text
title_text = "Ace Your Studies with Expert Tutoring!"
d.text((50, 50), title_text, font=title_font, fill=(0, 51, 102))

# Draw a rounded rectangle as a border for the body text
border_x0, border_y0, border_x1, border_y1 = 30, 130, 1050, 1050
d.rounded_rectangle([border_x0, border_y0, border_x1, border_y1], radius=20, outline=(0, 51, 102), width=5)

# Body text
body_text = (
    "Subjects: Math, Physics, Computer Science, English\n"
    "Tutor: Highly experienced with top scores and academic excellence\n\n"
    "Achievements:\n"
    "- Med Exam Score: 72.47 (Med Chula Cutoff 66.82)\n"
    "- Eng Exam Score: 78.63\n"
    "- TGAT: 87.92, TPAT3: 88\n"
    "- PAT1: 267, PAT2: 260\n"
    "- General Math: 86, Physics: 88\n"
    "- Medical Aptitude: 215.95\n"
    "- SAT Math: 800\n"
    "- SAT Subject: 800 in Math, Physics, Chemistry\n"
    "- 1st places in TCASTER and Dek-D (3 subjects)\n"
    "- Offered Ministry of Science scholarship for CS in US (declined)\n"
    "- Almost won King’s scholarship\n"
    "- Received an offer from ISE, Chulalongkorn University (declined)\n"
    "- Perfect GPA: 4.00 in all university and high school courses\n"
    "- Participated in Computer Olympiad camp\n"
    "- Passed first round of National Science Olympiad in Math and Physics (declined)"
)

# Split the body text into lines
lines = body_text.split('\n')

# Draw the body text within the border
y_text = 160
for line in lines:
    d.text((50, y_text), line, font=body_font, fill=(0, 51, 102))
    y_text += 50  # Adjust the line height as needed

# Draw some decorative icons or elements
# Example: Add a star icon for achievements
star_icon_path = "gen_image/tutoring/icons/star.png"
star_icon = Image.open(star_icon_path).resize((40, 40))

for i in range(12):
    img.paste(star_icon, (1000, 240 + i*50), star_icon)

# Add profile image
profile_img_path = "gen_image/tutoring/oong-oong-cropped.jpg"
profile_img = Image.open(profile_img_path).resize((200, 200))
img.paste(profile_img, (850, 50))

# Save the image
img.save('gen_image/tutoring/tutoring_session_post.png')
