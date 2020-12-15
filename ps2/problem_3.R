length(leaders$country)
length(unique(leaders$country))
length(leaders$year)/(max(leaders$year) - min(leaders$year))

leaders$success <- ifelse(grepl("die", leaders$result, ignore.case = TRUE), 1, 0)
mean(leaders$success)
mean(subset(leaders, success == 1)$politybefore)
mean(subset(leaders, success == 0)$politybefore)
t.test(subset(leaders, success == 1)$politybefore, subset(leaders, success == 0)$politybefore)

mean(subset(leaders, success == 1)$age)
mean(subset(leaders, success == 0)$age)
t.test(subset(leaders, success == 1)$age, subset(leaders, success == 0)$age)
leaders$warbefore <- ifelse(leaders$civilwarbefore == 1 | leaders$interwarbefore == 1, 1, 0)

mean(subset(leaders, warbefore == 1)$politybefore)
mean(subset(leaders, warbefore == 0)$politybefore)
t.test(subset(leaders, warbefore == 1)$politybefore, subset(leaders, warbefore == 0)$politybefore)

mean(subset(leaders, warbefore == 1)$age)
mean(subset(leaders, warbefore == 0)$age)
t.test(subset(leaders, warbefore == 1)$age, subset(leaders, warbefore == 0)$age)

leaders$warafter <- ifelse(leaders$civilwarafter == 1 | leaders$interwarafter == 1, 1, 0)
t.test(subset(leaders, success == 1)$polityafter, subset(leaders, success == 1)$politybefore)
t.test(subset(leaders, success == 0)$polityafter, subset(leaders, success == 0)$politybefore)
t.test(subset(leaders, success == 1)$warbefore, subset(leaders, success == 1)$warafter)
t.test(subset(leaders, success == 0)$warbefore, subset(leaders, success == 0)$warafter)
