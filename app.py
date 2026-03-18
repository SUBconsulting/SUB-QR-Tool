import streamlit as st
import streamlit.components.v1 as components
import qrcode
from io import BytesIO
from PIL import Image

#STUDIO SUB GA4
GA_ID = "G-BB7W98MSTQ"

GA_JS = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{GA_ID}');
    </script>
"""

# Esto inserta el script de forma invisible en la app
components.html(GA_JS, height=0)


# Configuración de la página
st.set_page_config(page_title="Generador de QR Pro", page_icon="🚀")

st.title("QR Generator 🗺️")
st.write("Ingresa un link (como Google Maps) para generar tu código QR listo para descargar.")

# Entrada de usuario
url = st.text_input("Pega aquí tu enlace:", placeholder="https://www.google.com/maps/...")

if url:
    # Generación del QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear la imagen en memoria
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convertir a formato que Streamlit pueda mostrar y descargar
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Mostrar vista previa
    st.image(byte_im, caption="Tu código QR generado", width=300)

    # Botón de descarga
    st.download_button(
        label="📥 Descargar Imagen QR",
        data=byte_im,
        file_name="codigo_qr.png",
        mime="image/png"
    )
