## Çözümleme - C
# Belirlediğiniz iki değişken için odds oranını hesaplayarak yorumlayınız ve önem kontrolünü yapınız.

# **Belirlenen Değişkenler:** \

# 1. Cinsiyet: Kadın, Erkek \
# 2. Soru 10: Kız/Erkek ilişkilerinde başarının anahtarı sizce nedir?
  
df <- read.csv("../Datasets/processed.csv")
head(df, 3)

unique(df$soru10)

library(dplyr)
df$soru10 <- recode(df$soru10,
                    "İletişim becerileri" = "A",
                    "Karşılıklı sevgi ve anlayış" = "B",
                    "Ortak ilgi ve hobiler" = "C")
unique(df$soru10)

# Bu kısımda kategorik seçenekler çıktıda çok yer kaplamasın diye encode ettim.

tablo <- xtabs(~ Sex + soru10, data = df)
tablo

### ODDS Oranlarının Hesaplanması

#install.packages("vcd")
library(vcd)
odds <- loddsratio(tablo, correct = any(tablo == 0L), log = F)
odds

# **Yorumlamalar:** \
# 
# - Erkeklerin kadınlara göre ilişkilerinde başarının anahtarını, karşılıklı sevgi ve anlayış (A) olarak görmesi olasılığı İletişim becerileri (B) olarak görmesi olasılığından 0.8357143 kat azdır. \
# 
# - Kadınların erkeklere göre ilişkilerinde başarının anahtarını, karşılıklı sevgi ve anlayış (A) olarak görmesi olasılığı İletişim becerileri (B) olarak görmesi olasılığından 1.19 ($1 / 0.8357143 \approx 1.19$) kat fazladır. \
# 
# - Erkeklerin kadınlara göre ilişkilerinde başarının anahtarını, İletişim becerileri (B) olarak görmesi olasılığı Ortak ilgi ve hobiler (C) olarak görmesi olasılığından 2.1538462 kat fazladır. \
# 
# 
# **Not!** \
# R dilinde, kategorik değişkenlerin referans kategorileri varsayılan olarak alfabetik veya sayısal olarak en düşük değer olan kategori olarak atanır. \
# 
# Bu durumda, "Sex" değişkeni "Erkek" ve "Kadın" kategorilerini içeriyor. R, bu durumda "Erkek" kategorisini referans kategorisi olarak kabul eder ve diğer kategorilerle karşılaştırmalar yapar. Dolayısıyla, çıktılarda "Erkek" kategorisi için referans olarak alınır.

### Önem Kontrolü

confint(odds)

# $$
#   H_0: \theta_{12} = 1 
# $$
#   $$
#   H_1: \theta_{12} \neq 1
# $$
#   Güven aralığı 1'i içerdiği için $H_0$ reddedilemez ve $\theta_{12}$'nin istatistiksel olarak anlamlı olmadığı %94 güvenle söylenebilir.
# 
# $$
#   H_0: \theta_{13} = 1 
# $$
#   $$
#   H_1: \theta_{13} \neq 1
# $$
#   Güven aralığı 1'i içerdiği için $H_0$ reddedilemez ve $\theta_{13}$'nin istatistiksel olarak anlamlı olmadığı %94 güvenle söylenebilir.
