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


library(wordcloud)
library(RColorBrewer)
par(family = "AppleGothic")

# omg_ko_count %>% wordcloud2()
# omg_ko_count[2:length(omg_ko_count)] %>% wordcloud2()
 pal <- brewer.pal(8, "Dark2")   # 단어 색상 목록 만들기
 set.seed(1234)                      # 난수 고정하기

wordcloud(words = df_results$word,     # 단어
           freq = df_results$n,      # 빈도
           min.freq = 2,             # 최소 단어 빈도
           max.words = 100,          # 표현 단어 수
           random.order = F,         # 고빈도 단어 중앙 배치
           rot.per = .1,              # 회전 단어 비율
           scale = c(6,0.4),         # 단어 크기 범위
           colors = pal)             # 색상 목록
