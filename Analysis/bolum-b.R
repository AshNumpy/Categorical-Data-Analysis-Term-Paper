# Verilere Genel Bakış

library(tidyverse)
library(janitor)
library(MASS)
library(gt)
setwd("C:/Users/ilkay/Documents/GitHub/Categorical-Data-Analysis")
df<- read.csv("C:/Users/ilkay/Documents/GitHub/Categorical-Data-Analysis/Datasets/processed.csv")
glimpse(df)

## RxC

df$likert_5[df$likert_5 ==1] <- "Hiç Katılmıyorum"
df$likert_5[df$likert_5 ==2] <- "Kısmen Katılmıyorum"
df$likert_5[df$likert_5 ==3] <- "Ne Katılıyorum Ne Katılmıyorum"
df$likert_5[df$likert_5 ==4] <- "Kısmen Katılıyorum"
df$likert_5[df$likert_5 ==5] <- "Tamamen Katılıyorum"
df$likert_2[df$likert_2 ==1] <- "Hiç Katılmıyorum"
df$likert_2[df$likert_2 ==2] <- "Kısmen Katılmıyorum"
df$likert_2[df$likert_2 ==3] <- "Ne Katılıyorum Ne Katılmıyorum"
df$likert_2[df$likert_2 ==4] <- "Kısmen Katılıyorum"
df$likert_2[df$likert_2 ==5] <- "Tamamen Katılıyorum"

df |> 
  dplyr::select(likert_2, likert_5) |>
  count(likert_5, likert_2) |> 
  pivot_wider(names_from = likert_5, values_from = n, values_fill = 0) |>
  adorn_totals("row") |> 
  adorn_totals("col") |> 
  
  gt(rowname_col = "likert_2") |> 
  tab_header(
    title= "Telefon kurcalama iznine Göre Giyime Karışma",
    # subtitle = "1 en az 5 en çok",
    
  ) |> 
  tab_stubhead("Telefon Kurcalama İzni") |>
  tab_spanner(label = "Katılım", columns = c("Hiç Katılmıyorum", "Kısmen Katılmıyorum", "Ne Katılıyorum Ne Katılmıyorum", "Kısmen Katılıyorum", "Tamamen Katılıyorum"))


# Telefon kurcalama iznine göre giyime karışmaya izin verme arasındaki ilişki (α = 0.05)
# 
# $H_0:$ Telefon kurcalama izni ile kız/erkek arkadaşın giyime karışması arasında ilişki yoktur.
# 
# $H_s:$ Telefon kurcalama izni ile kız/erkek arkadaşın giyime karışma arasında fark vardır


## Ki Kare

# $\chi_t ^2 = \chi_{(R-1)(C-1)}^2 = \chi_{16; 0.05} ^2 = 26.296$

tablo <- table(df$likert_2, df$likert_5)
chisq.test(tablo)

# $\chi_H^2 = 45.392$
#   
#   Yorum: Telefona karışma izni ile kız/erkek arkadaşın giyime karışması arasında bir ilişki olduğu 95% güven düzeyinde söylenebilir.

## İlişki Katsayısı

# $Phi = \phi = \sqrt{\frac{\chi^2}{n}} = \sqrt{\frac{45.392}{94}} = 0.6949055$
#   
#   telefon kurcalama ile kız/erkek arkadaşın giyimine karışması arasında 70% lik bir ilişki vardır.
# 
# ## Uyum Analizi

library(FactoMineR)
library(factoextra)
tablo <- table(df$likert_2, df$likert_5)
res.ca <- CA(tablo, graph = F)

## Row Based
df |> 
  tabyl(likert_2, likert_5) |> 
  adorn_totals(c("row", "col")) |> 
  adorn_percentages("row") |> 
  adorn_pct_formatting(rounding = "half up", digits = 0) |> 
  adorn_ns() |> 
  adorn_title("combined") |> 
  gt(rowname_col = "likert_2") |> 
  tab_header(
    title= "telefon kurcalama iznine Göre Giyime Karışma Row",
    # subtitle = "1 en az 5 en çok",
    
  ) |> 
  tab_stubhead("Telefona Karışma İzni") |> 
  tab_spanner(label = "Katılım", columns = c("Hiç Katılmıyorum", "Kısmen Katılmıyorum", "Ne Katılıyorum Ne Katılmıyorum", "Kısmen Katılıyorum", "Tamamen Katılıyorum"))

