import csv
import qrcode
import os
from PIL import Image, ImageDraw, ImageFont

# Configuration des chemins
csv_path = "./infos.csv"
output_dir = "qr_students"
os.makedirs(output_dir, exist_ok=True)

# Paramètres BIT
BIT_FONT_SIZE = 40
BIT_TEXT = "BIT"
BIT_GRADIENT_COLORS = ["black", "red", "black"]

def add_bit_watermark(qr_img):
    """Ajoute l'acronyme BIT au centre du QR code avec dégradé"""
    draw = ImageDraw.Draw(qr_img)
    try:
        font = ImageFont.truetype("arial.ttf", BIT_FONT_SIZE)
    except:
        font = ImageFont.load_default()
    
    width, height = qr_img.size
    text_width = draw.textlength(BIT_TEXT, font=font)
    position = ((width - text_width) // 2, (height - BIT_FONT_SIZE) // 2)
    
    print(f"BIT_TEXT: {BIT_TEXT}")  # Debugging line
    for i, char in enumerate(BIT_TEXT):
        char_width = draw.textlength(char, font=font)
        char_position = (position[0] + draw.textlength(BIT_TEXT[:i], font=font), position[1])
        color = BIT_GRADIENT_COLORS[i % len(BIT_GRADIENT_COLORS)]
        draw.text(char_position, char, fill=color, font=font)
    
    return qr_img

def sanitize_filename(name):
    """Nettoie les noms pour le système de fichiers"""
    return "".join(c if c.isalnum() or c in " _-" else "_" for c in name)

# Liste des colonnes attendues (avec l'espace dans 'First name ')
expected_columns = [
    "ID", 
    "Last Name", 
    "First name ",  # Espace à la fin
    "Gender", 
    "Birth date and place", 
    "Department", 
    "In emergency"
]

try:
    with open(csv_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        
        # Vérification des colonnes
        header = [col.strip() for col in header]  # Nettoie les espaces
        if header != [col.strip() for col in expected_columns]:
            print("Erreur : Les colonnes ne correspondent pas")
            print(f"Attendues: {expected_columns}")
            print(f"Trouvées : {header}")
            exit(1)

        for row in reader:
            if len(row) < 7:
                continue

            # Extraction des données avec les bons indices
            student_id = row[0]
            last_name = row[1].strip()
            first_name = row[2].strip()  # 'First name ' avec espace
            gender = row[3]
            birth = row[4]
            department = row[5]
            emergency = row[6]

            # Création du contenu du QR
            qr_content = f"""ID: {student_id}
Last Name: {last_name}
First Name: {first_name}
Gender: {gender}
Birth: {birth}
Department: {department}
Emergency: {emergency}"""

            # Génération QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=2
            )
            qr.add_data(qr_content)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            
            # Ajout du watermark
            img = add_bit_watermark(img)
            
            # Sauvegarde
            filename = f"{last_name}_{first_name}".replace(" ", "_")
            safe_name = sanitize_filename(filename)[:100]
            img.save(os.path.join(output_dir, f"{safe_name}.png"))

    print(f"Succès! {len(os.listdir(output_dir))} QR codes générés.")

except Exception as e:
    print(f"Erreur: {str(e)}")