import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os

# ARCHIVO JSON PARA AGREGAR USUARIOS
USER_DATA_FILE = "users.json"

# VERIFICAR SI EL JSON EXISTE, SI NO EXISTE, LO CREO
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as file:
        json.dump({}, file)

# CARGAR USUARIOS EN EL JSON
def carga_usuarios():
    with open(USER_DATA_FILE, "r") as file:
        return json.load(file)

# GUARDAR USUARIOS EN EL JSON
def guarda_usuarios(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

# FUNCIÓN PARA MOSTRAR LA PANTALLA PRINCIPAL (HOME)
def show_home_screen():
    # Limpia la ventana actual
    for widget in root.winfo_children():
        widget.destroy()

    # Configura el título de la ventana y el tamaño (celular)
    root.title("Home - Workea")
    root.geometry("300x550")# Tamaño fijo adecuado para pantallas pequeñas
    

    # Contenedor principal para el scroll
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    # Canvas para hacer scroll
    canvas = tk.Canvas(container, bg="orange", width=330, height=300)  
    canvas.pack(side="left", fill="both", expand=True)

    # Barra de desplazamiento (siempre visible)
    v_scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    v_scrollbar.pack(side="right", fill="y")

    h_scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    h_scrollbar.pack(side="bottom", fill="x")

    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Frame dentro del Canvas para contenido desplazable
    scrollable_frame = tk.Frame(canvas, bg="orange", width=100)
    scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

    # Agrega el frame desplazable al Canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    
    # Contenedor para el título y la imagen
    title_frame = tk.Frame(scrollable_frame, bg="orange")
    title_frame.pack(pady=2, anchor="s")

    # Imagen (cargar y mostrar)
    icon_path = "maletin.png"  # Reemplaza con la ruta de tu imagen
    if os.path.exists(icon_path):
       icon_img = Image.open(icon_path)
       icon_img = icon_img.resize((60, 60), Image.Resampling.LANCZOS)
       icon_photo = ImageTk.PhotoImage(icon_img)
       tk.Label(title_frame, image=icon_photo, bg="orange").image = icon_photo
       tk.Label(title_frame, image=icon_photo, bg="orange").pack(side="left", padx=5)
   
    # TÍTULO
    tk.Label(scrollable_frame, text="Ofertas de Trabajo", 
             font=("Arial Black", 14, "bold"), bg="orange", 
             fg="black").pack(pady=2)

    # LISTAS DE TRABAJO SIMULADAS CON DESCRIPCIÓN
    offers = [
        {
            "titulo": "Desarrollador Fullstack - Remoto",
            "pago": "$140000 $/semana",
            "tiempo": "6 meses",
            "experiencia": "3 años de experiencia en desarrollo web"
        },
        {
            "titulo": "Diseñador UX/UI - Tiempo Completo",
            "pago": "$900000 $/mes",
            "tiempo": "Indefinido",
            "experiencia": "2 años de experiencia en diseño de interfaces"
        },
        {
            "titulo": "Redactor de Contenidos - Freelance",
            "pago": "$500000 $/proyecto",
            "tiempo": "1 mes",
            "experiencia": "sin experiencia"
        },
        {
            "titulo": "Community Manager - Medio Tiempo",
            "pago": "$800000 $/mes",
            "tiempo": "Indefinido",
            "experiencia": "1 año de experiencia en gestión de redes sociales"
        },
        {
            "titulo": "Marketing Digital - Freelance",
            "pago": "$100000 $/proyecto",
            "tiempo": "2 meses",
            "experiencia": "2 años de experiencia en marketing digital"
        }
    ]

    # MOSTRAR LAS OFERTAS CON DESCRIPCIÓN
    for offer in offers:
        frame = tk.Frame(scrollable_frame, bg="#0D3C57", padx=3,
                         pady=3, relief="groove", borderwidth=2)
        frame.pack(pady=2, fill="both", padx=2)

        # Título del trabajo
        tk.Label(frame, text=offer["titulo"], font=("Arial", 12, "bold"), 
                 bg="white", anchor="w").pack(fill="x")
        
        # Descripción del trabajo
        tk.Label(frame, text=f"Pago: {offer['pago']}", 
                font=("Arial", 8), 
                bg="white", anchor="w").pack(fill="x")
        tk.Label(frame, text=f"Duración: {offer['tiempo']}", 
                font=("Arial", 8), bg="white", 
                anchor="w").pack(fill="x")
        tk.Label(frame, text=f"Experiencia requerida: {offer['experiencia']}", 
                font=("Arial", 8), bg="white", anchor="w").pack(fill="x")

    # BOTÓN DE PERFIL
    tk.Button(scrollable_frame, text="Aplicar", 
            font=("Arial Black", 12), bg="#0D3C57", 
            fg="#FFFFFF", command=show_profile_screen).pack(pady=10)
    
    
    
    # Barra inferior con íconos
    bottom_frame = tk.Frame(root, bg="#0D3C57", height=50)
    bottom_frame.pack(fill="x")

    icons = ["gente.png", "corazon.png", "nuevo-mensaje.png", "mapa.png", "buscar.png"]

    for icon in icons:
        if os.path.exists(icon):
            img = Image.open(icon)
            img = img.resize((30, 30), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            btn = tk.Button(bottom_frame, image=photo, bg="#0D3C57", borderwidth=0)
            btn.image = photo
            btn.pack(side="left", expand=True, padx=10)

     # Botón Cerrar Sesión
    logout_button = tk.Button(root, text="Cerrar Sesión", bg="#85929e", fg="#000000", relief="flat", 
                    font=("Arial Black", 8), command=show_login_screen)
    logout_button.pack(pady=10, side= "bottom")
    

    
    
# FUNCIÓN PARA MOSTRAR LA PANTALLA DEL PERFIL
# FUNCIÓN PARA MOSTRAR LA PANTALLA DEL PERFIL
def show_profile_screen():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Perfil - Workea")

    # Contenedor principal para el scroll
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    # Canvas para hacer scroll
    canvas = tk.Canvas(container, bg="orange")
    canvas.pack(side="left", fill="both", expand=True)

    # Barras de desplazamiento
    v_scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    v_scrollbar.pack(side="right", fill="y")

    h_scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    h_scrollbar.pack(side="bottom", fill="x")

    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Frame dentro del Canvas para contenido desplazable
    scrollable_frame = tk.Frame(canvas, bg="orange")
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # DETERMINAR EL TIPO DE PERFIL 
    user_type = "freelancer"  # Cambiar a "empresa" según el tipo de usuario

    if user_type == "freelancer":
        tk.Label(scrollable_frame, text="Perfil del Freelancer", font=("Arial Black", 16), bg="#FFBD59", fg="black").pack(pady=10)
        tk.Label(scrollable_frame, text="Nombre: Silvio M", font=("Arial black", 12), bg="#FFBD59", fg="black").pack(pady=5)

        # Espacio para la foto del perfil
        photo_frame = tk.Frame(scrollable_frame, bg="#AE9258")
        photo_frame.pack(pady=5)
        photo_path = "fotodeperfil.png"  # Ruta de la imagen del perfil
        if os.path.exists(photo_path):
            photo_img = Image.open(photo_path)
            photo_img = photo_img.resize((100, 100), Image.Resampling.LANCZOS)
            photo_photo = ImageTk.PhotoImage(photo_img)
            tk.Label(photo_frame, image=photo_photo, bg="#AE9258").image = photo_photo
            tk.Label(photo_frame, image=photo_photo, bg="#AE9258").pack()
        else:
            tk.Label(photo_frame, text="[Foto del perfil]", bg="#AE9258", fg="black", font=("Arial", 10)).pack()

        # Currículum Vitae
        tk.Label(scrollable_frame, text="C.V", font=("Arial black", 14, "bold"), bg="#AE9258", fg="black").pack(pady=5)
        tk.Label(scrollable_frame, text="- Python Developer\n- 5 años de experiencia\n- Django\n- Flask \n- APIs RESTful", font=("Arial Black", 12), 
                bg="#0D3C57", fg="#FFFFFF", justify="left").pack(pady=5)

        # Frame para Opiniones Destacadas
        opinions_frame = tk.Frame(scrollable_frame, bg="#AE9258", padx=10, pady=10, relief="groove", borderwidth=2)
        opinions_frame.pack(pady=10, fill="x", padx=10)
        tk.Label(opinions_frame, text="Opiniones Destacadas", font=("Arial Black", 12, "bold"), bg="#FFBD59", fg="#000000").pack()
        tk.Label(opinions_frame, text="\"Excelente profesional, altamente recomendado!\"\n- Cliente A", font=("Arial", 10), bg="#FFBD59", fg="black", justify="left").pack(pady=5)

        # Espacio para valoración con estrellas
        stars_frame = tk.Frame(scrollable_frame, bg="#0D3C57")
        stars_frame.pack(pady=10)
        star_path = "estrellaentera.png"  # Ruta de la imagen de la estrella
        if os.path.exists(star_path):
            star_img = Image.open(star_path)
            star_img = star_img.resize((20, 20), Image.Resampling.LANCZOS)
            star_photo = ImageTk.PhotoImage(star_img)
            for i in range(5):
                tk.Label(stars_frame, image=star_photo, bg="#0D3C57").image = star_photo
                tk.Label(stars_frame, image=star_photo, bg="#0D3C57").pack(side="left", padx=2)
        else:
            tk.Label(stars_frame, text="[Estrellas aquí]", bg="#AE9258", fg="black", font=("Arial", 10)).pack()
    else:
        tk.Label(scrollable_frame, text="Perfil del Contratista / Empresa", font=("Arial", 16, "bold"), bg="orange", fg="black").pack(pady=10)
        tk.Label(scrollable_frame, text="Empresa: Tech Solutions", font=("Arial", 12), bg="#AE9258", fg="black").pack(pady=5)
        tk.Label(scrollable_frame, text="Trabajo Ofrecido:", font=("Arial", 12, "bold"), bg="#AE9258", fg="black").pack(pady=5)
        tk.Label(scrollable_frame, text="Desarrollador Backend\nProyecto de 6 meses\nPago: $3000/mes", font=("Arial", 12), bg="white", fg="black", justify="left").pack(pady=5)

    # BOTÓN PARA REGRESAR AL HOME
    tk.Button(scrollable_frame, text="Volver", bg="#85929e", fg="#000000", 
              font=("Arial Black", 16), command=show_home_screen).pack(pady=20)

    # Configurar el canvas y barras de desplazamiento
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


    

# FUNCION PARA INICIO DE SESION
def login():
    email = email_entry.get()
    password = password_entry.get()

    users = carga_usuarios()
    if email in users and users[email] == password:
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        show_home_screen()
    else:
        messagebox.showerror("Error", "Correo o contraseña incorrectos")

# FUNCION PARA REGISTRAR UN NUEVO USUARIO
def register():
    email = reg_email_entry.get()
    password = reg_password_entry.get()

    if not email or not password:
        messagebox.showwarning("Advertencia", "Por favor completa todos los campos")
        return

    users = carga_usuarios()
    if email in users:
        messagebox.showerror("Error", "El usuario ya está registrado")
    else:
        users[email] = password
        guarda_usuarios(users)
        messagebox.showinfo("Registro", "Usuario registrado exitosamente")
        show_home_screen()

# PANTALLA INICIAL REGISTRO E INICIO DE SESION
def show_login_screen():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Workea - Inicio de Sesión")

    # LOGO
    logo_path = "Logo aplicación social de tránsito simple azul y rojo claro.png"  
    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((150, 150), Image.Resampling.LANCZOS)

        logo_photo = ImageTk.PhotoImage(logo_img)

        tk.Label(root, image=logo_photo, bg="#0D3C57").image = logo_photo
        tk.Label(root, image=logo_photo, bg="#0D3C57").pack(pady=10)

    tk.Label(root, text="CONECTA OPORTUNIDADES", font=("Arial", 10, "bold"),
            bg="#0D3C57", fg="#FFBD59").pack()

    # SECCION DE INICIO DE SESION
    login_frame = tk.Frame(root, bg="#0D3C57")
    login_frame.pack(pady=10, fill="x")

    global email_entry, password_entry, reg_email_entry, reg_password_entry

    email_entry = tk.Entry(login_frame, width=30, bg="white", fg="black")
    email_entry.insert(0, "Ingresa tu email")
    email_entry.pack(pady=5)

    password_entry = tk.Entry(login_frame, width=30, show="*", bg="white", fg="black")
    password_entry.insert(0, "Contraseña")
    password_entry.pack(pady=5)

    tk.Button(login_frame, text="INICIAR SESIÓN", bg="#85929e", fg="#000000", command=login).pack(pady=5)
    
    # Texto clickeable "¿Olvidaste tu contraseña?"
    forgot_password_label = tk.Label(
    login_frame, 
    text="¿Olvidaste tu contraseña?", 
    fg="#FFBD59", 
    bg="#0D3C57", 
    cursor="hand2"
)
    forgot_password_label.pack()

    # Evento clic para la etiqueta
    def forgot_password_action():
        print("Redirigiendo a recuperación de contraseña...")
    # Agregar la lógica para redirigir al usuario, como abrir una nueva ventana o un enlace web.

    forgot_password_label.bind("<Button-1>", lambda e: forgot_password_action())
    
    def forgot_password_action():
    # Crear una ventana emergente
        popup = tk.Toplevel(root)
        popup.title("Restablecer contraseña")
        popup.geometry("300x150")
        popup.config(bg="#0D3C57")
        popup.iconbitmap("iconologo.ico")

        tk.Label(popup, text="Restablecer contraseña", font=("Arial", 12, "bold"), bg="gray", fg="white").pack(pady=10)
    
    # Campo para nueva contraseña
        new_password_entry = tk.Entry(popup, width=30, show="*", bg="white", fg="black")
        new_password_entry.insert(0, "Nueva contraseña")
        new_password_entry.pack(pady=5)
    
    # Botón para confirmar
        def confirm_reset():
            new_password = new_password_entry.get()
            if new_password.strip() == "" or new_password == "Nueva contraseña":
               tk.Label(popup, text="Por favor, ingresa una contraseña válida.", fg="red", bg="gray").pack()
            else:
               print(f"Contraseña restablecida a: {new_password}")  # Para pruebas
               tk.Label(popup, text="Contraseña actualizada con éxito.", fg="green", bg="gray").pack()
               popup.after(2000, popup.destroy)  # Cerrar después de 2 segundos
    
        tk.Button(popup, text="Confirmar", bg="blue", fg="white", command=confirm_reset).pack(pady=10)

# Texto clickeable
    forgot_password_label.bind("<Button-1>", lambda e: forgot_password_action())


    reg_email_entry = tk.Entry(login_frame, width=30, bg="white", fg="black")
    reg_email_entry.insert(0, "Email")
    reg_email_entry.pack(pady=5)

    reg_password_entry = tk.Entry(login_frame, width=30, show="*", bg="white", fg="black")
    reg_password_entry.insert(0, "Contraseña")
    reg_password_entry.pack(pady=5)

    tk.Button(login_frame, text="REGISTRARSE", bg="#85929e", fg="#000000", command=register).pack(pady=5)

# CONFIGURACION INICIAL
root = tk.Tk()
root.geometry("200x450")
root.configure(bg="#0D3C57")
root.iconbitmap("iconologo.ico")

# MOSTRAR PANTALLA DE INICIO DE SESION
show_login_screen()

# EJECUTAR APLICACION
root.mainloop()


