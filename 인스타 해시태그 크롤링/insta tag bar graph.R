# 텍스트 마이닝
library(KoNLP)
library(dplyr)
library(foreign)
library(ggplot2)
library(readxl)

results <- read.csv("/Users/kimsiwoo/Desktop/WORKSPACE/PYTHON/results.csv",
                    header = T)
df_results <- as.data.frame(results, stringsAsFactors = F)
df_results <- rename(df_results,
                     number = X,
                     word = X0)
df_results <- df_results %>%
  group_by(word) %>%
  summarise(n=n()) %>%
  arrange(desc(n)) %>%
  filter(word != "오마이걸" &
           word != "ohmygirl" &
           word != "OHMYGIRL" )
df_results <- df_results %>%
  filter(df_results$n >= 12)

library(wordcloud)
library(RColorBrewer)
par(family = "AppleGothic")
theme_set(theme_gray(base_family="AppleGothic"))

ggplot(data=df_results, aes(reorder(word, -n) ,y= n)) + geom_col()