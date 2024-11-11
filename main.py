import turtle
import random
import pygame  # Pygame kütüphanesini ekliyoruz
import time

# Pygame'i başlat
pygame.mixer.init()

# Ses dosyasını yükle (örn. "click_sound.wav" adlı bir dosya)
click_sound = pygame.mixer.Sound("click_sound.wav")

# Ekranı oluştur ve ayarla
my_screen = turtle.Screen()
my_screen.title("Kaplumbağa Yakalama Oyunu")  # Ekranın başlığını belirliyoruz
my_screen.bgcolor("lightblue")  # Arka plan rengini belirliyoruz
my_screen.setup(width=800, height=800)  # Ekranın genişlik ve yükseklik ayarları

# Skor ve sayaç değişkenlerini tanımla
score = 0  # Başlangıç skoru 0
time_left = 30  # Oyunun başlangıç süresi (örneğin 30 saniye)

# Skor ve sayaç göstergesini ekrana yazdıran işlev
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-100, 260)  # Skor göstergesini ekranın üst kısmına yerleştiriyoruz
score_display.write(f"Skor: {score}", align="center", font=("Arial", 18, "bold"))

time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.goto(100, 260)  # Sayaç göstergesini ekranın üst kısmına yerleştiriyoruz

# Kaplumbağa nesnesini oluştur
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")  # Kaplumbağa şeklini belirliyoruz
turtle_instance.shapesize(stretch_wid=2, stretch_len=2)
turtle_instance.color("green")  # Rengini yeşil yapıyoruz
turtle_instance.penup()  # İz bırakmadan hareket etmesini sağlıyoruz
turtle_instance.speed("fastest")  # Hareket hızını en hızlı şekilde ayarlıyoruz


# Skoru arttıran işlev
def increase_score(x, y):
    global score
    score += 1  # Skoru bir arttırıyoruz
    score_display.clear()  # Skor göstergesini temizliyoruz
    score_display.write(f"Skor: {score}", align="center", font=("Arial", 18, "bold"))  # Güncellenmiş skoru yazdırıyoruz
    click_sound.play()  # Ses efektini çal


# Kaplumbağaya tıklama olayını bağla
turtle_instance.onclick(increase_score)


# Kaplumbağayı rastgele konumda gösteren işlev
def show_turtle():
    if time_left > 0:  # Süre bitmediyse
        x = random.randint(-280, 280)  # Ekran sınırları dahilinde rastgele x koordinatı
        y = random.randint(-280, 280)  # Ekran sınırları dahilinde rastgele y koordinatı
        turtle_instance.goto(x, y)  # Kaplumbağayı bu konuma taşı
        turtle_instance.showturtle()  # Kaplumbağayı göster
        my_screen.ontimer(hide_turtle, 1000)  # 1 saniye sonra kaplumbağayı gizle


# Kaplumbağayı gizleyen işlev
def hide_turtle():
    turtle_instance.hideturtle()  # Kaplumbağayı gizle
    my_screen.ontimer(show_turtle, 1000)  # 2 saniye sonra kaplumbağayı tekrar göster


# Animasyonlu bitiş mesajı işlevi
def show_final_score():
    final_score_display = turtle.Turtle()
    final_score_display.hideturtle()
    final_score_display.penup()
    final_score_display.goto(0, 0)  # Mesajı ekranın ortasına yerleştiriyoruz

    # Animasyonlu olarak yazıyı büyütme
    for size in range(12, 30, 2):  # Font boyutunu 12'den 30'a kadar büyütüyoruz
        final_score_display.clear()
        final_score_display.write(f"Oyun Bitti!\nSkorunuz: {score}", align="center", font=("Arial", size, "bold"))
        time.sleep(0.1)  # Her yazı boyutu değişikliğinde kısa bir bekleme süresi ekliyoruz


# Süreyi güncelleyen işlev
def update_time():
    global time_left
    time_display.clear()  # Eski süreyi temizle

    if time_left > 0:
        if time_left <= 10:
            # Son 10 saniye ise kırmızı yap ve büyüyüp küçülme efekti ekle
            font_size = 18 + (10 - time_left) % 2 * 4  # Boyutu büyütüp küçültme
            time_display.color("red")
            time_display.write(f"Süre: {time_left}", align="center", font=("Arial", font_size, "bold"))
        else:
            # Normal süre güncelleme
            time_display.color("black")
            time_display.write(f"Süre: {time_left}", align="center", font=("Arial", 18, "bold"))

        time_left -= 1
        my_screen.ontimer(update_time, 1000)  # 1000 milisaniye sonra yeniden çalıştır
    else:
        # Süre dolduğunda bitiş mesajı
        time_display.color("red")
        time_display.write("Süre Doldu!", align="center", font=("Arial", 18, "bold"))
        turtle_instance.hideturtle()  # Kaplumbağayı gizleyerek oyunu sonlandır

        # Bitiş mesajını animasyonlu göster
        show_final_score()


# İlk süre güncellemesini başlat
update_time()

# Kaplumbağayı ilk defa göster
show_turtle()

# Ekranın kapanmaması için
my_screen.mainloop()
