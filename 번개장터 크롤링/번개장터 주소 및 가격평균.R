# 텍스트 마이닝
library(KoNLP)
library(dplyr)
library(foreign)
library(ggplot2)
library(readxl)

results <- read.csv("/Users/kimsiwoo/Desktop/WORKSPACE/PYTHON/bunjang\ address.csv",
                    header = T)
df_results <- as.data.frame(results, stringsAsFactors = F)
df_results <- rename(df_results,
                     number = X,
                     word = X0)
df_results <- df_results %>%
  group_by(word) %>%
  summarise(n=n()) %>%
  arrange(desc(n)) %>%
  filter(word != "전국" &
    word != "동" &
    word != "서구" &
    word != "위치" &
    word != "남구" &
    word != "아이콘" &
    word != "" &
    word != "" &
    word != "" )

df_results <- df_results %>%
  filter(df_results$n >= 7)

# df_results
price <- read.csv("/Users/kimsiwoo/Desktop/WORKSPACE/PYTHON/bunjang\ price.csv",
                    header = T)
df_price <- as.data.frame(price, stringsAsFactors = T)
df_price <- rename(df_price,
                     number = X,
                     price_tag = X0)

df_price <- as.numeric(gsub(",", "", df_price$price_tag))
# price_tag는 factor이고, 이안에 쉼표도 제거해야함. 이 값들을 숫자값 형태로 만들고 쉼표도 제거

df_price <- as.data.frame(df_price) %>%
  filter(df_price >= 1000,
         df_price <= 10000) %>%
  summarise(mean_price = mean(df_price))

df_results
df_price