# Kız/erkek arkadaşım telefonumu kurcalayabilir sorusuna hiç katılmayan grubun içinde, kız/erkek arkadaşım giyimime karışabilir sorusuna hiç katılmayanların oranı 84% tür.
# 
# ## Col Based

df |> 
  tabyl(likert_2, likert_5) |> 
  adorn_totals(c("row", "col")) |> 
  adorn_percentages("col") |> 
  adorn_pct_formatting(rounding = "half up", digits = 0) |> 
  adorn_ns() |> 
  adorn_title("combined") |> 
  gt(rowname_col = "likert_2") |> 
  tab_header(
    title= "Telefona karışma iznine Göre Giyime Karışma Col",
    # subtitle = "1 en az 5 en çok",
    
  ) |> 
  tab_stubhead("likert2") |> 
  tab_spanner(label = "Katılım", columns = c("Hiç Katılmıyorum", "Kısmen Katılmıyorum", "Ne Katılıyorum Ne Katılmıyorum", "Kısmen Katılıyorum", "Tamamen Katılıyorum"))

# Kız/erkek arkadaşım telefonumu kurcalayabilir sorusuna tamamen katılanların grubu içinde giyime karışılmasına kısment katılanların oranı 40% tır.
# 
# ## Özdeğerler

eig.val <- get_eigenvalue(res.ca)
eig.val
# 
# Özdeğerler, her bir eksen tarafından tutulan bilgi miktarına karşılık gelir. Boyutlar azalan şekilde sıralanır ve çözümde açıklanan varyans miktarına göre listelenir. 1. boyut , çözümdeki en fazla varyansı açıklar, ardından boyut 2 sonrasında 3. boyut şeklinde gitmektedir.
# 
# \`cumulative.variance.percent\` kısmını incelediğimizde ilk eksenin %99.48 oranında açıkladığını görmekteyiz.
# 
# Özdeğere alternatif olarak scree-plot grafiklerine de bakılabilir.
# 
# #### Scree Plot

fviz_screeplot(res.ca, addlabels = TRUE, ylim = c(0, 50))

# Burada da görüleceği üzere 4. eksenin toplam varyansı açıklamada etkisiz kalmaktadır. Ancak boyut indirgemesi yaparken ortalam özdeğerin altındakileri çıkarmak üzerine bir yaklaşım yapabiliriz.

fviz_screeplot(res.ca) +
  geom_hline(yintercept=33.33, linetype=2, color="red")

# Yukarıdaki grafiğe göre çözümde sadece 1. boyut kullanılmalıdır. 2. 3. ve 4. boyutlar, ortalama özdeğerin (%33.33) altında olan toplam inertianın yalnızca yaklaşık %34'ünü açıklar ve daha fazla analiz için tutulamayacak kadar azdır. (kümülatif değil de ayrı ayrı düşünüldüğünde)
# 
# ## Biplot

fviz_ca_biplot(res.ca, repel = TRUE) 
res.ca


# Mavi noktalar: Satır (telefona karışma izni)
# 
# Kırmızı üçgenler: Sütun, değerlerini temsil etmektedir.(giyime karışma izni)
# 
# Herhangi bir satır noktası veya sütun noktası arasındaki mesafe, benzerliklerinin (veya benzemezliklerinin) bir ölçüsünü verir.
# 
# Grafiğe göre telefonunun kurcalanmasını istemeyen insanların, aynı zamanda giyimlerine de karışılmamasını istemedikleri yorumu yapılabilir. Tam tersi düşünce yapısında da benzer olduğu söylenebilir.
# 
# ## Row Plot

fviz_ca_row(res.ca, col.row = "contrib",
            gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"), 
            repel = TRUE)

# Grafiğe göre hiç katılmayanlar ile tamamen katılanlar iki farklı uçta yer almışlardır. Kısmen katılanlar ve tamamen katılanlar ilişkili iken kararsız olanlar farklılık göstermişlerdir.
# 
# ## Col Plot

fviz_ca_col(res.ca, col.col = "cos2", 
            gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"),
            repel = TRUE)

Grafiğe göre hiç katılmayanlar ile tamamen katılanlar farklı uçlarda yer almışlardır. Kısmen katılanlar ise farklılık göstermişlerdir.


