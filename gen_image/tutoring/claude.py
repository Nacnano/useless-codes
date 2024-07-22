from PIL import Image, ImageDraw, ImageFont
import textwrap

# Create a new image with a white background
img_size = (1080, 1080)
background_color = (255, 255, 255)
img = Image.new('RGB', img_size, background_color)

# Create a drawing object
draw = ImageDraw.Draw(img)

# Load fonts with adjusted sizes
font_path = "gen_image/font/SaoChingcha-Bold.otf"
title_font = ImageFont.truetype(font_path, 50)
subtitle_font = ImageFont.truetype(font_path, 30)
body_font = ImageFont.truetype(font_path, 24)

# Load star icon
star_icon_path = "gen_image/tutoring/icons/star.png"
star_icon = Image.open(star_icon_path).convert("RGBA")
star_icon = star_icon.resize((30, 30))

# Load and paste your picture
your_picture_path = "gen_image/tutoring/oong-oong-cropped.jpg"
your_picture = Image.open(your_picture_path).convert("RGBA")
your_picture = your_picture.resize((180, 180))
img.paste(your_picture, (450, 80), your_picture)

# Colors
title_color = (0, 0, 100)  # Dark blue
body_color = (50, 50, 50)  # Dark gray

# Draw title
draw.text((540, 50), "Expert Tutoring", font=title_font, fill=title_color, anchor="mm")
draw.text((540, 280), "Math | Physics | Computer | English", font=subtitle_font, fill=title_color, anchor="mm")

# Draw achievements
achievements = [
    "คะแนนกสพท. 72.47 (ขั้นต่ำแพทย์จุฬา 66.82)",
    "คะแนนวิศวะ 78.63",
    "TGAT 87.92, TPAT3 88",
    "PAT1 267, PAT2 260",
    "วิชาสามัญ: คณิต 86, ฟิสิกส์ 88",
    "ความถนัดแพทย์ 215.95",
    "SAT Math 800",
    "SAT Subject 800 ทุกวิชา (Math, Physics, Chemistry)",
    "ที่ 1 Mock Exam TCASTER และ Dek-D รวม 3 วิชา",
    "ได้ทุนกระทรวงวิทย์ศึกษาต่ออเมริกาด้านวิทยาการคอมพิวเตอร์ (สละสิทธิ์)",
    "ได้ offer จากคณะ ISE จุฬาลงกรณมหาวิทยาลัย (สละสิทธิ์)",
    "ได้เกรด 4.00 ทุกวิชาในมหาลัยจนถึงปัจจุบัน",
    "ได้เกรด 4.00 ทุกวิชาในโรงเรียนมหิดลวิทยานุสรณ์",
    "เข้าค่ายโอลิมปิกคอมพิวเตอร์",
    "สอบผ่านคัดเลือกรอบแรก สอวน. คณิต และฟิสิกส์ (สละสิทธิ์)"
]

y_position = 320
for achievement in achievements:
    # Paste star icon
    img.paste(star_icon, (40, y_position), star_icon)
    
    # Wrap text
    lines = textwrap.wrap(achievement, width=50)
    for line in lines:
        draw.text((80, y_position), line, font=body_font, fill=body_color)
        y_position += 30
    
    y_position += 10

# Draw footer
draw.text((540, 1020), "Book your session now!", font=subtitle_font, fill=title_color, anchor="mm")
draw.text((540, 1060), "Contact: your_email@example.com", font=body_font, fill=body_color, anchor="mm")

# Save the image
img.save("gen_image/tutoring/claude_tutoring_session_post.png")