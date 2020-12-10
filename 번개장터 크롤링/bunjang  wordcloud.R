# 텍스트 마이닝
library(KoNLP)
library(dplyr)
library(foreign)
library(ggplot2)
library(readxl)

results <- read.csv("/Users/kimsiwoo/Desktop/WORKSPACE/PYTHON/bunjang title.csv",
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
    word != "판매" &
    word != "구매" &
    word != "양도" &
    word != "팔아요" &
    word != "비니" &
    word != "승희" &
    word != "효정" &
    word != "지호" &
    word != "미미" &
    word != "아린" &
    word != "유아" &
    word != "팝니다" &
    word != "가격" &
    word != "판매합니다" &
    word != "양도합니다" &
    word != "구해요" &
    word != "교환" &
    word != "구합니다" &
    word != "삽니다" )



library(wordcloud)
library(RColorBrewer)
par(family = "AppleGothic")

# omg_ko_count %>% wordcloud2()
# omg_ko_count[2:length(omg_ko_count)] %>% wordcloud2()
 pal <- brewer.pal(5, "Dark2")   # 단어 색상 목록 만들기
 set.seed(19275)                      # 난수 고정하기

wordcloud(words = df_results$word,     # 단어
           freq = df_results$n,      # 빈도
           min.freq = 1,             # 최소 단어 빈도
           max.words = 100,          # 표현 단어 수
           random.order = F,         # 고빈도 단어 중앙 배치
           rot.per = .1,              # 회전 단어 비율
           scale = c(2,1),         # 단어 크기 범위
           colors = pal)             # 색상 목록
