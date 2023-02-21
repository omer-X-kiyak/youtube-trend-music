# youtube-trend-music
<h3>
Bu kod, Youtube'da popüler olan videoların başlıklarını ve kanal isimlerini bir dosyaya kaydeder.

Kodda, Selenium kütüphanesi kullanarak bir tarayıcı açılır, Youtube'un popüler videolar sayfasına gidilir ve sayfadaki videoların başlıkları find_elements fonksiyonu kullanılarak alınır. Bu başlıklar daha sonra bir dosyaya yazdırılır.

with anahtar kelimesi ile dosya açılır ve dosya modu w olarak belirtilir, bu mod dosyayı yazmak için açar ve dosyanın içeriğini siler. Daha sonra, bir döngü kullanılarak, her başlık dosyaya yazdırılır. encoding='utf-8' argümanı, dosyada Türkçe karakterleri desteklemek için kullanılır.

Sonuç olarak, kod dosyaya video-title sınıfı altındaki başlıkları yazdırır ve her başlık arasında 2 satır boşluk bırakır.
</h3>
