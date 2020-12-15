library(ggplot2)
data("transfer", package="qss")   #Get transfer data

#calculates cutoff from each threshold
transfer$cutoff_1 = 100 * (transfer$pop82 - 10188)/10188
transfer$cutoff_2 = 100 * (transfer$pop82 - 13584)/13584
transfer$cutoff_3 = 100 * (transfer$pop82 - 16980)/16980

#calculates lowest of these thresholds in terms of their absolute value
transfer$min_cutoff = ifelse(abs(transfer$cutoff_1) < abs(transfer$cutoff_2) & abs(transfer$cutoff_1) < abs(transfer$cutoff_3), transfer$cutoff_1, ifelse(abs(transfer$cutoff_2) < abs(transfer$cutoff_1) & abs(transfer$cutoff_2) < abs(transfer$cutoff_3), transfer$cutoff_2, transfer$cutoff_3))

transfer_below_3 = subset(transfer, abs(min_cutoff) <= 3) #Filters data close to threshold

#Splits data
transfer_neg = subset(transfer_below_3, min_cutoff < 0)
transfer_pos = subset(transfer_below_3, min_cutoff >= 0)


#Calculates line of best fit and correlation constant for each covariate and sides of the threshold, giving 6 lines and 6 constants total
lit_neg <- lm(literate91 ~ min_cutoff, data=transfer_neg)
lit_pos <- lm(literate91 ~ min_cutoff, data=transfer_pos)
lit_neg
cor(transfer_neg$literate91, transfer_neg$min_cutoff)
lit_pos
cor(transfer_pos$literate91, transfer_pos$min_cutoff)

educ_neg <- lm(educ91 ~ min_cutoff, data=transfer_neg)
educ_pos <- lm(educ91 ~ min_cutoff, data=transfer_pos)
educ_neg
cor(transfer_neg$educ91, transfer_neg$min_cutoff)
educ_pos
cor(transfer_pos$educ91, transfer_pos$min_cutoff)

pov_neg <- lm(poverty91 ~ min_cutoff, data=transfer_neg)
pov_pos <- lm(poverty91 ~ min_cutoff, data=transfer_pos)
pov_neg
cor(transfer_neg$poverty91, transfer_neg$min_cutoff)
pov_pos
cor(transfer_pos$poverty91, transfer_pos$min_cutoff)

#Plots each line and set of data points
ggplot(transfer_below_3, aes(x = min_cutoff, y = literate91)) + 
       geom_point(shape = 21) + 
       geom_vline(aes(xintercept = 0), color = 'grey', size = 1, linetype = 'dashed') + 
       geom_segment(data = transfer_neg, aes(x = -3, xend = 0, y = 0.006947928*-3 + 0.775610149, yend = 0.775610149)) + 
       geom_segment(data = transfer_pos, aes(x = 0, xend = 3, y = 0.83125473, yend = -0.01260095*3 + 0.83125473)) + xlab("Points from Threshold") + ylab("Literacy Rate")

ggplot(transfer_below_3, aes(x = min_cutoff, y = educ91)) + 
        geom_point(shape = 21) + 
        geom_vline(aes(xintercept = 0), color = 'grey', size = 1, linetype = 'dashed') + 
        geom_segment(data = transfer_neg,aes(x = -3, xend = 0, y = 0.05922276*-3 + 4.40728390, yend = 4.40728390)) + 
        geom_segment(data = transfer_pos,aes(x = 0, xend = 3, y = 4.9909233, yend = -0.1555516*3 + 4.9909233)) + xlab("Points from Threshold") + ylab("Education Rate")

ggplot(transfer_below_3, aes(x = min_cutoff, y = poverty91)) + 
        geom_point(shape = 21) + 
        geom_vline(aes(xintercept = 0), color = 'grey', size = 1, linetype = 'dashed') + 
        geom_segment(data = transfer_neg,aes(x = -3, xend = 0, y = -0.03382153*-3 + 0.59167396, yend = 0.59167396)) + 
        geom_segment(data = transfer_pos,aes(x = 0, xend = 3, y = 0.53134668, yend = 0.03076418*3 + 0.53134668)) + xlab("Points from Threshold") + ylab("Poverty Rate")
